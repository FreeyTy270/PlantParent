import type { Actions } from '@sveltejs/kit';
import type { apiResponse, Plant } from '$lib/types';

export const actions: Actions = {
	addPlant: async ({ fetch, request }) => {
		const formData: FormData = await request.formData();

		let newPlant: Plant = {
			nickname: String(formData.get('nickname')),
			plant_type: String(formData.get('plant_type')),
			scientific_name: String(formData.get('scientific_name')),
			last_watered: new Date(String(formData.get('last_watered'))),
			check_rate: Number(formData.get('check_rate')),
			adoption_date: new Date(String(formData.get('adoption_date'))),
			location_name: String(formData.get('location')),
			next_check: new Date(String(formData.get('next_check')))
		};

		const response: Response = await fetch('http://localhost:8000/add', {
			method: 'POST',
			body: JSON.stringify(newPlant),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		console.log(response);

		return (await response.json()) as Promise<apiResponse>;
	}
};
