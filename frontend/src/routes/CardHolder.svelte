<script lang="ts">
	import type { PageProps } from './$types';
	import type { apiResponse, Plant } from '$lib/types';
	import { hydrate } from 'svelte';
	import { invalidate } from '$app/navigation';
	const { data }: PageProps = $props();
	const { returnedPlants } = data;

	let dashboardPlants: Array<Plant> | null = $state(null);

	let bury = async (event: Event, the_fallen: Plant) => {
    event.preventDefault();
		console.log(`Laying to rest: ${the_fallen.nickname}`);
		dashboardPlants = returnedPlants.filter((dashPlant) => dashPlant.id != the_fallen.id);
		const response: Response = await fetch(
			`http://localhost:8000/bury?fallen_id=${the_fallen.id}`,
			{
				method: 'DELETE'
			}
		);
		console.log(response);
		if (!response.ok) throw new Error(response.statusText);
		console.log(`Could not delete ${the_fallen.nickname} from the database please try again later`);
		await invalidate('dashboardPlants');
		return (await response.json()) as Promise<apiResponse>;
	};
</script>

{#snippet dashCard(plant: Plant)}
	<div class="card">
		<h2 class="card-title">{plant.nickname}</h2>
		{#if plant.scientific_name}
			<p class="scientific-name">Scientific Name: {plant.scientific_name}</p>
		{:else if plant.scientific_name === null}
			<p class="scientific-name">Scientific Name: Unknown</p>
		{/if}
		<p class="check-rate">Check soil every {plant.check_rate} days</p>
		<p class="check-rate">Next check date: {plant.next_check}</p>
		<section>
			<button class="User-Interactive" type="button" onclick={(event) => bury(event, plant)}
				>Release</button
			>
		</section>
	</div>
{/snippet}

<div class="dashboard-grid">
	{#if returnedPlants.length === 0}
		<p class="banner-message">No plants found!</p>
	{:else}
		{#each data.returnedPlants as plant}
			{@render dashCard(plant)}
		{/each}
	{/if}
</div>

<style>
	@import '../styles/styles.css';
</style>
