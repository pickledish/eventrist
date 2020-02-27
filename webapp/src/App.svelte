<script>
  import Chart from 'chart.js';

  import Select from 'svelte-select';
  import MyChart from './MyChart.svelte'

  function getTimeRange(offsetMs) {
    var now = Date.now();
    var then = now - offsetMs
    return [then, now]
  }

  const timeItems = [
    {value: getTimeRange(3600000),    label: 'Last 1 hour'},
    {value: getTimeRange(21600000),   label: 'Last 6 hours'},
    {value: getTimeRange(86400000),   label: 'Last 24 hours'},
    {value: getTimeRange(172800000),  label: 'Last 48 hours'},
    {value: getTimeRange(604800000),  label: 'Last 7 days'},
    {value: getTimeRange(2592000000), label: 'Last 30 days'}
  ];

  let timeSelectedValue = timeItems[2];

  const aggItems = [
    {value: "cnt", label: 'Count'},
    {value: "max", label: 'Max'},
    {value: "min", label: 'Min'},
    {value: "avg", label: 'Average'},
    {value: "sum", label: 'Sum'},
    {value: "p50", label: 'P-50'},
    {value: "p75", label: 'P-75'},
    {value: "p90", label: 'P-90'},
    {value: "p95", label: 'P-95'},
    {value: "p99", label: 'P-99'}
  ];

  let aggSelectedValue = aggItems[0];

  const rollupItems = [
    {value: "1m", label: '1 Minute'},
    {value: "1h", label: '1 Hour'},
    {value: "1d", label: '1 Day'},
  ];

  let rollupSelectedValue = rollupItems[1];

  $: body = JSON.stringify({
    'event_name': 'response_time',
    'aggregation': aggSelectedValue.value,
    'rollup': rollupSelectedValue.value,
    'start_time': timeSelectedValue.value[0],
    'end_time': timeSelectedValue.value[1]
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
      var series = json.series || [{values: []}]
      times = series[0]['values'].map(point => point[0]);
      values = series[0]['values'].map(point => point[1]);
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
  <Select items={aggItems} bind:selectedValue={aggSelectedValue}></Select>
  <Select items={timeItems} bind:selectedValue={timeSelectedValue}></Select>
  <Select items={rollupItems} bind:selectedValue={rollupSelectedValue}></Select>
  <MyChart times={times} values={values}/>
</main>
