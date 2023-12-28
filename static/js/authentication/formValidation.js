$("#password").focus(function (e) {
  e.preventDefault();
  $(".password-help").removeClass("d-none");
});
$("#password").focusout(function (e) {
  e.preventDefault();
  $(".password-help").addClass("d-none");
});

$("#password").on("input", function () {
  let number = /([0-9])/;
  let Caps = /([A-Z])/;
  let Lower = /([a-z])/;
  let password = $(this).val().trim();
  let Valid = true;
  if (password.length >= 8) {
    $(".password-help .charachters").addClass("text-success");
    $(".password-help .charachters").removeClass("text-danger");
  } else {
    $(".password-help .charachters").removeClass("text-success");
    $(".password-help .charachters").addClass("text-danger");
    Valid = false;
  }
  if (password.match(number)) {
    $(".password-help .number").addClass("text-success");
    $(".password-help .number").removeClass("text-danger");
  } else {
    $(".password-help .number").removeClass("text-success");
    $(".password-help .number").addClass("text-danger");
    Valid = false;
  }
  if (password.match(Caps)) {
    $(".password-help .Caps").addClass("text-success");
    $(".password-help .Caps").removeClass("text-danger");
  } else {
    $(".password-help .Caps").removeClass("text-success");
    $(".password-help .Caps").addClass("text-danger");
    Valid = false;
  }
  if (password.match(Lower)) {
    $(".password-help .lower").addClass("text-success");
    $(".password-help .lower").removeClass("text-danger");
  } else {
    $(".password-help .lower").removeClass("text-success");
    $(".password-help .lower").addClass("text-danger");
    Valid = false;
  }
  if (Valid) {
    $(this).addClass("is-valid");
    $(this).removeClass("is-invalid");
  } else {
    $(this).removeClass("is-valid");
    $(this).addClass("is-invalid");
  }
});

$("#passwordMatch").on("input", function () {
  let match = $(this).val();
  let pass = $("#password").val();
  if (match === pass) {
    $(".reg-btn").removeClass("disabled");
    $(".reg-btn").removeAttr("disabled");
    $(".passwordMatch-help").addClass("d-none");
    $(this).addClass("is-valid");
    $(this).removeClass("is-invalid");
  } else {
    $(".passwordMatch-help").removeClass("d-none");
    $(".reg-btn").addClass("disabled");
    $(".reg-btn").attr("disabled", true);
    $(this).removeClass("is-valid");
    $(this).addClass("is-invalid");
  }
});

userNameValdiaton = async function () {
  let username = $("#username").val();
  if (username.length < 3) {
    $("#username").removeClass("is-valid");
    $("#username").addClass("is-invalid");
    $(".username-check").removeClass("d-none");
  } else {
    let res = await fetch("/dashboard/set-login-info/username-check/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username }),
    });
    let info = await res.json();
    if (info.stat != 200) {
      $("#username").removeClass("is-valid");
      $("#username").addClass("is-invalid");
      $(".username-check").removeClass("d-none");
    } else {
      $("#username").removeClass("is-invalid");
      $("#username").addClass("is-valid");
      $(".reg-btn").attr("type", "submit");
      $(".username-check").addClass("d-none");
    }
  }
};

$("#username").on("input", function () {
  userNameValdiaton();
});
