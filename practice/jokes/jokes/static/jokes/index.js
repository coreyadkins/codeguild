'use strict';

/**
/* Hides all punchlines in the document.
*/
function hidePunchlines() {
  $('.punchline').hide();
}

/**
/* Reveals a specific punchline.
*/
function revealPunchline(punchline) {
  punchline.show();
}

/**
/* Hides all punchlines, then on the click of a setup, reveals the punchline for that joke.
*/
function initializeEventHandlers() {
  hidePunchlines();
  $('section').on('click', function(event){
    var target = $(event.target).parent();
    var punchline = target.children('.punchline')
    revealPunchline(punchline);
  })
}

$(document).on('ready', initializeEventHandlers);
