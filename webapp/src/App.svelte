<script>

  import MyChart from './MyChart.svelte'
  import Controller from './Controller.svelte'

  import {selectedAgg, selectedRollup, selectedRange, selectedGroupBy} from './Stores.js';

  $: body = JSON.stringify({
    'event_name': 'response_time',
    'aggregation': $selectedAgg.value,
    'rollup': $selectedRollup.value,
    'start_time': $selectedRange.value[0],
    'end_time': $selectedRange.value[1],
    'group_by': $selectedGroupBy.value,
  })

  let times = [[],[]]
  let values = [[],[]]

  $: fetch("http://127.0.0.1:8000/stream/abcd/query", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: body
    })
    .then(response => response.json())
    .then(json => {
      var serieses = json.series || [{values: []}]
      times = serieses.map(s => s.values.map(point => point[0]));
      values = serieses.map(s => s.values.map(point => point[1]));
    })

</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 100%;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
</style>

<main>
  <Controller/>
  <MyChart times={times} values={values}/>
</main>
