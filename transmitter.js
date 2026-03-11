// state for the ʸ√x button: cycle through two pieces each click
const _rootStates = ['root(', ', '];
let _rootStateIndex = 0;

function send(button_value) {
  // reset helper state when starting over or calculating result
  if (button_value === '=' || button_value === 'C') {
    _rootStateIndex = 0;
    // restore original button label
    const rootbtn = document.getElementById('rootBtn');
    if (rootbtn) rootbtn.textContent = 'ʸ√x';
  }

  pywebview.api.button_pressed(button_value).then(function(result) {
    document.getElementById('display').value = result;
  });
}

// wrapper called by the root button in html
function sendRootButton() {
  const token = _rootStates[_rootStateIndex];
  send(token);
  // update button text so user knows what next click will insert
  const rootbtn = document.getElementById('rootBtn');
  if (rootbtn) {
    // show next token or keep original symbol if clearing
    const next = _rootStates[(_rootStateIndex + 1) % _rootStates.length];
    rootbtn.textContent = next === 'root(' ? 'ʸ√x' : ',';
  }
  // advance index in circular fashion
  _rootStateIndex = (_rootStateIndex + 1) % _rootStates.length;
}

const opener = document.getElementById('openerId');

// toggles advanced operations window and resizes webview
opener.addEventListener('click', function() {
  pywebview.api.toggle_advanced().then(function(is_open) {
    document.querySelector('.advanced-window').classList.toggle('open', is_open);
  });
  if (opener.textContent === '<<') {
    opener.textContent = '>>';
  } else {
    opener.textContent = '<<';
  }
});

// allow pressing Enter when typing in the display to evaluate
const display = document.getElementById('display');
display.addEventListener('keydown', function(e) {
  if (e.key === 'Enter') {
    pywebview.api.evaluate(display.value).then(function(result) {
      display.value = result;
    });
    e.preventDefault();
  }
});
