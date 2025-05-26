export interface Plant {
	nickname: string;
	scientific_name: string | null | undefined;
	last_watered: Date;
	check_rate: number;
	adoption_date: Date;
	location: string;
	next_check: Date;
}

