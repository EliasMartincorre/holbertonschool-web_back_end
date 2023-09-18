    export class HolbertonClass {
    constructor(year, location) {
        this._year = year;
        this._location = location;
    }
    
    get year() {
        return this._year;
    }
    set year(value) {
        this._year = value
    }
    
    get location() {
        return this._location;
    }
    
    set location(value) {
        this._location = value
    }
}


const hclass2019 = new HolbertonClass(2019, 'San Francisco');
const hclass2020 = new HolbertonClass(2020, 'San Francisco');

    export  class StudentHolberton extends HolbertonClass {
        constructor(firstName, lastName, holbertonClass, year, location) {
        super(holbertonClass)
        this._year = holbertonClass.year;
        this._location = holbertonClass.location;
        this._firstName = firstName;
        this._lastName = lastName;
        }
        
        get fullName() {
            return `${this._firstName} ${this._lastName}`
        }
        
        set fullName(fullName) {
            const [firstName, lastName] = fullName.split(" ");
            this._firstName = firstName;
            this._lastName = lastName;
        }
        get holbertonClass() {
            return this._holbertonClass;
        }
        
        get fullStudentDescription() {
            return `${this._firstName} ${this._lastName} - ${this._year} - ${this._location}`;
        }
        set fullStudentDescription(fullName) {
            const [firstName, lastName] = fullName.split(" ");
            this._firstName = firstName;
            this._lastName = lastName;
            
            
        }
    }
    const student1 = new StudentHolberton('Guillaume', 'Salva', hclass2020);
    const student2 = new StudentHolberton('John', 'Doe', hclass2020);
    const student3 = new StudentHolberton('Albert', 'Clinton', hclass2019);
    const student4 = new StudentHolberton('Donald', 'Bush', hclass2019);
    const student5 = new StudentHolberton('Jason', 'Sandler', hclass2019);
    
    const listOfStudents = [student1, student2, student3, student4, student5]; 
    export default listOfStudents;