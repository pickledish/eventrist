import { writable, derived } from 'svelte/store';
import { getTimeRange } from './util.js';

// ----------------------------------------------------------------------------

export const rangeItems = [
  {value: getTimeRange(3600000),    label: 'Last 1 hour'},
  {value: getTimeRange(21600000),   label: 'Last 6 hours'},
  {value: getTimeRange(86400000),   label: 'Last 24 hours'},
  {value: getTimeRange(172800000),  label: 'Last 48 hours'},
  {value: getTimeRange(604800000),  label: 'Last 7 days'},
  {value: getTimeRange(2592000000), label: 'Last 30 days'},
];

export const selectedRange = writable(rangeItems[2]);

// ----------------------------------------------------------------------------

export const aggItems = [
  {value: "cnt", label: 'Count'},
  {value: "max", label: 'Max'},
  {value: "min", label: 'Min'},
  {value: "avg", label: 'Average'},
  {value: "sum", label: 'Sum'},
  {value: "p50", label: 'P.50'},
  {value: "p75", label: 'P.75'},
  {value: "p90", label: 'P.90'},
  {value: "p95", label: 'P.95'},
  {value: "p99", label: 'P.99'},
];

export const selectedAgg = writable(aggItems[0]);

// ----------------------------------------------------------------------------

export const rollupItems = [
  {value: "1m", label: '1 Minute'},
  {value: "1h", label: '1 Hour'},
  {value: "1d", label: '1 Day'},
];

export const selectedRollup = writable(rollupItems[1]);

// ----------------------------------------------------------------------------

export const chartTickWidth = derived(
  selectedRollup, $selectedRollup => {
    if ($selectedRollup.value === "1m") {
      return {unit: "minute", unitStepSize: 1}
    } else if ($selectedRollup.value === "1h") {
      return {unit: "hour", unitStepSize: 1}
    } else {
      return {unit: "day", unitStepSize: 1}
    }
  }
);