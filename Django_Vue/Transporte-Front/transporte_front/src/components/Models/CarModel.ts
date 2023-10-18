export class CarModelMock {
    constructor(
        public id: number,
        public model: string,
        public brand: string,
        public price: number,
        public year: number,
        public color: string,
        public hasSunroof: boolean,
        public isFourWheelDrive: boolean,
        public hasLowMiles: boolean,
        public hasPowerWindows: boolean,
        public hasNavigation: boolean,
        public hasHeatedSeats: boolean,
        public licencePlate: string,
        public value: number,
    ){}
}