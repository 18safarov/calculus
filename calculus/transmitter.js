// state for the ʸ√x button: cycle through two pieces each click
const _rootStates = ['root(', ', '];
let _rootStateIndex = 0;

const rootbtn = document.getElementById('rootBtn');
const opener = document.getElementById('openerId');
const display = document.getElementById('display');

function resetRootState() {
  _rootStateIndex = 0;
  // restore original button label
  if (rootbtn) rootbtn.textContent = 'ʸ√x';
}

function send(button_value) {
  // reset helper state when starting over or calculating result
  if (button_value === '=' || button_value === 'C') {
    resetRootState();
  }

  pywebview.api.button_pressed(button_value).then(function(result) {
    if (display) display.value = result;
  });
}

// wrapper called by the root button in html
function sendRootButton() {
  const token = _rootStates[_rootStateIndex];
  send(token);

  // update button text so user knows what next click will insert
  if (rootbtn) {
    const next = _rootStates[(_rootStateIndex + 1) % _rootStates.length];
    rootbtn.textContent = next === 'root(' ? 'ʸ√x' : ',';
  }

  // advance index in circular fashion
  _rootStateIndex = (_rootStateIndex + 1) % _rootStates.length;
}

// toggles advanced operations window and resizes webview
if (opener) {
  opener.addEventListener('click', function() {
    pywebview.api.toggle_advanced().then(function(is_open) {
      const adv = document.querySelector('.advanced-window');
      if (adv) adv.classList.toggle('open', is_open);
    });

    opener.textContent = opener.textContent === '<<' ? '>>' : '<<';
  });
}

// allow pressing Enter when typing in the display to evaluate
if (display) {
  display.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      pywebview.api.evaluate(display.value).then(function(result) {
        display.value = result;
      });
      e.preventDefault();
    }
  });
}
