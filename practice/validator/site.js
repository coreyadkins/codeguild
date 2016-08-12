'use strict';

// 1. Input
/**
 * Gathers what has been typed in the 'name' field for each event.
 */
function getUserName() {
  return $('#name').val();
}
/**
 * Gathers what has been typed in the 'DOB' field for each event.
 */
function getUserDOB() {
  return $('#dob').val();
}
/**
 * Gathers what has been typed in the 'Phone' field for each event.
 */
function getUserPhone() {
  return $('#phone').val();
}

// 2. Transform Functions
// No transform.

// 3. Create
var NAME_MATCH = /^([a-z]+\s[a-z]+)?$/i;
var DOB_MATCH = /^(\d{4}-\d{2}-\d{2})?$/;
var PHONE_MATCH = /^(\d{3}-\d{3}-\d{4})?$/;
/**
 * Selects the 'name' input box.
 */
function getNameBox() {
  return $('#name');
}
/**
 * Selects the 'dob' input box.
 */
function getDOBBox() {
  return $('#dob');
}
/**
 * Selects the 'phone' input box.
 */
function getPhoneBox() {
  return $('#phone');
}

// 4. Modify and Sync
/**
 * Turns on the invalid class to mark that the input text is invalid.
 */
function addInvalid(box) {
  box.attr('class', 'invalid');
}
/**
 * Turns off the invalid class to mark that the input text is valid.
 */
function removeInvalid(box) {
  box.removeClass('invalid');
}
/**
 * Checks the input against the correct match. If they do not match and the box
 * is not empty, calls function to make input box yellow.
 */
function validate(match, box, input) {
  var doesMatch = match.test(input);
  /**
   * Ensures that an empty form will not be marked as invalid.
   */
  if (doesMatch === false) {
    addInvalid(box);
  }
  if (doesMatch === true) {
    removeInvalid(box);
  }
}

// 5. Main
/**
 * Pipes variables to test the 'name' input box for validity.
 */
function validateName() {
  var inputName = getUserName();
  var box = getNameBox();
  validate(NAME_MATCH, box, inputName);
}
/**
 * Pipes variables to test the 'dob' input box for validity.
 */
function validateDOB() {
  var inputDOB = getUserDOB();
  var box = getDOBBox();
  validate(DOB_MATCH, box, inputDOB);
}
/**
 * Pipes variables to test the 'phone' input box for validity.
 */
function validatePhone() {
  var inputPhone = getUserPhone();
  var box = getPhoneBox();
  validate(PHONE_MATCH, box, inputPhone);
}

// 6. Register Functions
/**
 * Registers when the user is typing and calls the appropriate function to
 * check validity of input.
 */
function registerInitialEventHandlers() {
  $('#name').on('input', validateName);
  $('#dob').on('input', validateDOB);
  $('#phone').on('input', validatePhone);
  $('form').on('submit', function(event) {
    event.preventDefault();
  });
}
$(document).ready(registerInitialEventHandlers);
