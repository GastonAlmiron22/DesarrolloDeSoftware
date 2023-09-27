export class CarModelMock {
    constructor(
        public id: number,
        public name: string,
        public brand: string,
        public price: number,
        public year: number,
        public color: string,
        public hasSunroof: boolean,
        public isFourWheelDrive: boolean,
        public hasLowMiles: boolean,
        public hasPowerWindows: boolean,
        public hasNavigation: boolean,
        public hasHeatedSeats: boolean
    ){}
}

export const CarList = () =>{
    let carModels: CarModelMock[] = [
    new CarModelMock(1, 'Sedan', 'Toyota', 10000, 2014, 'Blue', false, false, true, true, false, false),
    new CarModelMock(2, 'SUV', 'Ford', 20000, 2015, 'Red', true, true, false, true, true, true),
    new CarModelMock(3, 'SUV', 'BMW', 30000, 2016, 'White', true, false, true, false, true, false),
    new CarModelMock(4, 'Sedan', 'Audi', 40000, 2017, 'Black', false, true, false, true, false, true),
    new CarModelMock(5, 'Wagon', 'Volvo', 50000, 2018, 'Gray', true, false, true, false, true, false),
    ];
    return carModels;
}