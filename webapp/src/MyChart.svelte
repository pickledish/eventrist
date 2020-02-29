<script>

  import Chart from 'chart.js';

  import { onMount, afterUpdate } from 'svelte';

  import { chartTickWidth } from './Stores.js';

  export let serieses;

  var myChart;

  function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function makeJson(tuple) {
    let color = getRandomColor()
    return {
      'label': tuple.label,
      'data': tuple.values.map(v => v || 0),
      'borderColor': color,
      'backgroundColor': color,
      'lineTension': 0,
      'pointRadius': 2,
      'fill': false,
    }
  }

  afterUpdate(async() => {
    myChart.data.labels = serieses[0].times.map(t => Date.parse(t));
    myChart.data.datasets = serieses.map(tuple => makeJson(tuple))
    myChart.options.scales.xAxes[0].time = $chartTickWidth
    myChart.update()
  })

  onMount(async () => {
    var ctx = document.getElementById('myChart');
    myChart = new Chart(ctx, {
      type: 'line',
      data: {
      labels: [],
      datasets: [{data: []}]},
      options: {
        fill: false,
        responsive: false,
        scales: {
          xAxes: [{
            //stacked: true,
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
            //stacked: true,
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
