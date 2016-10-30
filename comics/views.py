import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader, Context
from .models import Comic, People, Publisher, UserComic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import NewComicForm
import comic_vine_api
import pprint


class IndexView(generic.ListView):
    template_name = 'comics/index.html'
    context_object_name = 'latest_comic_list'

    def get_queryset(self):
        return list(Comic.objects.all())


class DetailView(generic.DetailView):
    model = Comic
    template_name = 'comics/detail.html'
    queryset = Comic.objects.all()


class ComicAdd(CreateView):

    model = Comic
    form_class = NewComicForm

    def form_valid(self, form):
        new_pub = {}
        new_peeps = {}
        if form.is_valid():
            data = form.cleaned_data
            first = data['first_issue']
            last = data['last_issue'] + 1
            del data['first_issue']
            del data['last_issue']

        for num in range(first, last):
            add_one = comic_vine_api.main(data, num)
            org_result = {k: v for k, v in add_one.items()}
            if add_one.get('publisher'):
                try:
                    new_pub['publisher'] = add_one['publisher']
                    del add_one['publisher']
                    new_publisher = Publisher(** new_pub)
                    new_publisher.save()
                    pprint.pprint(add_one)
                except:
                    pass

                for k in ['writer', 'artist', 'letterer']:
                    try:
                        if add_one.get('writer'):
                            new_peeps['name'] = add_one['writer']
                            new_peeps['role'] = 'writer'
                            del add_one['writer']
                        if add_one.get('artist'):
                            new_peeps['name'] = add_one['artist']
                            new_peeps['role'] = 'artist'
                            del add_one['artist']
                        if add_one.get('letterer'):
                            new_peeps['name'] = add_one['letterer']
                            new_peeps['role'] = 'letterer'
                            del add_one['letterer']

                        new_people = People(**new_peeps)
                        new_people.save()
                    except:
                        pass
            people_art = People.objects.filter(name=org_result['artist']).first()
            people_write = People.objects.filter(name=org_result['writer']).first()
            people_letter = People.objects.filter(name=org_result['letterer']).first()


            if not people_art:
                people_art = People.objects.create(name=org_result['artist'])
            if not people_write:
                people_write = People.objects.create(name=org_result['writer'])
            if not people_letter:
                people_letter = People.objects.create(name=org_result['letterer'])

            publisher = Publisher.objects.filter(publisher=org_result['publisher']).first()
            if not publisher:
                publisher = Publisher.objects.create(publisher=org_result['publisher']).first()
            new_comic = Comic(artist=people_art, writer=people_write, letterer=people_letter,
                              publisher=publisher, **add_one)
            #import pdb; pdb.set_trace()
            new_comic.cover_date = datetime.datetime.strptime(org_result['cover_date'], '%Y-%m-%d')
            new_comic.save()
            print ('ID', new_comic.id)
            print (self.request.user.id)
            user_comic = UserComic.objects.create(comic_issue=new_comic, user_id=self.request.user)
            user_comic.save()
            #import pdb; pdb.set_trace()
        return HttpResponseRedirect('/comic-detail')


class ComicUpdate(UpdateView):
    model = Comic
    fields = ['name']


class ComicDelete(DeleteView):
    model = Comic
    success_url = reverse_lazy('comic-list')
