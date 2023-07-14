import pyautogui
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()
pyautogui.alert('This is an alert box.')