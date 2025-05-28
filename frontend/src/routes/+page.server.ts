import type {Actions} from "@sveltejs/kit";
import {type apiResponse, Plant} from "$lib/types";


export const actions: Actions = {
  addPlant: async ({fetch, request}) => {
    const formData: FormData = await request.formData();

    let lastWatered: Date = new Date(String(formData.get('last_watered')));
    let adoptionDate: Date = new Date(String(formData.get('adoption_date')));
    let nextCheck: Date = new Date(String(formData.get('next_check')));
    let newName: string = String(formData.get('nickname'));

    // let newPlant: Plant = new Plant(
    //   String(formData.get('plant_name')),
    //   String(formData.get('scientific_name')),
    //   lastWatered,
    //   Number(formData.get('check_rate')),
    //   adoptionDate,
    //   String(formData.get('location')),
    //   nextCheck,
    // )
    const response: Response = await fetch('http://localhost:8000/add', {
      method: 'POST',
      body: JSON.stringify({nickname: newName}),
      headers: {
        'Content-Type': 'application/json',
      }
    });

    console.log(response);

    return await response.json() as Promise<apiResponse>;
  }
}