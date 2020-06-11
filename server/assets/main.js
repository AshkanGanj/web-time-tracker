$(document).ready(function () {
  $(".card").hover(
    function () {
      $(this).addClass("shadow-lg").css("cursor", "pointer");
    },
    function () {
      $(this).removeClass("shadow-lg");
    }
  );
});
