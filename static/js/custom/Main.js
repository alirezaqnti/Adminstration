function Done(strong, span) {
  $(".alert-light-success strong").html(strong);
  $(".alert-light-success span").html(span);
  $(".alert-light-success").addClass("show");
  setTimeout(() => {
    $(".alert-light-success").removeClass("show");
  }, 3000);
}

function Failed(strong, span) {
  $(".alert-light-danger strong").html(strong);
  $(".alert-light-danger span").html(span);
  $(".alert-light-danger").addClass("show");
  setTimeout(() => {
    $(".alert-light-danger").removeClass("show");
  }, 3000);
}
function Warning(strong, span) {
  $(".alert-light-warning strong").html(strong);
  $(".alert-light-warning span").html(span);
  $(".alert-light-warning").addClass("show");
  setTimeout(() => {
    $(".alert-light-warning").removeClass("show");
  }, 3000);
}
