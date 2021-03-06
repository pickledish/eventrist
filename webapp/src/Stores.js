import { writable, derived } from 'svelte/store';
import { getTimeRange, getOrElse, flatten, getQueryParam, setQueryParam } from './util.js';

// ----------------------------------------------------------------------------

// Can be one of BAR, LINE, RAW
export const currentView = writable("BAR")

// ----------------------------------------------------------------------------

export const nameItems = writable([
  {value: "*", label: '(everything)'},
]);

export const selectedName = queryParamStore("event", "*")

// ----------------------------------------------------------------------------

export const whereItems = [
  {value: "", label: '(everything)'},
];

export const selectedWhere = writable(whereItems[0].value);

// ----------------------------------------------------------------------------

export const rangeItems = [
  {value: getTimeRange(3600000),     label: 'Last 1 hour'},
  {value: getTimeRange(21600000),    label: 'Last 6 hours'},
  {value: getTimeRange(86400000),    label: 'Last 24 hours'},
  {value: getTimeRange(172800000),   label: 'Last 48 hours'},
  {value: getTimeRange(604800000),   label: 'Last 7 days'},
  {value: getTimeRange(2592000000),  label: 'Last 30 days'},
  {value: getTimeRange(7776000000),  label: 'Last 3 months'},
  {value: getTimeRange(15552000000), label: 'Last 6 months'},
];

export const selectedRange = queryParamStore("timerange", rangeItems[5].value);

// ----------------------------------------------------------------------------

export const aggItems = [
  {value: "cnt", label: 'Count'},
  {value: "sum", label: 'Sum'},
  {value: "max", label: 'Maximum'},
  {value: "min", label: 'Minimum'},
  {value: "avg", label: 'Average'},
  {value: "p50", label: 'Median'},
  {value: "p75", label: '75th Percentile'},
  {value: "p90", label: '90th Percentile'},
  {value: "p95", label: '95th Percentile'},
  {value: "p99", label: '99th Percentile'},
];

export const selectedAgg = queryParamStore("aggr", "cnt")

// ----------------------------------------------------------------------------

export const rollupItems = [
  {value: "1m", label: '1 Minute'},
  {value: "1h", label: '1 Hour'},
  {value: "6h", label: '6 Hours'},
  {value: "1d", label: '1 Day'},
  {value: "1w", label: '1 Week'},
  {value: "30d", label: '1 Month'},
];

export const selectedRollup = queryParamStore("rollup", "1d")

// ----------------------------------------------------------------------------

function makeShit(tagval) {
  return {"value": tagval, "label": tagval}
}

export const groupByItems = derived(
  selectedName,
  async ($selectedName, set) => {
    let response = await fetch("http://127.0.0.1:8000/stream/abcd/tagkeys", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({"event_name": $selectedName})
    })
    let json = await response.json()
    let series = getOrElse(json.series, [{"values": []}])
    set(flatten(series[0]['values']).map(tagval => makeShit(tagval)))
  }
);

export const selectedGroupBy = queryParamStore("groupby", []);

// ----------------------------------------------------------------------------

/*
 * Custom state store which is backed by a normal Svelte `writable` store.
 * Ensures that all updates are persisted to query param with name `paramName`
 * so that when you refresh the page, the value is intact.
 *
 * Makes sharing of dashboards via URL possible, wahoo
 */
function queryParamStore(paramName, defaultValue) {

  let currentValue = getQueryParam(paramName, defaultValue)
  let innerStore = writable(currentValue);

  return {
    subscribe(newSubscriber) {
      return innerStore.subscribe(newSubscriber)
    },
    set(newValue) {
      setQueryParam(paramName, newValue)
      return innerStore.set(newValue)
    }
  }
}
