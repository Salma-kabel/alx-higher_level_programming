$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', {lang: lan}, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
