
# How to use:
# Copy the file path of the folder containing your RAW and jpeg photos (Shortcut: Ctrl L then Ctrl C)
# Run this script Rawculling.py
# That's all!!!

#! python3
import sys, pyperclip, os, fnmatch, pyautogui
from os.path import splitext
from send2trash import send2trash

address = pyperclip.paste()

os.chdir(address)
print(f'Current working directory: {os.getcwd()}')
dirlist = os.listdir()

jpg = []
arw = []

for file in dirlist:
    if fnmatch.fnmatch(file, '*.jpg'):
        jpg.append(splitext(file)[0])
    elif fnmatch.fnmatch(file, '*.arw'):
        arw.append(splitext(file)[0])

diff = list(set(arw).difference(jpg))
# print(diff)
diffext = [s + ".arw" for s in diff]
# print(diffext)

send2trash(diffext)

# for arwfile in diffext:
#     todelete = address + '\\' + arwfile
#     print(f'This file is deleted: {arwfile}')
#     os.remove(todelete)

print(f'These files are deleted: {diffext}')
print(f'{len(diffext)} items were deleted')

pyautogui.alert(f'{len(diffext)} item(s) were deleted', 'RAW photos culling (from Rawculling.py)')
