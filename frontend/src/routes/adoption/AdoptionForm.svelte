<script>
  import { namesBody } from "./FormNamesBody.svelte";
  import { careBody } from "./FormCareBody.svelte";
  import {slide} from "svelte/transition";
  import {isObjectType} from "eslint-plugin-svelte/lib/utils/ts-utils";

  let {show=$bindable(false)} = $props();
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
    <a href="#carousel__slide{slideNum}"
      class="carousel__navigation-button">
      Go to slide {slideNum}
    </a>
  </li>
{/snippet}

{#snippet carouselSlide(slideName)}
  <li id="carousel__slide{slideName}"
      class="carousel__slide">
    {#if slideName === 1}
      {@render namesBody()}
    {:else if slideName === 2}
      {@render careBody()}
    {/if}
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
  </li>
{/snippet}

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
  bind:this={dialog}
  onclose={() => (show = false)}>
  <form method="post" action="/">
    <section class="carousel" aria-label="Gallery">
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
    </section>
    <div id="form-buttons">
      <button type="button" onclick={() => dialog.close()}>close modal</button>
    </div>
  </form>
</dialog>

<style>
  @import "../../styles/carousel.css";
</style>
