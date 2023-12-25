$(document).ready(function () {
  var t = $("#alter_pagination").DataTable({
    // 'dom': 'Bfrtip',
    // "pagingType": "full_numbers",
    paging: false,
    oLanguage: {
      // "oPaginate": {
      //     "sFirst": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-right"><polyline points="9 18 15 12 9 6"></polyline></svg>',
      //     "sPrevious": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
      //     "sNext": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-left"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>',
      //     "sLast": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-left"><polyline points="15 18 9 12 15 6"></polyline></svg>'
      // },
      sInfo: "صفحه _PAGE_ از _PAGES_",
      sSearch:
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
      sSearchPlaceholder: "جستجو کنید...",
      sLengthMenu: "نتایج :  _MENU_",
    },
    stripeClasses: [],
    lengthMenu: [7, 10, 20, 50],
    pageLength: 7,
  });
});
$("body").on("click", ".ADDTeam", function (e) {
  e.preventDefault();
  $("#NewTeamModal").modal("show");
});
$(".NewTeamButt").click(async function (e) {
  e.preventDefault();
  let f = $(".NewTeamForm");
  let form = new FormData(f[0]);
  let res = await fetch("/admins/new-team-register/", {
    method: "post",
    body: form,
  });
  let info = await res.json();
  console.log(info);
  if ((info.stat = 200)) {
    let data = GetTeamData();
    console.log(data);
    window.location.reload();
  }
});
GetTeamData = async function () {
  let res = await fetch("/admins/get-team-data/");
  let info = await res.json();
  console.log(info);
  return info;
};
