$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  const hello = data.hello;
  $('#hello').append(hello);
});
