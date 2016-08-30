'use strict';

function hidePunchlines() {
  $('.punchline').hide();
}

function revealPunchline() {
  $('section.punchline').show();
}

function initializeEventHandlers() {
  hidePunchlines;
  $('section').on('click', function(event){
    revealPunchline;
  })
}

$(document).on('ready', initializeEventHandlers);
