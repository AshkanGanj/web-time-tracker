$(document).ready(function(){
    $("#search-input").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#list li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
          $('hr').hide();
      });
    });
  });