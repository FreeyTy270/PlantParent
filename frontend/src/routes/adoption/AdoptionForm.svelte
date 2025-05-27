<script>
  import {namesBody} from "./FormNamesBody.svelte";
  import {careBody} from "./FormCareBody.svelte";
  import {slide} from "svelte/transition";

  let {show = $bindable(false)} = $props();
  let dialog = $state(); // HTMLDialogElement
  let formState = $state("NAMES");

  $effect(() => {
    if (show) dialog.showModal();
    formState = "NAMES";
  });
</script>

{#snippet formHeader()}
  <th>
    <h2>{formState}</h2>
  </th>
{/snippet}

{#snippet carouselNavButtons(slideNum)}
  <li class="carousel__navigation-item">
    <span class="carousel__navigation-button">
      <a href="#carousel__slide{slideNum}">
        Go to slide {slideNum}
      </a>
    </span>
  </li>
{/snippet}

{#snippet carouselSlide(slideName)}
  <li id="carousel__slide{slideName}"
      class="carousel__slide">
    <div class="carousel__snapper">
      {#if slideName === 1}
        <a href="#carousel__slide4"
           class="carousel__prev">Go to last slide</a>
      {:else}
        <a href="#carousel__slide{slideName - 1}"
           class="carousel__prev">Go to previous slide</a>
      {/if}
      {#if slideName === 4}
        <a href="#carousel__slide1"
           class="carousel__next">Go to first slide</a>
      {:else}
        <a href="#carousel__slide{slideName + 1}"
           class="carousel__next">Go to next slide</a>
      {/if}
    </div>
    {#if slideName === 1}
      {@render namesBody()}
    {:else if slideName === 2}
      {@render careBody()}
    {/if}
  </li>
{/snippet}

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
  class="carousel"
  bind:this={dialog}
  onclose={() => (show = false)}>
  <form id="adoptionForm" aria-label="Gallery" method="POST" action="http://localhost:8000/add">
    <ol class="carousel__viewport">
      {@render carouselSlide(1)}
      {@render carouselSlide(2)}
      {@render carouselSlide(3)}
      {@render carouselSlide(4)}
    </ol>
    <aside class="carousel__navigation">
      <ol class="carousel__navigation-list">
        {@render carouselNavButtons(1)}
        {@render carouselNavButtons(2)}
        {@render carouselNavButtons(3)}
        {@render carouselNavButtons(4)}
      </ol>
    </aside>
  </form>
  <div id="form-buttons">
    <button type="button" onclick={() => dialog.close()}>close modal</button>
    <button form="adoptionForm" type="submit">Submit Papers</button>
  </div>
</dialog>

<style>
  @import "../../styles/carousel.css";
</style>
