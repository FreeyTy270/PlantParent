import type {PageLoad} from './$types';
import type {Plant} from '$lib/types';

export const load: PageLoad = async () => {

  let returnedPlants: Array<Plant> = await fetch('http://localhost:8000/existing').then((value) => value.json());
  return {returnedPlants};
};
