<script module>
  export { careBody };
</script>

{#snippet careBody()}
  <section class="formbody">
    <p>
      <label for="check-rate">How often does it need to be watered: </label>
      <input id="check-rate" type="number" min="1" max="31">
    </p>
    <p>
      <label for="soil-dryness">How dry should the soil be before watering: </label>
      <input id="soil-dryness" type="range" step="any">
    </p>
  </section>
{/snippet}