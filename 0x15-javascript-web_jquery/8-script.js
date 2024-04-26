$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const titles = data.results;
  $.each(titles, function (i, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
