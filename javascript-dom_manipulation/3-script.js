document.getElementById('toggle_header')
  .addEventListener('click', function() {
    header = document.querySelector('header');
    if (header.classList.contains('red'))
      header.classList.replace('red', 'green');
    else
      header.classList.replace('green', 'red');
  });
