<script>

  import { get } from 'svelte/store';
  import Select from 'svelte-select';
  import { readable } from 'svelte/store';

  import { getOrElse } from './util.js';

  export let label;
  export let items;
  export let store;
  export let leading = false;

  // DONE: pickerITEMS needs to be reactive ($, not get()), pickerSTORE needs to NOT be

  function stupidStoreWrapper(store) {
    return {
      subscribe(newSubscriber) { return store.subscribe(newSubscriber) },
      set(newValue) { return store.set(newValue) }
    }
  }

  // make sure we support both Svelte stores and normal lists of options
  let safeItems = readable(items);
  if (typeof items.subscribe == 'function') {
    safeItems = stupidStoreWrapper(items);
  }

</script>

<style>
  * {
    font-size: 10pt;
    display: flex;
    white-space: nowrap;
  }
  .middle {
    /* nothing! */
  }
  .first {
    border-left: 1px solid #D8DBDF;
  }
  .last {
    border-right: 1px solid #D8DBDF;
  }
  .label {
    background-color: #f4f4f4;
    border-top: 1px solid #D8DBDF;
    border-bottom: 1px solid #D8DBDF;
    height: 36px;
    padding: 0 16px 0 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .picker {
    --borderRadius: 0px;
    --selectedItemPadding: 0px 0px 0px 0px;
    --itemPadding: 0px 16px 0px 16px;
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
  }
</style>

<div>
  <div class="label {(leading) ? "first" : "middle"}">
    <span>{label}</span>
  </div>
  <div class="picker">
    <Select
      isClearable={false}
      items={$safeItems}
      selectedValue={getOrElse($safeItems.filter(i => i.value == get(store))[0], {"label": get(store), "value": get(store)})}
      on:select={(item) => store.set(item.detail.value)}
    ></Select>
  </div>
</div>
