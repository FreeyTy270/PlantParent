import type { PageLoad } from './$types';
import type { Plant } from '$lib/types';
import {redirect} from "@sveltejs/kit";

export const load: PageLoad = async ({ fetch }) => {
	let returnedPlants: Array<Plant> = await fetch('http://localhost:8000/existing').then((value) =>
		value.json()
	);

	// if (returnedPlants.length === 0)
	// 	redirect(303, "/onboarding")

	return { returnedPlants };
};
