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
    document.getElementById("hello").textContent = data.hello;
  })
  .catch((error) => console.log(error));
