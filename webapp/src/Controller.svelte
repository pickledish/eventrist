<script>

  import Select from 'svelte-select';

  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';

</script>

<style>
  .themed {
    --borderRadius: 0px;
    --itemPadding: 0px;
    --height: 40px;
    width: 100%;
  }
  .themed {
    display: flex;
    align-items: left;
  }
  .nonselect {
    background-color: #f2f2f2;
    border: 1px solid #d0d0d0;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: left;
    padding: 0 16px 0 16px;
    vertical-align: top;
  }
  span {
    white-space: nowrap;
  }

</style>

<div>
  <div style="width: 200px; display: inline-block; float: right">
    <span>
      Time Range:
      <Select isClearable={false} items={rangeItems} bind:selectedValue={$selectedRange}></Select>
    </span>
  </div>
</div>

<div class="themed">
  <div class="nonselect">
    <span>Query</span>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={["response_time"]}></Select>
  </div>
  <div class="nonselect">
    <span>where</span>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={["(everything)"]}></Select>
  </div>
  <div class="nonselect">
    <span>take the</span>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={aggItems} bind:selectedValue={$selectedAgg}></Select>
  </div>
  <div class="nonselect">
    <span>of each</span>
  </div>
  <div style="width: 200px; display: inline-block;">
    <Select isClearable={false} items={rollupItems} bind:selectedValue={$selectedRollup}></Select>
  </div>
</div>
