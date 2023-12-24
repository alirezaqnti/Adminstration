$(".login-btn").click(async function (e) {
  e.preventDefault();
  let username = $("#username").val();
  let password = $("#password").val();

  let res = await fetch("/login/authentiction/", {
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
