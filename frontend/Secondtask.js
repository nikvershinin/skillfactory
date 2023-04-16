//task1

/*
function funcCounter(){
  let even = 0,
    odd = 0,
    zero = 0;

    for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === 'number' && !isNaN(arr[i])) {
        if (arr[i] === 0) {
            zero += 1;
        } else if (arr[i] % 2 === 0) {
            even += 1;
        } else {
            odd += 1;
        }
    }}


console.log('четных элементов: ', even)
console.log('нечетных элементов: ', odd)
console.log('нулей: ', zero)

}

const arr = [0, null, NaN, 0, 1, 2, 4, "str"]

funcCounter(arr)
 */

// task2
//function isSimple (n) {
//     if (n === 1 || n === 0 || n >1000) {
//       console.log('Неверное число');
//       return false;
//     } else {
//         for(let i = 2; i < n; i++) {
//             if(n % i === 0) {
//                 console.log('Число сожное')
//                 return false;
//             }
//         }
//         console.log('Число простое')
//         return true;
//     }
// }
// isSimple(56)

//task3
// function example(func){
//     let a=func();
//     return function(b=1){
//         console.log(a+b)
//     }
// }
// function argFunc(a=1){
//     return a
// }
// const resultFunc = example(argFunc);
// resultFunc();

//task4
// Напишите функцию, которая принимает два числа.
// Каждую секунду необходимо выводить в консоль,
// начиная от первого и заканчивая вторым.
// Используйте setInterval.
// Например, пользователь ввёл числа 5 и 15.
// Каждую секунду в консоль должно печататься число,
// начиная с 5 и заканчивая 15 (всего 11 чисел: 5 6 7 8 9 10 11 12 13 14 15).
//
// function numbersLoop(a,b) {
//     console.log(a);
//     a++;
//     setTimeout(function (){
//         if (a<b){
//             numbersLoop(a,b)
//         }
//         else {
//         console.log(b)}
//     }, 1000)
// }
// numbersLoop(5,15)
//
//task5
// Напишите функцию, которая принимает два натуральных числа x и n и возвращает x в
// степени n. Иначе говоря, умножает x на себя n раз и возвращает результат.
//     Используйте Arrow Function синтаксис.
//     Протестируйте функцию на любых значениях и выведите результат в консоль.
// const exponention = (x,n) => console.log(x**n)
// exponention(2,3)