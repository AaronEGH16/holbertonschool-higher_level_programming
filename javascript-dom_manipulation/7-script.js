const promisURL = fetch('https://swapi-api.hbtn.io/api/films/?format=json');

promisURL
  .then((response) => {
    if (!response.ok) {
      console.log('network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    const list = document.getElementById('list_movies');
    (data.results).forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
  .catch((error) => console.log(error));
