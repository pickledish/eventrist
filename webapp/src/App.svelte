<script>

  import MyChart from './MyChart.svelte'
  import Controller from './Controller.svelte'

  import {selectedName, nameItems, selectedWhere, selectedAgg, selectedRollup, selectedRange, selectedGroupBy} from './Stores.js';
  import {getOrElse} from './util.js'

  $: body = JSON.stringify({
    'event_name': $selectedName.value,
    'aggregation': $selectedAgg.value,
    'rollup': $selectedRollup.value,
    'start_time': $selectedRange.value[0],
    'end_time': $selectedRange.value[1],
    'filters': $selectedWhere.value,
    'group_by': $selectedGroupBy.value,
  })

  function Series(label, times, values) {
    this.label = label;
    this.times = times;
    this.values = values;
  }

  var serieses = [new Series("No Identifier", [], [])]

  function influxToSeries(series) {
    return new Series(
      JSON.stringify(Object.values(getOrElse(series.tags, {"tags": "None"}))),
      series.values.map(point => point[0]),
      series.values.map(point => point[1])
    )
  }

  $: fetch("http://127.0.0.1:8000/stream/abcd/query", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: body
    })
    .then(response => response.json())
    .then(json => {serieses = getOrElse(json.series, []).map(s => influxToSeries(s))})

  fetch("http://127.0.0.1:8000/stream/abcd/names", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
  })
  .then(response => response.json())
  .then(json => $nameItems = json['series'][0]['values'].reduce((acc, val) => acc.concat(val), []))

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
  <MyChart serieses={serieses}/>
</main>
