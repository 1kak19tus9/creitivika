import pyautogui
import keyboard
a = input("введите команду: ")
if a == "выход":
    exit
elif a == "поиск":
    b = input("введите запрос: ")
    pyautogui.moveTo(219, 1071)
    pyautogui.click()
    pyautogui.moveTo(1608, 25)
    pyautogui.click()
    keyboard.write(b)#print(pyautogui.write('введите запрос', interval=0.25)
    pyautogui.press('enter')