<script>
  let {showAdoptionForm = $bindable()} = $props();

  let dialog = $state(); // HTMLDialogElement

  $effect(() => {
    if (showAdoptionForm) dialog.showModal();
  });
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
  bind:this={dialog}
  onclose={() => (showAdoptionForm = false)}
  onclick={(e) => { if (e.target === dialog) dialog.close(); }}
>
  <div>
    <h2 class="card-title">Plant Adoption Form</h2>

    <form method="POST">
      <table class="form-table">
        <tbody>
        <tr>
          <td>
            <label for="nickname-field" class="check-rate">
              Adoptive Name
              <input name="nickname" type="text" required/>
            </label>
          </td>
        </tr>
        <tr class="sciname-field">
          <td>
            <label for="sciname-field" class="scientific-name">
              Scientific Name
              <input name="scientific_name" type="text"/>
            </label>
          </td>
        </tr>
        <tr>
          <td>
            <label class="check-rate">
              Last Watering Date
              <input name="last_watered" type="date" min={new Date().toLocaleDateString('fr-ca')}/>
            </label>
          </td>
        </tr>
        <tr>
          <td>
            <label class="check-rate">
              How often should the soil be checked?
              <input name="check_rate" type="number" min=1 max=31/>
            </label>
          </td>
        </tr>
        <tr>
          <td>
            <label class="check-rate">
              Plant's location in the house
              <input name="location" type="text" required/>
            </label>
          </td>
        </tr>
        <tr>
          <td>
            <button>
              Bring Home
              <input type="submit">
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </form>
    <!-- svelte-ignore a11y_autofocus -->
    <button autofocus onclick={() => dialog.close()}>close modal</button>
  </div>
</dialog>

<style>
  dialog {
    font-family: 'helvetica', sans-serif;
    background: #2f4f4f;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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
