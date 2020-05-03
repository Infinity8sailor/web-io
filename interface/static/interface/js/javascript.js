var endpoint = '/api'; 
		
$.ajax({ 
  method: "GET", 
  url: endpoint, 
  success: function(data) { 
    drawLineGraph(data, 'myChartline'); 
    console.log("drawing"); 
  }, 
  error: function(error_data) { 
    console.log(error_data); 
  } 
}) 


function drawLineGraph(data, id) { 
  var labels = data.labels; 
  var chartLabel = data.chartLabel; 
  var chartdata = data.chartdata; 
  var ctx = document.getElementById(id).getContext('2d'); 
  var chart = new Chart(ctx, { 
    // The type of chart we want to create 
    type: 'line', 

    // The data for our dataset 
    data: { 
      labels: labels, 
      datasets: [{ 
        label: chartLabel, 
        backgroundColor: 'rgb(55, 100, 255)', 
        borderColor: 'rgb(0, 200, 102)', 
        data: chartdata, 
      }] 
    }, 

    // Configuration options go here 
    options: { 
      scales: { 
        xAxes: [{ 
          display: true 
        }], 
        yAxes: [{ 
          ticks: { 
            beginAtZero: true 
          } 
        }] 
      } 
    } 

  }); 
} 
