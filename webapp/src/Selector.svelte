<script>

  import { get } from 'svelte/store';
  import Select from 'svelte-select';
  import { readable } from 'svelte/store';

  import { getOrElse } from './util.js';

  export let pickerLabel;
  export let pickerItems;
  export let pickerStore;
  export let pickerOrder = "middle";

  // DONE: pickerITEMS needs to be reactive ($, not get()), pickerSTORE needs to NOT be

  let safeItems = readable(pickerItems);

  function stupidStoreWrapper(store) {
    return {
      subscribe(newSubscriber) {
        return store.subscribe(newSubscriber)
      },
      set(newValue) {
        return store.set(newValue)
      }
    }
  }

  // make sure we support both Svelte stores and normal lists of options
  if (typeof pickerItems.subscribe == 'function') {
    safeItems = stupidStoreWrapper(pickerItems);
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
    border-left: 1px solid #d0d0d0;
  }
  .last {
    border-right: 1px solid #d0d0d0;
  }
  .label {
    background-color: #f2f2f2;
    border-top: 1px solid #d0d0d0;
    border-bottom: 1px solid #d0d0d0;
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
  <div class="label {pickerOrder}">
    <span>{pickerLabel}</span>
  </div>
  <div class="picker">
    <Select
      isClearable={false}
      items={$safeItems}
      selectedValue={getOrElse($safeItems.filter(i => i.value == get(pickerStore))[0], {"label": get(pickerStore), "value": get(pickerStore)})}
      on:select={(item) => pickerStore.set(item.detail.value)}
    ></Select>
  </div>
</div>
