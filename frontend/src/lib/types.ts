interface __plantInterface__ {
  nickname: string;
  scientific_name: string | null | undefined;
  last_watered: Date;
  check_rate: number;
  adoption_date: Date;
  location: string;
  next_check: Date;
}

export class Plant {
  nickname: string;
  scientific_name: string | null | undefined;
  last_watered: Date;
  check_rate: number;
  adoption_date: Date;
  location: string;
  next_check: Date;

  constructor(nickname: string, scientific_name: string | null | undefined = null, last_watered: Date, check_rate: number, adoption_date: Date, location: string, next_check: Date) {
    this.nickname = nickname;
    this.scientific_name = scientific_name;
    this.last_watered = last_watered;
    this.check_rate = check_rate;
    this.adoption_date = adoption_date;
    this.location = location;
    this.next_check = next_check;
  }
}

export interface apiResponse {
  success: boolean;
  message: string;
  error?: string;
}
