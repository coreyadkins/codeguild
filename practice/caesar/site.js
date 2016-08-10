'use strict';

/**
 * Returns the ASCII position of the inputted character.
*/
function getIndex(letter) {
  return letter.charCodeAt();
}

/**
 * Returns the ASCII character as a string associated with supplied index.
*/
function getLetter(index) {
  return String.fromCharCode(index);
}

/**
 * Takes in a string and shifts it [key] amount on the alphabet to encrypt
 * the word.
*/

function caesarEncrypt(key, inputWord) {
  var wordAsArray = inputWord.split('');
  var indexArray = _.map(wordAsArray, getIndex);
  var shiftedIndexArray = _.map(indexArray, function(index) {
    var asciiSpace = 32;
    if (index === asciiSpace) {
      return index;
    } else {
      var newIndex = index + key;
    }
    var asciiIndexZ = 122;
    var alphabetsize = 26;
    var asciiMiscCharMin = 91;
    var asciiMiscCharMax = 96;
    if (newIndex > asciiIndexZ) {
      newIndex -= alphabetsize;
    } else if (newIndex >= asciiMiscCharMin && newIndex <= asciiMiscCharMax) {
      newIndex -= alphabetsize;
    }
    return newIndex;
  });
  var outputArray = _.map(shiftedIndexArray, getLetter);
  return outputArray.join('');
}


/**
 * Takes in a string and shifts it back [key] amount on the alphabet to decrypt
 * the word.
 */

function caesarDecrypt(key, inputWord) {
  var wordAsArray = inputWord.split('');
  var indexArray = _.map(wordAsArray, getIndex);
  var shiftedIndexArray = _.map(indexArray, function addKey(index) {
    if (index === 32) {
      return index;
    } else {
      var newIndex = index - key;
    }
    if (newIndex < 65) {
      newIndex += 26;
    } else if (newIndex > 90 && newIndex < 97) {
      newIndex += 26;
    }
    return newIndex;
  });
  var outputArray = _.map(shiftedIndexArray, getLetter);
  return outputArray.join('');
}
