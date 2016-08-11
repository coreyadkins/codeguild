'use strict';

// 1. Input


// 2. Transform
// No transform.

// 3. Create
var MOLE_URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3e/ScalopusAquaticus.jpg';
var HOLE_URL = 'https://metrouk2.files.wordpress.com/2016/03/ad_199293905.jpg?quality=80&strip=all&strip=all';
var NUM_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
   18, 19, 20];

function createNumList() {
  var arr = Array.apply(null, Array(20));
  return arr.map(function(x, i) {
    return i;
  });
}

// 4. Modify and Sync
function pickImg() {
  var imgNum = _.pull(_.sample(NUM_LIST));
  return $('#' + imgNum);
}

function changeToMole(image) {
  image.attr('src', MOLE_URL);
}

function changetoHole(imgNum) {
  $('#' + imgNum).attr('src', HOLE_URL);
  NUM_LIST.push(imgNum);
}

// 5. Main
function removeMole(imgNum) {
  changetoHole(imgNum);
}

function createMole() {
  var image = pickImg();
  changeToMole(image);
}
// 6. Register Functions
function registerInitialEventHandlers() {
  $('#1').on('click', function() {
    var imgNum = 1;
    removeMole(imgNum);
  });
  $('#2').on('click', function() {
    var imgNum = 2;
    removeMole(imgNum);
  });
  $('#3').on('click', function() {
    var imgNum = 3;
    removeMole(imgNum);
  });
  $('#4').on('click', function() {
    var imgNum = 4;
    removeMole(imgNum);
  });
  $('#5').on('click', function() {
    var imgNum = 5;
    removeMole(imgNum);
  });
  $('#6').on('click', function() {
    var imgNum = 6;
    removeMole(imgNum);
  });
  $('#7').on('click', function() {
    var imgNum = 7;
    removeMole(imgNum);
  });
  $('#8').on('click', function() {
    var imgNum = 8;
    removeMole(imgNum);
  });
  $('#9').on('click', function() {
    var imgNum = 9;
    removeMole(imgNum);
  });
  $('#10').on('click', function() {
    var imgNum = 10;
    removeMole(imgNum);
  });
  $('#11').on('click', function() {
    var imgNum = 11;
    removeMole(imgNum);
  });
  $('#12').on('click', function() {
    var imgNum = 12;
    removeMole(imgNum);
  });
  $('#13').on('click', function() {
    var imgNum = 13;
    removeMole(imgNum);
  });
  $('#14').on('click', function() {
    var imgNum = 14;
    removeMole(imgNum);
  });
  $('#15').on('click', function() {
    var imgNum = 15;
    removeMole(imgNum);
  });
  $('#16').on('click', function() {
    var imgNum = 16;
    removeMole(imgNum);
  });
  $('#17').on('click', function() {
    var imgNum = 17;
    removeMole(imgNum);
  });
  $('#18').on('click', function() {
    var imgNum = 18;
    removeMole(imgNum);
  });
  $('#19').on('click', function() {
    var imgNum = 19;
    removeMole(imgNum);
  });
  $('#20').on('click', function() {
    var imgNum = 20;
    removeMole(imgNum);
  });
  $('main').on('load', setInterval(function() {
    createMole();
  }, 1000));
}

$(document).ready(registerInitialEventHandlers());
