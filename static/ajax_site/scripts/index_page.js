function showAlert() {
    alert("Hello World!");
}

// Подключаем функцию к клику по кнопке
// 1. Надо получить объект кнопки
// querySelector() -- получение ПЕРВОГО объекта DOM'а
// Можно получать по тегу, классу, id
let button = document.querySelector("button");
// 2. Привязываем функцию выше к кнопке
button.addEventListener("click", showAlert);

// Пример от Коробова Даниила
// document.querySelector("button").addEventListener("click", () => { alert("Hello World!") });