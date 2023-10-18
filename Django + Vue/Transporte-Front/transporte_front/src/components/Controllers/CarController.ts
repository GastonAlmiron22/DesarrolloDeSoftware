import axios from "axios";

export class CarController {
    getCars(car: any) {
        axios.get('http://localhost:3000/cars/').then((response) => {
            return response.data;
        });
    }
}
