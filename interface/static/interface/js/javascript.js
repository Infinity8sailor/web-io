var endpoint = '/api'; 
		
$.ajax({ 
  method: "GET", 
  url: endpoint, 
  success: function(data) { 
    drawLineGraph(data, 'myChartline'); 
    myDoughnut(data, 'myChartDoughnut');
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
  var chartdata1 = data.chartdata1;
  var ctx = document.getElementById(id).getContext('2d'); 
  var chart = new Chart(ctx, { 
    // The type of chart we want to create 
    type: 'line', 

    // The data for our dataset 
    data: { 
      labels: labels, 
      datasets: [
      { 
        label: chartLabel, 
        backgroundColor: '#39B580', 
        borderColor: 'rgb(0, 150, 0)', 
        borderDash: [5],
        data: chartdata, 
      },
      { 
        label: chartLabel, 
        backgroundColor: '#97C69D', 
        borderColor: 'rgb(255, 0, 0)', 
        borderDash: [6],
        data: chartdata1,
      } 
    ] 
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
      }, 
      responsive : true,
      maintainAspectRatio: true
    },


  }); 
} 

function myDoughnut (data0, id){
  // And for a doughnut chart
  var ctx = document.getElementById(id).getContext('2d'); 
  var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data : {
      datasets: [
        {
        data: [10, 20, 30, 50,45,55],
        backgroundColor: [
        '#0BA462',
        '#39B580',
        '#67C69D',
        '#95D7BB',
        '#06D8CC',
        '#5F8F55'
      ]
      }],
      
      // These labels appear in the legend and in the tooltips when hovering different arcs
      labels: [
        'Red',
        'Yellow',
        'Blue'
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  });
}
