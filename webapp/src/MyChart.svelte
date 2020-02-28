<script>

  import Chart from 'chart.js';

  import { onMount, afterUpdate } from 'svelte';

  import { chartTickWidth } from './Stores.js';

  export let times;
  export let values;

  var myChart;

  function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function makeJson(valueList) {
    return {'data': valueList.map(v => v || 0), 'backgroundColor': getRandomColor()}
  }

  afterUpdate(async() => {
    myChart.data.labels = times[0].map(t => Date.parse(t));
    // myChart.data.datasets[0].label = "foo"
    // myChart.data.datasets[0].backgroundColor = 'rgba(255, 99, 132, 0.2)'
    // myChart.data.datasets[0].hoberBackgroundColor = 'rgba(1, 99, 132, 0.9)'
    myChart.data.datasets = values.map(valueList => makeJson(valueList))
    myChart.options.scales.xAxes[0].time = $chartTickWidth
    myChart.update()
  })

  onMount(async () => {
    var ctx = document.getElementById('myChart');
    myChart = new Chart(ctx, {
      type: 'bar',
      data: {
      labels: [],
      datasets: [{data: []}]},
      options: {
        fill: false,
        responsive: false,
        scales: {
          xAxes: [{
            stacked: true,
            type: 'time',
            display: true,
            time: $chartTickWidth,
            scaleLabel: {
              display: true,
              labelString: "Date",
            },
            gridLines: {
              display: false,
            },
          }],
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true,
            },
            display: true,
            scaleLabel: {
              display: true,
              labelString: "brandon-test",
            }
          }]
        }
      }
    });
  });

</script>

<main>
  <canvas id="myChart" width="1200px" height="400px"></canvas>
</main>
