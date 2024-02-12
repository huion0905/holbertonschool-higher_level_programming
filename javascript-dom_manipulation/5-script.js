// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function() {
    // Select the element with ID 'update_header'.
    var updateHeaderButton = document.getElementById('update_header');

    // Assigning a click event detector to the 'update_header' button
    updateHeaderButton.addEventListener('click', function() {
        // Select the 'header' element
        var header = document.querySelector('header');

        // Update the text of the 'header' element to 'New Header!!!'.
        header.textContent = 'New Header!!!';
    });
});