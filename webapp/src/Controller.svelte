<script>

  import Select from 'svelte-select';

  import {nameItems, selectedName} from './Stores.js';
  import {whereItems, selectedWhere} from './Stores.js';
  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';
  import {groupByItems, selectedGroupBy} from './Stores.js';

</script>

<style>
  .themed {
    --borderRadius: 0px;
    --itemPadding: 0px;
    --height: 40px;
    --listMaxHeight: 300px;
    width: 100%;
  }
  .themed {
    display: flex;
    padding-bottom: 12px;
  }
  .nonselect {
    background-color: #f2f2f2;
    border-top: 1px solid #d0d0d0;
    border-bottom: 1px solid #d0d0d0;
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

<div class="themed" style="justify-content: flex-end;">
  <div class="nonselect" style="border-left: 1px solid #d0d0d0;">
    <span>Time Range</span>
  </div>
  <div style="width: 180px; display: inline-block;">
      <Select isClearable={false} items={rangeItems} bind:selectedValue={$selectedRange}></Select>
  </div>
</div>

<div class="themed">
  <div class="nonselect" style="border-left: 1px solid #d0d0d0;">
    <span>Query</span>
  </div>
  <div style="width: 180px; display: inline-block;">
    <Select isClearable={false} bind:items={$nameItems} bind:selectedValue={$selectedName}></Select>
  </div>
  <div class="nonselect">
    <span>where</span>
  </div>
  <div style="width: 180px; display: inline-block;">
    <Select isClearable={false} isCreatable={true} items={whereItems} bind:selectedValue={$selectedWhere}></Select>
  </div>
  <div class="nonselect">
    <span>take the</span>
  </div>
  <div style="width: 180px; display: inline-block;">
    <Select isClearable={false} items={aggItems} bind:selectedValue={$selectedAgg}></Select>
  </div>
  <div class="nonselect">
    <span>of each</span>
  </div>
  <div style="width: 180px; display: inline-block;">
    <Select isClearable={false} items={rollupItems} bind:selectedValue={$selectedRollup}></Select>
  </div>
  <div class="nonselect">
    <span>group by</span>
  </div>
  <div style="width: 180px; display: inline-block;">
    <Select isClearable={false} items={$groupByItems} bind:selectedValue={$selectedGroupBy}></Select>
  </div>
</div>
