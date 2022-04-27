import time
import pyautogui
import tkinter.filedialog
import os
from datetime import datetime

n = 5
for i in range(n):
    print((((2*i)+1)*"*").center((2*n)-1))
    time.sleep(2)

for i in range(n, 0, -1):
    print((((2*i)-1)*"*").center(((2*n)-1)*3))
    time.sleep(2)

screen = pyautogui.screenshot()
folder = tkinter.filedialog.askdirectory()
current_time = datetime.now().replace(microsecond=0)
Format = "%y_%b_%d_%H_%M_%S"
current_time = datetime.strftime(current_time, Format)
file_name = "hello "+current_time+".png"
file = os.path.join(folder, file_name)
screen.save(file)
