'use strict';

// 1. Input
function getImgUrl() {
  return $('input').val();
}

// 2. Transform Functions
// No transforms.

// 3. Create
function createImg(imageURL) {
  var newImage = $('<img>').attr('src', imageURL);
  return newImage;
}

function createImgLink(imageURL) {
  var imageLink = $('<a></a>').attr('href', imageURL);
  imageLink.text('Image Source');
  return imageLink;
}

function createDeleteLink() {
  var deleteLink = $('<a></a>').attr('href', '');
  deleteLink.text('X');
  return deleteLink;
}

function createImgTile(imageURL) {
  var tile = $('<div></div>');
  var image = createImg(imageURL);
  var link = createImgLink(imageURL);
  var deleteButton = createDeleteLink();
  deleteButton.on('click', function(event) {
    event.preventDefault();
    deleteTile(tile);
  });
  tile.append(image, link, deleteButton);
  return tile;
}

function deleteTile(tile) {
  tile.remove();
  countImages();
  updateHeader();
}


function countImages() {
  return $('div').length;
}

function updateHeader() {
  var imageCount = countImages();
  var headerParagraph = $('span');
  headerParagraph.text(imageCount);
}

// 4. Modify and Sync
function appendImgTile(tile) {
  $('section').append(tile);
  countImages();
  updateHeader();
}

// 5. Main
function addImgTile() {
  var imageURL = getImgUrl();
  var tile = createImgTile(imageURL);
  appendImgTile(tile);
}

// 6. Register Functions
function registerInitialEventHandlers() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    addImgTile();
  });
}

$(document).ready(registerInitialEventHandlers);

// function deleteImage() {}
