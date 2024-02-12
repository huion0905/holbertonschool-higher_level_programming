// Since the script is loaded in the <head>, it is necessary to ensure that the DOM is fully loaded before executing the code.
document.addEventListener('DOMContentLoaded', function() {
    // Use Fetch API to fetch data from the provided URL
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(function(response) {
            // Convert the response to JSON format
            return response.json();
        })
        .then(function(data) {
            // Once the promise is resolved and the data is available, select the element with ID 'hello'.
            var helloElement = document.getElementById('hello');

            // Update the text content of the 'hello' element with the value of 'hello' obtained from the response
            helloElement.textContent = data.hello;
        })
        .catch(function(error) {
            // In case of an error in the request or in the data processing, print the error in the console.
            console.error('Error fetching greeting:', error);
        });
});