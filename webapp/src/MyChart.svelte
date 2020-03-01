<script>

  import Chart from 'chart.js';

  import { onMount, afterUpdate } from 'svelte';

  import { selectedRollup } from './Stores.js';

  export let serieses;






  function stringToColor(idString) {
    var hash = 0;
    for (var i = 0; i < idString.length; i++) {
      hash = idString.charCodeAt(i) + ((hash << 5) - hash);
    }
    var colour = '#';
    for (var i = 0; i < 3; i++) {
      var value = (hash >> (i * 8)) & 0xFF;
      colour += ('00' + value.toString(16)).substr(-2);
    }
    return colour;
  }

  function makeJson(tuple) {
    return {
      'label': tuple.label,
      'data': tuple.values.map(v => v || 0),
      'borderColor': stringToColor(tuple.label),
      'backgroundColor': stringToColor(tuple.label),
      'lineTension': 0,
      'pointRadius': 2,
      'fill': isBarChart,
    }
  }

  var myChart;
  var initialized = false;
  var isBarChart = true;






  $: chartTickWidth =
    ($selectedRollup.value === "1m") ? {unit: "minute", unitStepSize: 1} :
    ($selectedRollup.value === "1h") ? {unit: "hour", unitStepSize: 1} :
    ($selectedRollup.value === "6h") ? {unit: "hour", unitStepSize: 6} :
    ($selectedRollup.value === "1w") ? {unit: "week", unitStepSize: 1} :
    ($selectedRollup.value === "30d") ? {unit: "month", unitStepSize: 1} :
    {unit: "day", unitStepSize: 1};

  $: chartOptions = {
    fill: false,
    responsive: false,
    scales: {
      xAxes: [{
        stacked: isBarChart,
        type: 'time',
        display: true,
        time: chartTickWidth,
        scaleLabel: {
          display: true,
          labelString: "Date",
        },
        gridLines: {
          display: false,
        },
      }],
      yAxes: [{
        stacked: isBarChart,
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
  };

  $: {
    if (initialized) {
      myChart && myChart.destroy();
      let myData = (serieses.length == 0) ? {} : {
        labels: serieses[0].times.map(t => Date.parse(t)),
        datasets: serieses.map(tuple => makeJson(tuple)),
      };
      myChart = new Chart(document.getElementById('myChart'), {
        type: isBarChart ? 'bar' : 'line',
        data: myData,
        options: chartOptions,
      });
    } else {
      console.log("Wanted to update the chart but it wasn't ready")
    }
  }

  onMount(async () => {
    initialized = true;
  });

</script>

<main>
  View as Bar Chart: <input type=checkbox bind:checked={isBarChart}>
  <canvas id="myChart" width="1200px" height="400px"></canvas>
</main>
