<script lang="ts">
    import {onMount} from 'svelte';
    import type {Plant} from "$lib/types";

    let currentPlants = $state<Array<Plant> | null>(null);

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
    <h1>Your Plant Parent Dashboard</h1>
    {@debug currentPlants}
    <div class="dashboard-grid">
        {#each currentPlants as plant}
            <div class="card">
                <h2>{plant.nickname}</h2>
                {#if plant.scientific_name}
                    <p class="scientific-name">{plant.scientific_name}</p>
                {/if}
                <p class="check-rate">{plant.check_rate}</p>
            </div>
        {/each}
    </div>
</main>
