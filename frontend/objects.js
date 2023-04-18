// Задание 1.
// Написать, функцию, которая принимает в качестве аргумента объект и
// выводит в консоль все ключи и значения только собственных свойств.
// Данная функция не должна возвращать значение.
//
// function getArgs (obj){
//     for (let key in obj) {
//         if (obj.hasOwnProperty(key)) {
//             console.log(key+':'+obj[key]);
//         }
//     }
// }
// someFamily = {
//     lastname : "Ivanov"
// }
// someOne = Object.create(someFamily);
// someOne.firstname = 'Ivan'
// getArgs(someOne)

//     Задание 2.
// Написать функцию, которая принимает в качестве аргументов строку
// и объект, а затем проверяет есть ли у переданного объекта
// свойство с данным именем. Функция должна возвращать true или false.
// function checkProp(prop, obj){
//     if (typeof prop == "string" | typeof obj == 'object'){
//         if (obj.hasOwnProperty(prop)) {
//             console.log('true')
//             return true
//         } else {
//             console.log('false')
//             return false
//             }
//     } else {
//         console.log('неверные исх данные')
//     }
// }
// someFamily = {
//     lastname : "Ivanov"
// }
// checkProp('lastname', someFamily)
// checkProp('firstname', someFamily)

//
//     Задание 3.
// Написать функцию, которая создает пустой объект, но без прототипа.
//     При возникновении проблем по ходу решения вы всегда можете обратиться к ментору в Slack.
// function obj(){
//  return Object.create(null);
// }
// console.log (obj());

//task4
//Реализовать следующее консольное приложение подобно примеру,
// который разбирался в видео. Реализуйте его на прототипах.
// Определить иерархию электроприборов. Включить некоторые в розетку.
// Посчитать потребляемую мощность.
// Таких приборов должно быть, как минимум, два
// (например, настольная лампа и компьютер).
// Выбрав прибор, подумайте, какими свойствами он обладает.
function Equipment(name, power){
    this.name = name;
    this.typeIs = 'электроприбор';
    this.isOn = false
    this.power = power;
}
Equipment.prototype.setisOn = function () {
    this.isOn = true;
}
Equipment.prototype.setisOf = function () {
    this.isOn = false;
}
Equipment.prototype.getisOn = function () {
    if (this.isOn = true){
        console.log(this.name+' включено')
    }else {
    console.log(this.isOn+ 'выключено')
}}
Equipment.prototype.powerAll = function () {
    if (this.isOn = true){
        console.log(this.name+' включено')
    }else {
        console.log(this.isOn+ 'выключено')
    }}



const light = new Equipment('Лампа', 30);
const computer = new Equipment('Компьютер', 40);

computer.setisOn();
light.setisOn();

function powerSum(args){
    let result = 0;
    for (let i in args){
        console.log(i[this.power]);
        result += i[this.power];
    }

    console.log(result);
    return result;
    }
powerSum(computer)