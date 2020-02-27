<script>

  import Select from 'svelte-select';

  import {rangeItems, selectedRange} from './Stores.js';
  import {aggItems, selectedAgg} from './Stores.js';
  import {rollupItems, selectedRollup} from './Stores.js';

</script>

<Select items={aggItems} bind:selectedValue={$selectedAgg}></Select>
<Select items={rangeItems} bind:selectedValue={$selectedRange}></Select>
<Select items={rollupItems} bind:selectedValue={$selectedRollup}></Select>
