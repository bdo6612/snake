import os
from time import sleep
import keyboard, random

def invertedpolepluscheck (num, czyx):
    if czyx:
        try:
            if pole[y_head][x_head + 1] == num:
                return False
            else:
                return True
        except:
            return True
    else:
        try:
            if pole[y_head+1][x_head] == num:
                return False
            else:
                return True
        except:
            return True
def polepluscheck (num, czyx):
    if czyx:
        try:
            if pole[y_head][x_head + 1] == num:
                return True
            else:
                return False
        except:
            return False
    else:
        try:
            if pole[y_head+1][x_head] == num:
                return True
            else:
                return False
        except:
            return False
def apple_adder(pole):
    while(True):
        x_location = random.randint(1, dimensions - 2)
        y_location = random.randint(1, dimensions -2)
        if (pole[y_location][x_location] == 0):
            pole[y_location][x_location] = 4
            break
def drawer(lista):
    os.system('cls')
    print(borders)
    for i in range(0, dimensions - 1):
        r = ""
        for a in range(0, dimensions - 1):
            r = r.replace("","b",1)
        for y in range(0, dimensions - 1):
            if (lista[i][y] == 1):
                r = r.replace("b", " ○", 1)
            elif (lista[i][y] == 2):
                r = r.replace("b", " ⓿", 1)
            elif (lista[i][y] == 3):
                r = r.replace("b", " ⑧", 1)
            elif (lista[i][y] == 4):
                r = r.replace("b", " x", 1)
            else:
                r = r.replace("b", "  ", 1)

        print(f"Q{r}Q")
    print(borders)
                                                # 3 tail,  2 head, 1 body, 0 void
def finder(pole,num):
    x = -1
    y = -1
    for i in range(len(pole)):
        try:
            x = pole[i].index(num)
            y = i
        except:
            pass
    if x!=-1:
        return x,y
    else:
        return False

def kbrdlisten(previous):
    if (keyboard.is_pressed('down') and previous != 'up'):
        return 'down'
    if (keyboard.is_pressed(('up')) and previous != 'down'):
        return 'up'
    if (keyboard.is_pressed('left') and previous != 'right'):
        return 'left'
    if (keyboard.is_pressed('right') and previous != 'left'):
        return 'right'
    else :
        return previous

dimensions = int(input("ENTER AREA DIMENSIONS "))
speed = int(input("ENTER SPEED "))

if dimensions==0 or speed == 0:
    print("cannot be 0")
    exit(0)
borders = ""
for i in range(dimensions):
    borders = borders.replace("", "QQ", 1 )
pole = []
for i in range(dimensions):
    list_insight = []
    for y in range(dimensions):
        list_insight.append(0)
    pole.append(list_insight)

czyzyje = True
pole[5][5] = 2
pole[4][5] = 1
pole[3][5] = 3
lenght = 0


rounds = 0
previous_dir = ['down', 'down']
key_pressed = 'down'
while (czyzyje):

   key_pressed = kbrdlisten(key_pressed)
   previous_dir.append(key_pressed)

   drawer(pole)

   x_tail,y_tail = finder(pole,3)
   x_head,y_head = finder(pole,2)

   if ((x_head == dimensions  and key_pressed == 'right') or (x_head == 0 and key_pressed == 'left') or (y_head == 0 and key_pressed == 'up') or (y_head == dimensions and key_pressed == 'down')):
      break
   else:


        if (key_pressed != 'up' or pole[y_head - 1][x_head] != 4) and (
                key_pressed != 'down' or invertedpolepluscheck(4, False)) and (
                key_pressed != 'left' or pole[y_head][x_head - 1] != 4) and (
                key_pressed != 'right' or invertedpolepluscheck(4, True)):

            if (previous_dir[rounds] == 'up'):
               pole[y_tail - 1][x_tail] = 3
            if (previous_dir[rounds] == 'down'):
               pole[y_tail + 1][x_tail] = 3
            if (previous_dir[rounds] == 'left'):
               pole[y_tail][x_tail - 1] = 3
            if (previous_dir[rounds] == 'right'):
               pole[y_tail][x_tail + 1] = 3
            pole[y_tail][x_tail] = 0

        else:

            lenght += 1
            rounds -= 1

        if (key_pressed == 'up'):
            if (pole[y_head-1][x_head] == 0 or pole[y_head-1][x_head]==4):
              pole[y_head-1][x_head] = 2
            else:
                break
        if (key_pressed == 'down'):
            if (polepluscheck(0, False) or polepluscheck(4, False)):
                pole[y_head +1 ][x_head] = 2
            else:
                break
        if (key_pressed == 'left'):
            if (pole[y_head][x_head - 1] == 0 or pole[y_head][x_head - 1] == 4):
              pole[y_head][x_head - 1] = 2
            else :
                break
        if key_pressed == 'right':
            if polepluscheck(0, True) or polepluscheck(4, True):
              pole[y_head][x_head + 1] = 2
            else:
                break
        pole[y_head][x_head] = 1
        rounds += 1
        if finder(pole, 4) == False :
            apple_adder(pole)
        sleep(1/speed)

os.system('cls')
print(f"             END"
      f"            SCREEN")
print( f"      YOUR SCORE IS {lenght}")
sleep(5)

