const promisURL = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');

promisURL
  .then((response) => {
    if (!response.ok) {
      console.log('network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    const div = document.getElementById('hello');
    const p = document.createElement('p');
    p.textContent = data.hello;
    div.appendChild(p);
  })
  .catch((error) => console.log(error));
