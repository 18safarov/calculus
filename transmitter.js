// sends button value to backend and updates display
function send(button_value) {
  pywebview.api.button_pressed(button_value).then(function(result) {
    document.getElementById('display').value = result;
  });
}

// toggles advanced operations window
document.querySelector('.opener').addEventListener('click', function() {
  document.querySelector('.advanced-window').classList.toggle('open');
});
