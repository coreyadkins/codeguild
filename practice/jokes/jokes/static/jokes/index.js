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
    var punchline = $(event.currentTarget).children('.punchline');
    revealPunchline(punchline);
  })
}

$(document).on('ready', initializeEventHandlers);
