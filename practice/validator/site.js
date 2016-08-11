'use strict';

// 1. Input
function getUserName() {
  return $('#name').val();
}

function getUserDOB() {
  return $('#DOB').val();
}

function getUserPhone() {
  return $('#phone').val();
}

// 2. Transform Functions
// No transform.

// 3. Create


// 4. Modify and Sync


// 5. Main
function validateForms() {
  var inputName = getUserName();
  var inputDOB = getUserDOB();
  var inputPhone = getUserPhone();
}

// 6. Register Functions
function registerInitialEventHandlers() {
  $('form').on('keydown', function() {
    validateForms();
  });
}
$(document).ready(registerInitialEventHandlers);
