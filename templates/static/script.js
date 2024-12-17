// Validación básica de formulario
document.getElementById('registroForm').addEventListener('submit', function(event) {
    const nombre = document.getElementById('nombre').value;
    const edad = document.getElementById('edad').value;
    const email = document.getElementById('email').value;

    if (!nombre || !edad || !email) {
        alert("Por favor, complete todos los campos.");
        event.preventDefault(); // Evitar el envío del formulario si falta un campo
    }
});
