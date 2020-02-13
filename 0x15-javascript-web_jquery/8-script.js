$.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
  const film = data.results;
  for (const i in film) {
    $('#list_movies').append('<li>' + film[i].title + '</li>');
  }
});
