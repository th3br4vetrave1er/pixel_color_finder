import pyautogui

while True:
    x, y = pyautogui.position()
    print(x, y)
    current_color = pyautogui.pixel(x, y)
    print(f"Pointed color: {current_color}")
    if current_color == (69, 50, 110):
        print(pyautogui.pixel(x, y))
        print('BINGO')
        break
    else:
        print('NOT BINGO')

'''
Jesus, the amount of time i spend installing gnome-screenshot,
considering I already had gnome screenshot BUT NOT HTE ONE PYAUTOGUI WANTED,
IS INSANE!
Then installed Tkinter and pillow. And it worked!
'''

# TODO add user input with custom color search. Make it a function
