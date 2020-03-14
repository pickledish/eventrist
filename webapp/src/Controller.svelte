<script>

  import Select from 'svelte-select';

  import {nameItems, selectedName} from './Stores.js';
  import {whereItems, selectedWhere} from './Stores.js';
  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';
  import {groupByItems, selectedGroupBy} from './Stores.js';

  import { getOrElse, flatten } from './util.js';

  function handleMulti(newVal, storeToUpdate) {
    let detail = getOrElse(newVal.detail, [])
    let flat = flatten(detail.map(elem => elem.value))
    console.log(flat)
    $selectedGroupBy = flat
    console.log($selectedGroupBy)
  }

</script>

<style>
  .themed {
    --borderRadius: 0px;
    --itemPadding: 0px 0px 0px 16px;
    --height: 36px;
    --listMaxHeight: 300px;
    --inputFontSize: 10pt;
    --multiItemBorderRadius: 2px;
    --multiItemHeight: 28px;
    --multiClearTop: 6px;
    --multiClearBG: rgba(0,0,0,0);
    --multiClearFill: rgba(64,64,64,255);
    --multiClearHoverBG: rgba(0,0,0,0);
    --multiClearHoverFill: rgba(0,0,0,255);
    --multiItemPadding: 0px 8px;
    font-size: 10pt;
    width: 100%;
    display: flex;
    padding-bottom: 12px;
    text-align: left;
  }
  .nonselect {
    background-color: #f2f2f2;
    border-top: 1px solid #d0d0d0;
    border-bottom: 1px solid #d0d0d0;
    height: 36px;
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
  <div style="width: 150px; display: inline-block;">
      <Select isClearable={false} items={rangeItems} bind:selectedValue={$selectedRange}></Select>
  </div>
</div>

<div class="themed">
  <div class="nonselect" style="border-left: 1px solid #d0d0d0;">
    <span>Query</span>
  </div>
  <div style="min-width: 180px;">
    <Select isClearable={false} bind:items={$nameItems} bind:selectedValue={$selectedName}></Select>
  </div>
  <div class="nonselect">
    <span>where</span>
  </div>
  <div style="min-width: 180px;">
    <Select isClearable={false} isCreatable={true} items={whereItems} bind:selectedValue={$selectedWhere}></Select>
  </div>
  <div class="nonselect">
    <span>take the</span>
  </div>
  <div style="min-width: 150px;">
    <Select isClearable={false} items={aggItems} bind:selectedValue={$selectedAgg}></Select>
  </div>
  <div class="nonselect">
    <span>of each</span>
  </div>
  <div style="min-width: 120px;">
    <Select isClearable={false} items={rollupItems} bind:selectedValue={$selectedRollup}></Select>
  </div>
  <div style="width: 100%; display: flex; justify-content: flex-end;">
    <div class="nonselect" style="border-left: 1px solid #d0d0d0;">
      <span>Graph by</span>
    </div>
    <div style="min-width: 150px;">
      <Select
        isClearable={false}
        items={$groupByItems}
        isMulti={true}
        placeholder={"(everything)"}
        on:select={(selectedVal) => handleMulti(selectedVal, $selectedGroupBy)}
      ></Select>
    </div>
  </div>
</div>
