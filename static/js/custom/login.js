$(".code-verification").click(function (e) {
  e.preventDefault();
  $("#FormPass").fadeOut(function () {
    $("#FormPass").addClass("d-none"),
      $("#FormPhone").removeClass("d-none"),
      $("#FormPhone").fadeIn();
  });
});

$(".password-login").click(function (e) {
  e.preventDefault();
  if (!$("#FormPhone").hasClass("d-none")) {
    $("#FormPhone").fadeOut(function () {
      $("#FormPhone").addClass("d-none"),
        $("#FormPass").removeClass("d-none"),
        $("#FormPass").fadeIn();
    });
  } else {
    $("#FormCode").fadeOut(function () {
      $("#FormCode").addClass("d-none"),
        $("#FormPass").removeClass("d-none"),
        $("#FormPass").fadeIn();
    });
  }
});

$(".login-btn").click(async function (e) {
  e.preventDefault();
  let username = $("#username").val();
  let password = $("#password").val();

  let res = await fetch("/login/authentiction/password/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: username, password: password }),
  });
  let info = await res.json();
  if (info.stat == 200) {
    Done("خوش آمدید", `${info.Name} عزیز به داشبورد منتقل می شوید`);
    setTimeout(function () {
      window.location.href = "/dashboard/";
    }, 3000);
  } else {
    Failed("متاسفیم!", "نام کاربری یا رمز عبور اشتباه است");
  }
});

$(".Phone-btn").click(async function (e) {
  e.preventDefault();
  let Phone = $("#Phone").val();
  let info = await GetCode(Phone);
  console.log(info);
  if (info.stat == 200) {
    Done("", info.report);
    $("#FormPhone").fadeOut(function () {
      $("#FormPhone").addClass("d-none"),
        $("#FormCode").removeClass("d-none"),
        $("#FormCode").fadeIn();
    });
    setInterval(doUpdate, 1000);
  } else {
    Failed("متاسفیم!", info.report);
  }
});
$(".Code-btn").click(async function (e) {
  e.preventDefault();
  let Code = $("#Code").val();
  let Phone = $("#Phone").val();

  let res = await fetch("/login/authentiction/phone/code/check/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ Code: Code, Phone: Phone }),
  });
  let info = await res.json();
  if (info.stat == 200) {
    Done("خوش آمدید", `${info.Name} عزیز به داشبورد منتقل می شوید`);
    setTimeout(function () {
      window.location.href = "/dashboard/";
    }, 3000);
  } else {
    Failed("متاسفیم!", info.report);
  }
});

var doUpdate = function () {
  $(".countdown").each(function () {
    var count = parseInt($(this).html());
    if (count !== 0) {
      $(this).html(count - 1);
    } else {
      $(".code-countdown").fadeOut(function () {
        $(".code-countdown").addClass("d-none");
        $(".code-resend").removeClass("d-none"), $(".code-resend").fadeIn();
      });
    }
  });
};

GetCode = async function (Phone) {
  let res = await fetch("/login/authentiction/phone/code/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ Phone: Phone }),
  });
  let info = await res.json();
  return info;
};

$(".code-resend").click(async function (e) {
  e.preventDefault();
  let Phone = $("#Phone").val();
  let info = await GetCode(Phone);
  if (info.stat == 200) {
    $(".countdown").html(180);
    $(".code-resend").fadeOut(function () {
      $(".code-resend").addClass("d-none");
      $(".code-countdown").removeClass("d-none"), $(".code-countdown").fadeIn();
    });
  } else {
    Failed("متاسفیم!", "مشکلی پیش آمده ،دقایقی دیگر تلاش کنید");
  }
});
