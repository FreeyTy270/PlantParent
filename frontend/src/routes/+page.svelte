<script lang="ts">
  // import { onMount } from 'svelte';
  import type {PageProps} from './$types';
  import AdoptionForm from "./AdoptionForm.svelte";

  const {data}: PageProps = $props();
  const {returnedPlants} = data
  let showAdoptionForm = $state(false)
  let adopt = async () => {
    console.log('adopted New Plant!!')
    showAdoptionForm = !showAdoptionForm
  }

</script>

<main class="container">
  <h1 class="Page-Title">Your Plant Parent Dashboard</h1>
  <div class="dashboard-grid">
    {#each returnedPlants as plant}
      <div class="card">
        <h2 class="card-title">{plant.nickname}</h2>
        {#if plant.scientific_name}
          <p class="scientific-name">Scientific Name: {plant.scientific_name}</p>
        {:else if plant.scientific_name === null}
          <p class="scientific-name">Scientific Name: Unknown</p>
        {/if}
        <p class="check-rate">Check soil every {plant.check_rate} days</p>
        <p class="check-rate">Next check date: {plant.next_check}</p>
      </div>
    {/each}
  </div>
  <div class="container">
    <button class="User-Interactive" onclick={adopt}>Adopt a Plant!</button>
  </div>

  <AdoptionForm bind:showAdoptionForm>
  </AdoptionForm>
</main>

<style>
  @import './styles.css';
</style>
