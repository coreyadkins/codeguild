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
    completionsArray.push(_.filter(this.completions, function(comp) {
      return _.startsWith(comp, prefix);
    }));
    return completionsArray;
  }
};

function Completer() {
  this.completions = [];
}

Completer.prototype = completerPrototype;

var myCompleter = new Completer();
