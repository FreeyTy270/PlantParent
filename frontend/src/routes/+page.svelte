<script lang="ts">
  import {onMount} from 'svelte';
  import type {Plant} from "$lib/types";

  let currentPlants: Array<Plant>;

  onMount(async () => {
    const fetched = await fetch('http://localhost:8000/existing');
    currentPlants = await fetched.json();
    if (currentPlants) {
      currentPlants.forEach((plant) => {
          console.log("Plant Right Now:" + plant)
      })
    }
  });
</script>


<main class="container">
  <h1 class="Page-Title">Your Plant Parent Dashboard</h1>
  <div class="dashboard-grid">
    {#each currentPlants as plant}
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
</main>


<style>
  .Page-Title {
    font-size: 2rem;
    font-weight: bold;
    color: aliceblue;
    margin-bottom: 1.5rem;
    font-style: oblique;
    text-decoration: underline;
    text-underline-offset: 0.25rem;
    text-decoration-thickness: 0.125rem;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }

  .card {
    font-family: 'helvetica', sans-serif;
    background: #2F4F4F;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }

  .card-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: aliceblue;
    text-decoration: underline;
    text-underline-offset: 0.25rem;
    text-decoration-thickness: 0.125rem;
  }

  .scientific-name {
    font-size: 1rem;
    color: aliceblue;
    font-style: italic;
  }

  .check-rate {
    font-size: 1rem;
    color: aliceblue;


  }
</style>
