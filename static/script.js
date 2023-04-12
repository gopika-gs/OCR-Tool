function showImagePreview() {
    const fileInput = document.getElementById('image-selector');
    const selectedImage = document.getElementById('selected-image');
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function (event) {
        selectedImage.src = event.target.result;
    }

    reader.readAsDataURL(file);
}