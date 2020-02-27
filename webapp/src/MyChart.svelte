<script>

  import Chart from 'chart.js';

  import { onMount, afterUpdate } from 'svelte';

  import { chartTickWidth } from './Stores.js';

  export let times;
  export let values;

  var myChart;

  afterUpdate(async() => {
    myChart.data.labels = times.map(t => Date.parse(t));
    myChart.data.datasets[0].label = "foo"
    myChart.data.datasets[0].backgroundColor = 'rgba(255, 99, 132, 0.2)'
    myChart.data.datasets[0].hoberBackgroundColor = 'rgba(1, 99, 132, 0.9)'
    myChart.data.datasets[0].data = values.map(v => v || 0)
    myChart.options.scales.xAxes[0].time = $chartTickWidth
    console.log($chartTickWidth)
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
        responsive: true,
        scales: {
          xAxes: [{
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
  <canvas id="myChart" width="200px" height="200px"></canvas>
</main>
