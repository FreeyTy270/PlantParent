<script module>
  export { namesFormBody }
</script>
<script>
  import AdoptionForm from "./AdoptionForm.svelte";
</script>

<table id="NameBody">
  <tbody>
  {#snippet namesFormBody()}
    <tr>
      <td>
        <label for="nickname">Adoptive Name: </label>
      </td>
      <td>
        <input id="nickname" type="text">
      </td>
    </tr>
    <tr>
      <td>
        <label for="scientific_name">Scientific Name: </label>
      </td>
      <td>
        <input id="scientific_name" type="text">
      </td>
    </tr>
  {/snippet}
  </tbody>
</table>

<table id="CareBody">
  <tbody>
  {#snippet careFormBody()}
    <tr>
      <td>
        <label for="nickname">Adoptive Name: </label>
      </td>
      <td>
        <input id="nickname" type="text">
      </td>
    </tr>
    <tr>
      <td>
        <label for="scientific_name">Scientific Name: </label>
      </td>
      <td>
        <input id="scientific_name" type="text">
      </td>
    </tr>
  {/snippet}
  </tbody>
</table>
