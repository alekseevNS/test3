function send_request() {
    let request = new XMLHttpRequest();
    request.open("GET", "http://127.0.0.1:8000/json_test/", true);
    request.onload = function () {
        let responseJSON = JSON.parse(request.response);
        console.log(responseJSON);
    }

    // Добавляем действие на ошибку
    request.onerror = function () {
        console.log("Ошибка");
    }

    request.send();
}

let button = document.querySelector("button");
button.addEventListener("click", send_request);