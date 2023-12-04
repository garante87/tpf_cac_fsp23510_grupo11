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


function validar() {
    const todo_correcto = true;
    if (!todo_correcto) {
        alert('Algunos campos no están correctos, vuelva a revisarlos');
    }
    return todo_correcto;
}

document.addEventListener("click", (e) => {
    if (e.target === $submit) {
        e.preventDefault();
        validateInputs();
        validar();
    }
})
