const promisURL = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');

promisURL
  .then((response) => {
    if (!response.ok) {
      console.log('network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    document.getElementById('character').textContent = data.name;
  })
  .catch((error) => console.log(error));
