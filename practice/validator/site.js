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
/**
 * Generates the regex to test 'name' against.
 */
function getNameMatch() {
  return /\w+\s\w+/;
}
/**
 * Selects the 'name' input box.
 */
function getNameBox() {
  return $('#name');
}
/**
 * Generates the regex to test 'dob' against.
 */
function getDOBMatch() {
  return /\d\d\d\d-\d\d-\d\d/;
}
/**
 * Selects the 'dob' input box.
 */
function getDOBBox() {
  return $('#dob');
}
/**
 * Generates the regex to test 'phone' against.
 */
function getPhoneMatch() {
  return /\d\d\d-\d\d\d-\d\d\d\d/;
}
/**
 * Selects the 'phone' input box.
 */
function getPhoneBox() {
  return $('#phone');
}

// 4. Modify and Sync
/**
 * Toggles the invalid class on or off to mark whether the input text is invalid.
 */
function toggleInvalid(box) {
  box.toggleClass('invalid');
}
/**
 * Checks the input against the correct match. If they do not match and the box
 * is not empty, calls function to make input box yellow.
 */
function validate(match, box, input) {
  var doesMatch = match.test(input);
  var alreadyInvalid = box.hasClass('invalid');
  /**
   * Ensures that an empty form will not be marked as invalid.
   */
  if (input === '') {
    doesMatch = true;
  }
  if (doesMatch === false && alreadyInvalid === false) {
    toggleInvalid(box);
  }
  if (doesMatch === true && alreadyInvalid === true) {
    toggleInvalid(box);
  }
}

// 5. Main
/**
 * Pipes variables to test the 'name' input box for validity.
 */
function validateName() {
  var inputName = getUserName();
  var match = getNameMatch();
  var box = getNameBox();
  validate(match, box, inputName);
}
/**
 * Pipes variables to test the 'dob' input box for validity.
 */
function validateDOB() {
  var inputDOB = getUserDOB();
  var match = getDOBMatch();
  var box = getDOBBox();
  validate(match, box, inputDOB);
}
/**
 * Pipes variables to test the 'phone' input box for validity.
 */
function validatePhone() {
  var inputPhone = getUserPhone();
  var match = getPhoneMatch();
  var box = getPhoneBox();
  validate(match, box, inputPhone);
}

// 6. Register Functions
/**
 * Registers when the user is typing and calls the appropriate function to
 * check validity of input.
 */
function registerInitialEventHandlers() {
  $('#name').on('input', function() {
    validateName();
  });
  $('#dob').on('input', function() {
    validateDOB();
  });
  $('#phone').on('input', function() {
    validatePhone();
  });
}
$(document).ready(registerInitialEventHandlers);
