'use strict';

var completerPrototype = {
  addCompletion: function(comp) {
    this.completions.push(comp);
  },
  removeCompletion: function(str) {
    var index = this.completions.indexOf(str);
    this.completions.splice(index, 1);
  },
  complete: function(prefix) {
    var completionsArray = [];
    for (var i = 0; i < this.completions.length; i += 1) {
      var comp = this.completions[i];
      if (prefix === comp[0]) {
        completionsArray.push(comp);
      }
    }
    return completionsArray;
  }
};

function Completer() {
  this.completions = [];
}

Completer.prototype = completerPrototype;

var myCompleter = new Completer();
