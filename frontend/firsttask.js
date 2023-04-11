//task1
const inputValue = prompt('Введите число')

const value = +inputValue;

if (typeof value == "number" && !isNaN(value)) {
    if (value == 0) {
        console.log('ноль')
    } else if (value % 2 == 0) {
        console.log('чётное')
    } else {
        console.log('нечётное')
    }
} else {
    console.log('Упс, кажется, вы ошиблись')
}
// //tas2
// let x;
//
// switch (typeof x) {
//     case 'number':
//         console.log('x - число');
//         break;
//     case 'string':
//         console.log('x - строка');
//         break;
//     case 'boolean':
//         console.log('x - булево значение');
//         break;
//     default:
//         console.log('Тип x не определен');
// }
// //task3
// const string = 'Hello';
//
// // split разбивает строку на массив символов
// // меняет местами символы (элементы массива)
// // соединяет массив в строку
// const reverseString = string.split("").reverse().join("");
// //task4
// /*
//  ** Math.random() * 101
//  ** возвращает псевдослучайное число с плавающей запятой из диапазона [0, 1),
//  ** то есть, от 0 (включительно) до 1 (но не включая 1)
//  ** Умножаем на 101, тк необходим больший диапазон
//  ** Метод Math.floor() - округляет число.
//  */
// const random = Math.floor(Math.random() * 101);

// //task5
// const arr = [0, null, NaN, 0, 1, 2, 4, "str"]
// console.log('количество элементов: ', arr.length)
//
// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i])
// }
// //task6
// const arr = [1, 2, 3, 3]
//
// let isEqual = true;
// const reference = arr[0];
//
// for (let item of arr) {
//     if (item !== reference) {
//         isEqual = false;
//     }
// }
//
// console.log(isEqual)
//
// //task7
// const arr = [0, null, NaN, 0, 1, 2, 4, "str"]
//
// let even = 0,
//     odd = 0,
//     zero = 0;
//
// for (let i = 0; i < arr.length; i++) {
//     if (typeof arr[i] === 'number' && !isNaN(arr[i])) {
//         if (arr[i] === 0) {
//             zero += 1;
//         } else if (arr[i] % 2 === 0) {
//             even += 1;
//         } else {
//             odd += 1;
//         }
//     }
// }
//
// console.log('четных элементов: ', even)
// console.log('нечетных элементов: ', odd)
// console.log('нулей: ', zero)
//
// //task8
// let map = new Map();
// map.set('key1', 'prop1');
// map.set('key2', 'prop2');
//
// const keys = map.keys()
//
// for (let key of keys) {
//     console.log(`Ключ - ${key}, значение - ${map.get(key)}`)
// }
