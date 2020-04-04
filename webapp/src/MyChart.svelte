<script>

  import Chart from 'chart.js';

  import { onMount, afterUpdate } from 'svelte';

  import { selectedRollup, selectedRange, currentView } from './Stores.js';

  import c3 from 'c3';

  export let serieses;






//   function stringToColor(idString) {
//     var hash = 0;
//     for (var i = 0; i < idString.length; i++) {
//       hash = idString.charCodeAt(i) + ((hash << 5) - hash);
//     }
//     var colour = '#';
//     for (var i = 0; i < 3; i++) {
//       var value = (hash >> (i * 8)) & 0xFF;
//       colour += ('00' + value.toString(16)).substr(-2);
//     }
//     return colour;
//   }

//   function makeJson(tuple) {
//     return {
//       'label': tuple.label,
//       'data': tuple.values.map(v => (v || 0).toFixed(2)),
//       'borderColor': stringToColor(tuple.label),
//       'borderWidth': 2, // slightly thinner than the default lines
//       'backgroundColor': stringToColor(tuple.label),
//       'lineTension': 0.02, // corners not so sharp as to cut you
//       'pointRadius': 0, // don't draw individual points, it's a line
//       'pointHitRadius': 8, // make hovering on a point a little easier
//       'fill': ($currentView === "BAR"),
//     }
//   }

//   var myChart;
//   var initialized = false;






//   $: chartTickWidth =
//     ($selectedRollup === "1m")  ? {unit: "minute", unitStepSize: 1} :
//     ($selectedRollup === "1h")  ? {unit: "hour",   unitStepSize: 1} :
//     ($selectedRollup === "6h")  ? {unit: "hour",   unitStepSize: 6} :
//     ($selectedRollup === "1w")  ? {unit: "week",   unitStepSize: 1} :
//     ($selectedRollup === "30d") ? {unit: "month",  unitStepSize: 1} :
//                                   {unit: "day",    unitStepSize: 1};

//   $: chartOptions = {
//     fill: false,
//     responsive: false,
//     // animation: {
//     //   duration: 0
//     // },
//     // tooltips: {
//     //   mode: 'point'
//     // },
//     scales: {
//       xAxes: [{
//         stacked: ($currentView === "BAR"),
//         type: 'time',
//         display: true,
//         time: chartTickWidth,
//         scaleLabel: {
//           display: true,
//           labelString: "Date",
//         },
//         gridLines: {
//           display: false,
//         },
//       }],
//       yAxes: [{
//         stacked: ($currentView === "BAR"),
//         ticks: {
//           beginAtZero: true,
//         },
//         display: true,
//         scaleLabel: {
//           display: true,
//           labelString: "brandon-test",
//         }
//       }]
//     }
//   };

//   $: {
//     if (initialized && $currentView !== "RAW") {
//       myChart && myChart.destroy();
//       let myData = (serieses.length == 0) ? {} : {
//         labels: serieses[0].times.map(t => Date.parse(t)),
//         datasets: serieses.map(tuple => makeJson(tuple)),
//       };
//       myChart = new Chart(document.getElementById('myChart'), {
//         type: $currentView.toLowerCase(),
//         data: myData,
//         options: chartOptions,
//       });
//     } else if ($currentView === "RAW") {
//       myChart && myChart.destroy();
//       document.getElementById('rawEvents').innerHTML = `<div>${JSON.stringify(serieses)}</div>`
//       console.log("Would have shown you the raw events now!")
//     } else {
//       console.log("Wanted to update the chart but it wasn't ready")
//     }
//   }

  var chart;
  var initialized = false;

  $: chartTickFormat =
    ($selectedRollup === "1m")  ? "%H:%M:%S" :
    ($selectedRollup === "1h")  ? "%H:%M" :
    ($selectedRollup === "6h")  ? "%Y-%m-%d %H:%M":
    ($selectedRollup === "1w")  ? "%Y-%m-%d" :
    ($selectedRollup === "30d") ? "%Y-%m-%d" :
                                  "%Y-%m-%d";

  $: {
    if (initialized) {

      console.log(JSON.stringify(serieses.times));
      let fixedSerieses = (serieses.length == 0) ? [{'times': []}] : serieses;
      let parsedTimes = fixedSerieses[0].times.map(t => Date.parse(t));
      let realParsedTimes = (parsedTimes.length == 0) ? [Date.parse("2020-02-21T00:00:00-05:00")] : parsedTimes;
      console.log(JSON.stringify(parsedTimes));

      let arrays = serieses.map(tuple => [tuple.label].concat(tuple.values.map(v => (v || 0))));

      var chart = c3.generate({
        bindto: '#myChart',
        data: {
          x: 'x',
          columns: [
            ['x'].concat(realParsedTimes),
            ...arrays
          ],
          type: ($currentView == 'bar') ? 'bar' : 'line',
          groups: ($currentView == 'bar') ? [arrays.map(arr => arr[0])] : []
        },
        zoom: {
          enabled: true,
          type: 'drag',
          disableDefaultBehavior: true,
          onzoomend: d => $selectedRange = d.map(t => t.getTime()),
        },
        point: {
          r: 0,
            focus: {
            expand: {
              r: 3.5
            }
          }
        },
        axis: {
          x: {
            type: 'timeseries',
            tick: {
              format: chartTickFormat,
              rotate: -45,
              //values: this.every(15, 'minutes'),
            },
          },
        },
        grid: {
          y: {
            show: true,
          },
        },
      });
    } else {
      console.log("Wanted to update the chart but it wasn't ready")
    }
  }

  onMount(async () => {
    initialized = true;
  });



</script>

<style>

  #myChart {
    min-width: 1200px;
    min-height: 400px;
  }

</style>

<main>
  <div id="myChart">helo</div>
  <button on:click={() => $currentView = "bar"}>See Bar Chart</button>
  <button on:click={() => $currentView = "line"}>See Line Chart</button>
  <button on:click={() => $currentView = "raw"}>See Raw Events</button>
  <div id="rawEvents" width="1200px" height="400px"></div>
</main>
