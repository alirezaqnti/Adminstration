var togglePassword = document.getElementById("toggle-password");
var formContent = document.getElementsByClassName("form-content")[0];
var getFormContentHeight = formContent.clientHeight;

var formImage = document.getElementsByClassName("form-image")[0];
if (formImage) {
  var setFormImageHeight = (formImage.style.height =
    getFormContentHeight + "px");
}
$(".toggle-password").click(function (e) {
  e.preventDefault();
  let x = $(this).prev()[0];
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
});
