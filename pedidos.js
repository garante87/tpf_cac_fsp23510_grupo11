const $submit = document.getElementById("submit"),
    $name = document.getElementById("name"),
    $address = document.getElementById("address"),
    $order = document.getElementById("order");

function validateInputs() {
    if ($name.value === "") {
        alert("Por favor ingresa un nombre y apellido");
    }
    if ($address.value === "") {
        alert("Por favor ingresa una direccion de envio");
    }
    if ($order.value === "") {
        alert("Por favor ingresa una orden");
    }
}

document.addEventListener("click", (e) => {
    if (e.target === $submit) {
        e.preventDefault();
        validateInputs();
        validar();
    }
})
