window.onkeyup = function validate_password() {
    if (document.getElementById('id_password1').value == document.getElementById('id_password2').value) {
        document.getElementById('submit-button').disabled = false;
    } else {
        document.getElementById('submit-button').disabled = true;
    }
}
