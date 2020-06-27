
if (localStorage.getItem("token") === null) {
  login();
  $("a").click(function () {
    chrome.tabs.create({ url: "http://ashkanganj.pythonanywhere.com/signUp/" });
  });
} else {
  $(".login").hide();
  $("#success").text("user logged in successfull");
  $("#logout").click(function () {
    localStorage.removeItem("token");
    login();
  });
  $("#dashboard").click(function () {
    chrome.tabs.create({ url: "http://ashkanganj.pythonanywhere.com/" });
  });
}

function login() {
  $(".logged").hide();
  $("form.ajax").submit(function () {
    var email = $("#email").val();
    var pass = $("#password").val();
    if (email === "" || pass === "") {
      $("#error").text("please enter email or password");
    }
    sendReq(email, pass);
    event.preventDefault;

    return false;
  });
}
function sendReq(email,pass) {
  $.ajax({
    type: "POST",
    url: "http://ashkanganj.pythonanywhere.com/api/login/",
    data: {
      username: email,
      password: pass,
    },
    dataType: "json",
    success: function (response) {
      localStorage.setItem("token", response["token"]);
      logedin();
    },
  });
}
function logedin() {
  $(".login").hide();
  $("#success").text("user logged in successfull");
  
}
