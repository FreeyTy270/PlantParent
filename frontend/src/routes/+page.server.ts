import type {Actions} from "@sveltejs/kit";
import type {Plant} from "$lib/types";


export const actions: Actions = {
  addPlant: async ({fetch, request}) => {
    const formData = await request.formData();
    let newPlant: Plant = {
      nickname: String(formData.get('nickname')),
      scientific_name: String(formData.get('scientific_name')),
      last_watered: Date(formData.get('last_watered')),
      check_rate: formData.get('check_rate'),
      adoption_date: formData.get('adoption_date'),
      location: formData.get('location'),
      next_check: formData.get('next_check'),
    }
    const response = await fetch('http://localhost:8000/add', {
      method: 'POST',
      body: newPlant
    });

    const message = response.json();
    return {message};
  }
}