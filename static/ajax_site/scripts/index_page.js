function showAlert() {
    alert("Hello World!");
}

function ajax_load_data() {
    // 1. Составляем запрос (асинхронный -- чтобы страничка не повисла)
    let request = new XMLHttpRequest();
    request.open(method = "GET", url = "/json_test/", async = true);

    // 2. Указываем, что делать после получения ответа
    request.onload = function () {
        let responseJson = JSON.parse(request.response);

        let spanStatus = document.querySelector("#spanStatus");
        let spanData = document.querySelector("#spanData");

        spanStatus.innerHTML = responseJson.status;
        spanData.innerHTML = responseJson.data;
    }

    // 3. Отправляем запрос
    request.send();
}

// Подключаем функцию к клику по кнопке
// 1. Надо получить объект кнопки
// querySelector() -- получение ПЕРВОГО объекта DOM'а
// Можно получать по тегу, классу, id
let button = document.querySelector("#cardButton");
// 2. Привязываем функцию выше к кнопке
button.addEventListener("click", showAlert);

// Пример от Коробова Даниила
// document.querySelector("#cardButton").addEventListener("click", () => { alert("Hello World!") });

let secondCardButton = document.querySelector("#secondCardButton");
secondCardButton.addEventListener("click", ajax_load_data);