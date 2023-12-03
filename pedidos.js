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

    ValidaCheck: function(vname) {
        if ($("[name='" + vname + "']:checked").val() != undefined) {
            alert('seleccionado:' + $("[name='status']:checked").val());
        } else {
            alert('sin seleccionar');
        }
    }

    validaCheck('status');

}

document.addEventListener("click", (e) => {
    if (e.target === $submit) {
        e.preventDefault();
        validateInputs();
    }
})