export interface Plant {
	id?: number;
	nickname: string;
	plant_type: string;
	scientific_name?: string;
	last_watered?: Date;
	check_rate: number;
	adoption_date: Date;
	location_name: string;
	next_check?: Date;
}

export interface apiResponse {
	success: boolean;
	message: string;
	error?: string;
}
