'use strict';

var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

/** Takes in a string and shifts it [key] amount on the alphabet to encrypt
the word.
*/
function caesarEncrypt(key, inputWord) {
  var inputWord = inputWord.toUpperCase();
  var i = 0;
  var outputArray = [];
  for (var x = 0; x < inputWord.length; x += 1) {
    var inputLetter = inputWord[x];
    for (var y = 0; y < alphabet.length; y += 1) {
      var letter = alphabet[y];
      if (inputLetter === letter) {
        var index = i + key;
        if (index > 25) {
          index -= 26;
        }
        outputArray.push(alphabet[index]);
      }
      if (i >= 25) {
        i = 0;
        if (inputLetter === ' ') {
          outputArray.push(inputLetter);
        }
      } else {
        i += 1;
      }
    }
  }
  return outputArray.join('');
}

/**Takes in a string and shifts it back [key] amount on the alphabet to
decrypt the word.
*/
function caesarDecrypt(key, inputWord) {
  var inputWord = inputWord.toUpperCase();
  var i = 0;
  var outputArray = [];
  for (var x = 0; x < inputWord.length; x += 1) {
    var inputLetter = inputWord[x];
    for (var y = 0; y < alphabet.length; y += 1) {
      var letter = alphabet[y];
      if (inputLetter === letter) {
        var index = i - key;
        if (index < 0) {
          index += 26;
        }
        outputArray.push(alphabet[index]);
      }
      if (i >= 25) {
        i = 0;
        if (inputLetter === ' ') {
          outputArray.push(inputLetter);
        }
      } else {
        i += 1;
      }
    }
  }
  return outputArray.join('');
}
