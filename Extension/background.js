/*
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
*/
var mtimer, sec, start, tabUrl, x;
const serverUrl = "http://localhost:8000/api/update/";

function Timmer(start) {
  mtimer = setInterval(function () {
    var seconds = new Date().getTime() / 1000;
    var time = parseInt(seconds - start);
    sec = time.toString();
    console.log(sec);
  }, 1000);
}

function send(severUrl, tabUrl, time) {
  var x = new XMLHttpRequest();
  url = severUrl;
  x.open("POST", url);
  x.setRequestHeader("Authorization", "Token " + localStorage.getItem("token"));
  x.send(
    JSON.stringify({
      url: tabUrl,
      time: time,
    })
  );
}

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if (
    changeInfo.status == "complete" &&
    tab.status == "complete" &&
    tab.url != undefined
  ) {
    var lastUrl = x;
    if (tab.url) {
      x = tab.url;
    }
    clearInterval(mtimer);
    
    if (lastUrl) {
      send(serverUrl, lastUrl, sec);
    } else {
      send(serverUrl, x, sec);
    }
    start = new Date().getTime() / 1000;
    Timmer(start);
  }
});

chrome.tabs.onActivated.addListener(function (activeInfo) {
  chrome.tabs.get(activeInfo.tabId, function (tab) {
    start = new Date().getTime() / 1000;
    tabUrl = tab.url;
    Timmer(start);
  });
  if (tabUrl) {
    send(serverUrl, tabUrl, sec);
  } else {
    send(serverUrl, x, sec);
  }
  clearInterval(mtimer);
});
