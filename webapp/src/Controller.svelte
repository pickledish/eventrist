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
    font-size: 10pt;
    width: 100%;
    display: flex;
    padding-bottom: 12px;
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
