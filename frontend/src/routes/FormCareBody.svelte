<script module>
  export {careBody};
</script>

{#snippet careBody()}
  <section class="formbody">
    <p class="form-input">
      <label for="check-rate">How often does it need to be watered: </label>
      <input name="check-rate" type="number" min="1" max="31">
    </p>
    <p class="form-input">
      <label for="soil-dryness">How dry should the soil be before watering: </label>
      <input name="soil-dryness" type="range" step="any" min="0" max="4">
    </p>
  </section>
{/snippet}

<style>
  .formbody {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    top: 2em;
    bottom: 2rem;
  }
</style>