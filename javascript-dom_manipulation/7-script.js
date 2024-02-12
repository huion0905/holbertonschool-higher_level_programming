// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function() {
    // Use Fetch API to fetch data from the provided URL
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(function(response) {
            // Convert the response to JSON format
            return response.json();
        })
        .then(function(data) {
            //Once the promise is resolved and the data is available, select the ul element with ID 'list_movies'.
            var listMoviesElement = document.getElementById('list_movies');

            // Iterate on each film obtained in the answer.
            data.results.forEach(function(movie) {
                // Create a new element li
                var listItem = document.createElement('li');

                // Set the text content of the new li element with the movie title
                listItem.textContent = movie.title;

                // Add the new li element at the end of the ul list
                listMoviesElement.appendChild(listItem);
            });
        })
        .catch(function(error) {
            // In case of an error in the request or in the data processing, print the error in the console.
            console.error('Error fetching movies:', error);
        });
});