<script>
  import Chart from 'chart.js';
  import { onMount } from 'svelte';

  export let name;

  const apiURL = "http://127.0.0.1:8000/stream/abc/query";

  onMount(async () => {

    const response = await fetch(apiURL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        'event_name': 'brandon-test',
        'aggregation': 'p90',
        'rollup': '2h',
        'start_time': 1582581066832,
        'end_time': 1582621270814
      }),
    })
    var data = await response.json();

    var times = data['series'][0]['values'].map(point => point[0])
    var values = data['series'][0]['values'].map(point => point[1])
    console.log(times)
    console.log(values)

    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: times.map(t => Date.parse(t)),
        datasets: [
          {
            data: values.map(v => v || 0)
          }
        ]
      },
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
            }
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

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: 800px;
    }
  }
</style>

<main>
  <h1>Hello {name}!</h1>
  <p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
  <canvas id="myChart" width="400px" height="400px"></canvas>
</main>
