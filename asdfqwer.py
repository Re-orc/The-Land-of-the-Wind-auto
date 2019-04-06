import pyautogui
import time

b,c,f = 0,0,0
i = 0

class auto:
    '바람의나라 오토'

    def Onenum(self):
        pyautogui.hotkey('1','down','enter')
        pyautogui.hotkey('1','up','enter')
        pyautogui.hotkey('1','left','enter')
        pyautogui.hotkey('1','right','enter')
        pyautogui.hotkey('3','enter')
        pyautogui.hotkey('0')

    def Twonum(self):
        pyautogui.hotkey('2')
        pyautogui.hotkey('2')
        pyautogui.hotkey('2')
    
    def buff(self):
        pyautogui.hotkey('5')
        time.sleep(4)
        

    def up(self):
        pyautogui.hotkey('up')

    def down(self):
        pyautogui.hotkey('down')

Auto = auto()

while True:
    i +=  1
    start = time.time()
    Auto.Onenum()
    a = time.time() - start
    b += a; c += a;  f += a
    if round(b,1) >= 5.0:
        Auto.Twonum()
        b = 0
    if round(c,1) >= 60.0:
        Auto.buff()
        c = 0
    if i <= 25 and round(b,1) >= 2.0:
        Auto.up()
    elif i > 25 and i < 51:
        Auto.down()
    if i == 51:
        i =0
#pyautogui.click(100,100)
