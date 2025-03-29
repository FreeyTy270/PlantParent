<script lang="ts">
    import {onMount} from 'svelte';
    import type {Plant} from "$lib/types";

    let currentPlants: Array<Plant>;

    onMount(() => {
        // Initial data fetch
        async function fetch_initial() {
            const fetched = await fetch('http://localhost:8000/existing');
            currentPlants = await fetched.json();
        }

        fetch_initial()

        return currentPlants
    });
</script>


<main class="container">
    <h1>Your Plant Parent Dashboard</h1>
    <div>
        { currentPlants }
    </div>

</main>