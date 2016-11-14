(function() {
    var cards = document.querySelectorAll(".card.effect__click");
    for ( var i  = 0, len = cards.length; i < len; i++ ) {
    var card = cards[i];
   console.log(card)
clickListener( card );
    }

function clickListener(card) {
    card.addEventListener( "click", function() {
    var c = this.classList;
    c.contains("flipped") === true ? c.remove("flipped") : c.add("flipped");
    });
  }
})();

function changeOrdinal() {

  var length = items.children.length,
      ordinal = 0;

  // start at the item BEFORE the active one.
  var index = active-1;

  /* if the active item was 0, we're now at -1 so
      set to the last item */
  if (index < 0) {
      index = length-1;
  }

  // now run through adding the ordinals
  while ( ordinal < length ) {
      // add 1 to the ordinal - ordinal cannot be 0.
      ordinal++;

      // check the item definetely exists :)
      var item = items.children[index];
      if ( item && item.style ) {
          // new ordinal value
          item.style[boxOrdinalGroup] = ordinal;
      }

      /* as we are working from active we need to go back to
         the start if we reach the end of the item list */
      if ( index < length-1 ) {
          index++;
      } else {
          index = 0;
      }
  }
}
</script>

<script>
// attach the onclick event
function move(inc){
var box = document.getElementById('outer_box');
var x_pos = box.offsetLeft;
box.style.left = (x_pos+inc) + 'px';
}
