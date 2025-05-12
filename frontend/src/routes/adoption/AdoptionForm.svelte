<script>
  import {FormSelector} from "$lib/types.ts";
  import { formBodySnippet } from "./FormBodies.svelte";

  let {show} = $props();
  let dialog = $state(); // HTMLDialogElement
  let formState = $state(FormSelector.NAMES);

  $effect(() => {
    if (show) dialog.showModal();
    formState = FormSelector.NAMES;
  });
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
  bind:this={dialog}
  onclose={() => (show = false)}>

  {#snippet formHeader()}
    <h2>{formState}</h2>
  {/snippet/}

  <div id="plant-adoption-form">
    <h1>Plant Adoption Forms</h1>
    <form method="POST">
      <table class="form-table">
        <thead>
          <tr>{@render formHeader}</tr>
        </thead>
        <tbody>
        {@render }
        <tr>
          <td>
            <button>Bring Home</button>
          </td>
          <td>
            <button onclick={() => dialog.close()}>close modal</button>
          </td>
        </tr>
        </tbody>
      </table>
    </form>
    <!-- svelte-ignore a11y_autofocus -->
  </div>
</dialog>

<style>
  dialog {
    font-family: 'helvetica', sans-serif;
    background: #2f4f4f;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin: auto;
  }

  dialog::backdrop {
    background: rgba(0, 0, 0, 0.3);
  }

  dialog > div {
    padding: 1em;
  }

  dialog[open] {
    animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  @keyframes zoom {
    from {
      transform: scale(0.95);
    }
    to {
      transform: scale(1);
    }
  }

  dialog[open]::backdrop {
    animation: fade 0.2s ease-out;
  }

  @keyframes fade {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  button {
    display: block;
    font-family: 'helvetica', sans-serif;
    background: var(--color-mint-500);
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
</style>
