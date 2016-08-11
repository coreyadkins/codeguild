'use strict';

// 1. Input


// 2. Transform
// No transform.

// 3. Create
var MOLE_URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3e/ScalopusAquaticus.jpg';
var HOLE_URL = 'https://metrouk2.files.wordpress.com/2016/03/ad_199293905.jpg?quality=80&strip=all&strip=all';

// 4. Modify and Sync
function pickImg() {
  var imgNum = Math.floor(Math.random() * 20) + 1;
  return $('#' + imgNum);
}

function changeToMole(image) {
  image.attr('src', MOLE_URL);
}

function changetoHole() {
  $('#1').attr('src', HOLE_URL);
}

// 5. Main
function removeMole() {
  changetoHole();
}

function createMole() {
  var image = pickImg();
  changeToMole(image);
}
// 6. Register Functions
function registerInitialEventHandlers() {
  $('#1').on('click', function() {
    removeMole();
  });
  $('main').on('load', setInterval(function() {
    createMole();
  }, 1000));
}

$(document).ready(registerInitialEventHandlers());
