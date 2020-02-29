import { writable, derived } from 'svelte/store';
import { getTimeRange } from './util.js';

// ----------------------------------------------------------------------------

export const nameItems = [
  {value: "response_time", label: 'response_time'},
  {value: "transaction_amount", label: 'transaction_amount'},
];

export const selectedName = writable(nameItems[0]);

// ----------------------------------------------------------------------------

export const whereItems = [
  {value: "", label: '(everything)'},
  ];

export const selectedWhere = writable(whereItems[0]);

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

export const selectedRange = writable(rangeItems[2]);

// ----------------------------------------------------------------------------

export const aggItems = [
  {value: "cnt", label: 'Count'},
  {value: "max", label: 'Maximum'},
  {value: "min", label: 'Minimum'},
  {value: "avg", label: 'Average'},
  {value: "sum", label: 'Sum'},
  {value: "p50", label: 'Median'},
  {value: "p75", label: '75th Percentile'},
  {value: "p90", label: '90th Percentile'},
  {value: "p95", label: '95th Percentile'},
  {value: "p99", label: '99th Percentile'},
];

export const selectedAgg = writable(aggItems[0]);

// ----------------------------------------------------------------------------

export const rollupItems = [
  {value: "1m", label: '1 Minute'},
  {value: "1h", label: '1 Hour'},
  {value: "6h", label: '6 Hours'},
  {value: "1d", label: '1 Day'},
  {value: "1w", label: '1 Week'},
  {value: "30d", label: '1 Month'},
];

export const selectedRollup = writable(rollupItems[1]);

// ----------------------------------------------------------------------------

export const groupByItems = [
  {value: [], label: '(everything)'},
  {value: ["family"], label: 'family'},
  {value: ["app_name"], label: 'app_name'},
  {value: ["trace_id"], label: 'trace_id'},
  {value: ["Category"], label: 'Category'},
];

export const selectedGroupBy = writable(groupByItems[0]);

// ----------------------------------------------------------------------------

export const chartTickWidth = derived(
  selectedRollup, $selectedRollup => {
    if ($selectedRollup.value === "1m") {
      return {unit: "minute", unitStepSize: 1}
    } else if ($selectedRollup.value === "1h") {
      return {unit: "hour", unitStepSize: 1}
    } else if ($selectedRollup.value === "6h") {
      return {unit: "hour", unitStepSize: 6}
    } else if ($selectedRollup.value === "1w") {
      return {unit: "week", unitStepSize: 1}
    } else if ($selectedRollup.value === "30d") {
      return {unit: "month", unitStepSize: 1}
    } else {
      return {unit: "day", unitStepSize: 1}
    }
  }
);
