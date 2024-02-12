// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function() {
    // Select the element with ID 'add_item'.
    var addItemButton = document.getElementById('add_item');

    // Select the ul element with class 'my_list'.
    var myList = document.querySelector('.my_list');

    // Assigning a click event detector to the 'add_item' button
    addItemButton.addEventListener('click', function() {
        // Create a new element li
        var newLi = document.createElement('li');

        // Set the text content of the new item li
        newLi.textContent = 'Item';

        // Add the new li element at the end of the ul list
        myList.appendChild(newLi);
    });
});