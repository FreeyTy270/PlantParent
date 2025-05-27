<script module>
  export {namesBody};
</script>

{#snippet namesBody()}
  <section class="formbody">
    <p class="form-input">
      <label for="nickname">Adoptive Name: </label>
      <input id="nickname" type="text" name="nickname">
    </p>
    <p class="form-input">
      <label for="plant-type">Plant Type: </label>
      <input id="plant-type" name="plant_type">
    </p>
    <p class="form-input">
      <label for="scientific-name">Scientific Name: </label>
      <input id="scientific-name" name="scientific_name">
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
    top: 50%;
  }
</style>


