<script>

  import { onMount, afterUpdate } from 'svelte';

  export let times;
  export let values;

  var myChart;

  afterUpdate(async() => {
    console.log(myChart)
    console.log(myChart.data.labels)
    console.log(myChart.data.datasets[0].data)
    myChart.data.labels = times.map(t => Date.parse(t));
    myChart.data.datasets[0].data = values.map(v => v || 0)
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
        time: {
          unit: 'hour',
          unitStepSize: 1
        },
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
