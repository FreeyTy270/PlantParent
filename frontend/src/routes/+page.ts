import type {PageLoad} from './$types';

export const load: PageLoad = async (params) => {
    const fetched = await fetch('http://localhost:8000/existing');
    return await fetched.json();
};