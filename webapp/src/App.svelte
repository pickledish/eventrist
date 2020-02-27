<script>
  import Chart from 'chart.js';

  import Select from 'svelte-select';
  import MyChart from './MyChart.svelte'

  function getTimeRange(offsetMs) {
    var now = Date.now();
    var then = now - offsetMs
    return [then, now]
  }

  const items = [
    {value: getTimeRange(3600000),    label: 'Last 1 hour'},
    {value: getTimeRange(21600000),   label: 'Last 6 hours'},
    {value: getTimeRange(86400000),   label: 'Last 24 hours'},
    {value: getTimeRange(172800000),  label: 'Last 48 hours'},
    {value: getTimeRange(604800000),  label: 'Last 7 days'},
    {value: getTimeRange(2592000000), label: 'Last 30 days'}
  ];

  let selectedValue = items[2];

  $: body = JSON.stringify({
    'event_name': 'response_time',
    'aggregation': 'cnt',
    'rollup': '1h',
    'start_time': selectedValue.value[0],
    'end_time': selectedValue.value[1]
  })

  let apiURL = "http://127.0.0.1:8000/stream/abcd/query";

  let times = []
  let values = []

  $: fetch(apiURL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: body
    })
    .then(response => response.json())
    .then(json => {
      times = json['series'][0]['values'].map(point => point[0]);
      values = json['series'][0]['values'].map(point => point[1]);
    })

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
  <Select {items} bind:selectedValue></Select>
  <MyChart times={times} values={values}/>
</main>
