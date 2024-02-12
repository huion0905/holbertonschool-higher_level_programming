// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function() {
    // Use Fetch API to fetch data from the provided URL
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(function(response) {
            // Convert the response to JSON format
            return response.json();
        })
        .then(function(data) {
            // Una vez que la promesa se resuelve y los datos están disponibles, seleccionar el elemento con ID 'character'
            var characterElement = document.getElementById('character');

            // Actualizar el contenido del texto del elemento 'character' con el nombre del personaje obtenido
            characterElement.textContent = data.name;
        })
        .catch(function(error) {
            // In case of an error in the request or in the data processing, print the error in the console.
            console.error('Error fetching character:', error);
        });
});