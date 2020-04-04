<script>

  import Select from 'svelte-select';

  import { get } from 'svelte/store';

  import {nameItems, selectedName} from './Stores.js';
  import {whereItems, selectedWhere} from './Stores.js';
  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';
  import {groupByItems, selectedGroupBy} from './Stores.js';

  import Selector from './Selector.svelte'

  import { getOrElse, flatten } from './util.js';

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
  <Selector label={"Time Range"} items={rangeItems} store={selectedRange} leading={true}/>
</div>

<div class="themed">

  <Selector label={"Query"} items={nameItems} store={selectedName} leading={true}/>
  <Selector label={"where"} items={whereItems} store={selectedWhere}/>
  <Selector label={"take the"} items={aggItems} store={selectedAgg}/>
  <Selector label={"of each"} items={rollupItems} store={selectedRollup}/>
  <!--<Selector label={"graphy by"} items={groupByItems} store={selectedGroupBy} leading={true} multi={true}/>-->

  <!-- UGLLYYYYY please convert me to a Selector, too! Hard because it's a multi -->
  <div style="width: 100%; display: flex; justify-content: flex-end;">
    <div class="nonselect" style="border-left: 1px solid #d0d0d0;">
      <span>Graph by</span>
    </div>
    <div>
      <!-- BUG: trying to selectedGroupBy in the filter statement causes duplicate calls, no work -->
      <!-- I guess changes to $selectedGroupBy cause this to be recomputed? -->
      <!-- Fix by getting an immutable copy from the store, no subscribing: https://svelte.dev/docs#get -->
      <Select
        isClearable={false}
        items={$groupByItems}
        isMulti={true}
        placeholder={"(everything)"}
        selectedValue={getOrElse($groupByItems, []).filter(i => get(selectedGroupBy).includes(i.value))}
        on:select={(selected) => $selectedGroupBy = flatten(getOrElse(selected.detail, []).map(elem => elem.value))}
      ></Select>
    </div>
  </div>
</div>
