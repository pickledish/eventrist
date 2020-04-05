<script>

  import {nameItems, selectedName} from './Stores.js';
  import {whereItems, selectedWhere} from './Stores.js';
  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';
  import {groupByItems, selectedGroupBy} from './Stores.js';

  import Selector from './Selector.svelte'

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

  <div style="width: 100%; display: flex; justify-content: flex-end;">
    <Selector label={"Graph by"} items={groupByItems} store={selectedGroupBy} leading={true} multi={true}/>
  </div>

</div>
