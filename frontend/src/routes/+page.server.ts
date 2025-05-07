import type { PageServerLoad } from './$types';
import type { Plant } from '$lib/types';

export const load: PageServerLoad = async (params) => {
	const fetched = await fetch('http://localhost:8000/existing');
	let returnedPlants: Array<Plant> = await fetched.json();
	return { returnedPlants };
};
