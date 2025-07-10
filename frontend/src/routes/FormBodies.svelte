<script module>
	export { namesBody, careBody };
</script>

{#snippet namesBody()}
	<section class="formbody">
		<h1>Identification Information</h1>
		<p class="form-input">
			<label for="nickname">Adoptive Name: </label>
			<input id="nickname" type="text" name="nickname" required />
		</p>
    <p class="form-input">
      <label for="adoption-date">Adoption Date: </label>
      <input id="adoption-date" type="date" name="adoption_date" />
    </p>
		<p class="form-input">
			<label for="plant-type">Plant Type: </label>
			<input id="plant-type" name="plant_type" />
		</p>
		<p class="form-input">
			<label for="scientific-name">Scientific Name: </label>
			<input id="scientific-name" name="scientific_name" />
		</p>
	</section>
{/snippet}

{#snippet careBody()}
	<section class="formbody">
		<h1>Care Details</h1>
		<p class="form-input">
			<label for="last-watered">When was it watered last: </label>
			<input id="last-watered" name="last_watered" type="date" />
		</p>
		<p class="form-input">
			<label for="check-rate">How often does it need to be watered: </label>
			<input id="check-rate" name="check_rate" type="number" min="1" max="31" required />
		</p>
		<p class="form-input">
			<label for="soil-dryness">How dry should the soil be before watering: </label>
			<input id="soil-dryness" name="soil_dryness" type="range" step="25" min="0" max="100" />
		</p>
	</section>
{/snippet}

<style>
	.formbody {
		display: flex;
		flex-direction: column;
		align-items: center;
		position: relative;
		top: 10%;
	}
</style>
