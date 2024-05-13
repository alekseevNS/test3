function get_blog() {
    let request = new XMLHttpRequest();
    request.open("GET", "/get_blog/?blog_id=" + this.innerHTML, true);
    request.onload = function () {
        let responseJSON = JSON.parse(request.response);
        let blogTitle = document.querySelector("#blogTitle");
        let blogText = document.querySelector("#blogText");

        blogTitle.innerHTML = responseJSON.data["title"];
        blogText.innerHTML = responseJSON.data["text"];

        let blogCard = document.querySelector("#blog_card");
        // blogCard.style = "height: auto;";
    }
    request.send();
}

let buttons = document.querySelectorAll(".btn-primary");
for (let index = 0; index < buttons.length; ++index) {
    buttons[index].addEventListener("click", get_blog);
}