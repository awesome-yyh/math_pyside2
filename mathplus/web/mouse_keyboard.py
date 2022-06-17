from pynput.keyboard import Key
from pynput.keyboard import Controller as kController
from pynput.mouse import Button
from pynput.mouse import Controller as mController
import time 
import pyperclip
import re

mouse = mController()
keyboard = kController()

def mouse_move(x,y):
    #移动鼠标
    mouse.position = (x, y)
    time.sleep(0.01)

def mouse_click(x, y):
    #鼠标单击
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    time.sleep(0.05)

def mouse_dclick(x, y):
    #鼠标双击
    mouse.position = (x, y)
    mouse.click(Button.left, 2)
    time.sleep(0.05)

def key_input(keyName):
    #按下键盘
    keyboard.press(keyName)
    keyboard.release(keyName)
    time.sleep(0.1)

def key_dinput(keyName1, keyName2):
    # 按组合键
    with keyboard.pressed(keyName1):
        keyboard.press(keyName2)
        keyboard.release(keyName2)
    time.sleep(0.1)

##
def copy(times):
    # 复制简单数字
    mouse_dclick(700,500)
    mouse_dclick(1500,500)
    for i in range(times):
        key_dinput(Key.alt, Key.tab)
        key_input(Key.tab)
        key_dinput(Key.ctrl, 'a')
        key_dinput(Key.ctrl, 'c')
        key_dinput(Key.alt, Key.tab)
        key_input(Key.enter)
        key_dinput(Key.ctrl, 'v')
    mouse_move(1500,600)

def copy_plus(times):
    # 复制复杂表达式
    mouse_dclick(700,500)
    mouse_dclick(1500,500)
    for i in range(times):
        key_dinput(Key.alt, Key.tab)
        key_input(Key.tab)
        if i != 0:
            key_input(Key.tab)
        key_dinput(Key.ctrl, 'a')
        key_dinput(Key.ctrl, 'c')
        key_dinput(Key.alt, Key.tab)
        key_input(Key.enter)
        key_dinput(Key.ctrl, 'v')
    mouse_move(1500,600)

def download():
    """自动下载当前网页"""
    mouse_click(500,300)
    key_dinput(Key.ctrl, 's')
    time.sleep(0.8)
    key_dinput(Key.ctrl, 'c')
    time.sleep(0.5)
    title = pyperclip.paste()

    chapter = re.compile(r'\d+\.*\d*')
    chapter = chapter.findall(title)[0]

    keyboard.type(chapter)
    time.sleep(1)
    key_input(Key.enter)
    key_input(Key.left)
    key_input(Key.enter)
    key_input(Key.page_down)
    key_input(Key.page_down)
    mouse_move(1050,60)
    return chapter

if __name__ == "__main__":
    # mouse_click(70,180)
    mouse_move(1050,60)
    # print(download())
    # copy(8)
    # copy_plus(3)
    # download_math113()
