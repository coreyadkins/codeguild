'use strict';

/**
 * This program stores words, and then returns matching "suggestions" to
 * complete a word on command.
 *
 * This variable stores all of the functions which are used for the program.
*/
var completerPrototype = {
  /**
   * Adds a word to the completion list to be stored as a suggestion.
   */
  addCompletion: function(comp) {
    if (_.includes(this.completions, comp)) {
      null; //Is this the best way to tell JS to do nothing?
    } else {
      this.completions.push(comp);
    }
  },
  /**
   * Removes a word from the completion list.
   */
  removeCompletion: function(str) {
    _.remove(this.completions, function(item) {
        return item === str;
    });
  },
  /**
   * Inputs the beginning of a word and outputs a list of suggested words that
   * match the inputted stem.
   */
  complete: function(prefix) {
    var completionsArray = [];
    completionsArray.push(_.filter(this.completions, function(comp) {
      return _.startsWith(comp, prefix);
    }));
    return completionsArray;
  }
};
/**
 * Constructor to create and store an instance of this program.
 */
function Completer() {
  this.completions = [];
}

Completer.prototype = completerPrototype;

var myCompleter = new Completer();
