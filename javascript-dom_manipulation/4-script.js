document.getElementById('add_item')
  .addEventListener('click', function () {
    list = document.querySelector('.my_list');
    listItem = document.createElement('li');
    listItem.textContent = 'Item';
    list.appendChild(listItem);
  });
