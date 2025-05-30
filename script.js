const nombre = document.getElementById("name");
const email = document.getElementById("email");
const button = document.getElementById("btn_enviar");
const form = document.getElementById("contact-form");
const textArea = document.getElementById("message");

function validarFormulario(event) {
    event.preventDefault();
    let error = false;

    if (nombre.value.trim() === "" || email.value.trim() === "" || textArea.value.trim() === "") {
        alert("Por favor, completa todos los campos.");
        error = true;
    }

    if (nombre.value.trim()!=="" && !/^[a-zA-Z\s]+$/.test(nombre.value)) {
        alert("El nombre solo debe contener letras y espacios.");
        error = true;
    }

    if (email.value.trim() !=="" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        error = true;
    }

    if (!error) {
        alert("Datos enviados correctamente, te contactaremos a tu correo proximamente.");
        form.reset();
    }
}
button.addEventListener("click", validarFormulario);