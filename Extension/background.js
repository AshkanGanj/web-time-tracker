/*
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
*/
var mtimer, sec, start,active;
var tabUrlsUpdate = {};
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

function newTimer() {
  clearInterval(mtimer);
  start = new Date().getTime() / 1000;
  Timmer(start);
}

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if (changeInfo.status == "complete" && tab.status == "complete" && tab.url != undefined)
  {
    active = tab.url;
    var lastUrl;
    if (tabUrlsUpdate[tabId]) {
      lastUrl = tabUrlsUpdate[tabId];
      console.log(lastUrl);
      console.log(sec); 
      send(serverUrl, lastUrl, sec);
    }
    else {
      console.log("error");
    }    
    if (tab.url) {
      tabUrlsUpdate[tabId] = tab.url;
    }

    clearInterval(mtimer);
    start = new Date().getTime() / 1000;
    Timmer(start);
  }
});

chrome.tabs.onActivated.addListener(function (activeInfo) {
  chrome.tabs.get(activeInfo.tabId, function (tab) {
    u = tab.url;
    console.log(u);
  });
  if (active != "") {
    console.log("out A " + active);
    console.log(sec);
    send(serverUrl, active, sec);
    active = "";
    newTimer();

  } else {
    console.log("out U " + u);
    console.log(sec);
    send(serverUrl, u, sec);
    newTimer();
  }
});
