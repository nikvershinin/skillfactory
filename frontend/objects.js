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