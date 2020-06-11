/*
  developed by Ashkan Ganj
  Github:https://github.com/Ashkan-agc
*/

var endpoint = "/api/ChartData";
var cdata;
function getSeccond(str) {
  var a = str.split(':');
  var seconds = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]); 
  return seconds;
}
const max = getSeccond($("#max").text());
const min = getSeccond($("#min").text());
const sum = getSeccond($("#sum").text());
const dailyData = [parseInt(max),parseInt(min), parseInt(sum)];
console.log(dailyData);

$.ajax({
  method: "GET",
  url: endpoint,
  success: function (data) {
    bar(data);
    circle(data);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});

var dynamicColors = function () {
  var r = Math.floor(Math.random() * 255);
  var g = Math.floor(Math.random() * 255);
  var b = Math.floor(Math.random() * 255);
  return "rgb(" + r + "," + g + "," + b + ")";
};

var poolColors = function (a) {
  var pool = [];
  for (i = 0; i < a; i++) {
    pool.push(dynamicColors());
  }
  return pool;
};

function circle(data) {
  new Chart(document.getElementById("doughnut-chart"), {
    type: "doughnut",
    data: {
      labels: data["label"],
      datasets: [
        {
          label: "time in percentages %",
          backgroundColor: poolColors(data["percentage"].length),
          data: data["percentage"],
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "time in percantage %",
      },
      plugins: {
        colorschemes: {
          scheme: "brewer.Paired12",
        },
      },
    },
  });
}

function bar(data) {
  var ctx = document.getElementById("barchart").getContext("2d");
  var chart = new Chart(ctx, {
    type: "horizontalBar",
    data: {
      labels: data["label"],
      datasets: [
        {
          label: "Time in second",
          data: data["min"],
          backgroundColor: poolColors(data["data"].length),
          borderWidth: 1,
          barThickness: 4,
        },
      ],
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: "visted sites time in second",
      },
      scales: {
        xAxes: [{
          ticks: {
            min: 0
          } 
        }],
        yAxes: [{
        }],
      }
    },
  });
}

var ctx = document.getElementById('areachart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',

    data: {
        labels: ['saturday', 'sunday', 'monday', 'tuesday', 'wendesday', 'thursday', 'friday'],
        datasets: [{
          label: "  My Second dataset",   
          fillColor: "rgb(215,236,251,0.2)",
          strokeColor: "rgba(151,187,205,1)",
          pointColor: "rgba(151,187,205,1)",
          pointStrokeColor: "#fff",
          pointHighlightFill: "#fff",
          pointHighlightStroke: "rgba(151,187,205,1)",
          data: dailyData
        }]
    },

    options: {}
});
