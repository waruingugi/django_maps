// Set random blob images
// Main colors: #00C569, #FC2101
elements = document.getElementsByClassName('cart-illustration');

for (var i = 0; i < elements.length; i++) {
    // Generate random number

    var max_range = 15;
    var random_number = Math.floor(Math.random() * max_range);
    var blob_name = 'blob_'+ random_number +'.svg';
    var image = "url(static/assets/img/blobs/" + blob_name + ")";

    elements[i].style.backgroundImage = image;

}