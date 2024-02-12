// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with the ID 'toggle_header'.
    var toggleHeader = document.getElementById('toggle_header');

    // Assigning a click event detector to the selected element
    toggleHeader.addEventListener('click', function() {
        // Select the 'header' element
        var header = document.querySelector('header');

        // Check if the 'header' element currently has the class 'network'.
        if (header.classList.contains('red')) {
            // If so, remove the class 'red' and add the class 'green'.
            header.classList.remove('red');
            header.classList.add('green');
        } else {
            // If the 'header' element does not have the class 'red', remove 'green' and add 'red'.
            header.classList.remove('green');
            header.classList.add('red');
        }
    });
});