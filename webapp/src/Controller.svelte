<script>

  import Select from 'svelte-select';

  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';

</script>

<style>
  .themed {
    --border: 2px solid grey;
    --borderRadius: 0px;
  }
  .themed {
    display: inline;
  }
</style>

<div class="themed">
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={aggItems} bind:selectedValue={$selectedAgg}></Select>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={rangeItems} bind:selectedValue={$selectedRange}></Select>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={rollupItems} bind:selectedValue={$selectedRollup}></Select>
  </div>
</div>
