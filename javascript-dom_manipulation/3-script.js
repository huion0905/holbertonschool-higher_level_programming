// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with ID 'red_header' and assign a click event detector
    document.getElementById('red_header').addEventListener('click', function() {
        // When clicked, select the 'header' element and add the 'network' class to its list of classes
        document.querySelector('header').classList.add('red');
    });
});