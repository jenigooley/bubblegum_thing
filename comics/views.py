from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader, Context
from .models import Comic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def index(request):
    latest_comics_list = Comic.objects.order_by('-cover_date')[:5]
    print latest_comics_list
    template = loader.get_template('comics/index.html')
    context = Context({'latest_comics_list': latest_comics_list, })
    return HttpResponse(template.render(context))


def detail(request, comic_id):

    # try:
    #     comic = get_object_or_404(Comic, pk=comic_id)
    #     #comic = comic.objects.order_by('cover_date')
    #     template = loader.get_template('comics/detail.html')
    #     context = Context({'comic': comic})
    #     return HttpResponse(template.render(context))
    # except (KeyError, Comic.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'comics/detail.html',
    #                   {'comic': comic,'error_message': "Invalid.", })
    # else:
    #     return render('comics/detail.html', {'comic': comic})

    class IndexView(generic.ListView):
        template_name = 'comics/index.html'
        context_object_name = 'latest_comic_list'

        def get_queryset(self):
            """Return the last five published questions."""
            return Comic.objects.order_by('-cover_date')[:5]


    class DetailView(generic.DetailView):
        model = Comic
        template_name = 'comics/detail.html'
