const nameField = document.querySelector("[name=nombre]")
const apellido = document.querySelector("[name=apellido]")
const email = document.querySelector("[name=email]")
const consulta = document.querySelector("[name=consulta]")

const validateEmptyField = (message, e) => {
    const field = e.target;
    const fieldValue = e.target.value;
    if (fieldValue.trim().length === 0) {
        field.classList.add("invalid");
        field.nextElementSibling.classList.add("error");
        field.nextElementSibling.innerText = message;
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.classList.remove("error");
        field.nextElementSibling.innerText = "";
    }
}

const validateEmailFormat = e => {
    const field = e.target;
    const regex = new RegExp(/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/
    );
}


nameField.addEventListener("blur", (e) => validateEmptyField("Escribe un nombre", e));
apellido.addEventListener("blur", (e) => validateEmptyField("Escribe un apellido", e));
email.addEventListener("blur", (e) => validateEmptyField("Escribe un email", e));
consulta.addEventListener("blur", (e) => validateEmptyField("Escribe una consulta", e));

email.addEventListener("input", validateEmailFormat);
