import sys
import random
import pygame
from pygame.locals import KEYDOWN, K_q
import math
import time

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 700, 600
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
PR = (67, 123, 163)
JF = (129, 155, 113)
SN = (216,157,84)
# VARS:
_VARS = {'surf': False}
j=0

def roll(n=6):
    return random.randint(1,n)

def odd_move(start_pos=0,r=0):
    if r in [1,3,5]:
        pos = start_pos + r
    elif r in [6]:
        pos = start_pos
        while r in [6]:
            r=roll(6)
            print("Roll: {}".format(r))
            if r in [1,3,5]:
                pos+=r
            else:
                pos=pos
    else:
        pos=start_pos

    if pos >= 34:
        type='none'
    else:
        type='odd'
    return pos,type

def back_move(n=6,pos=0,r=0,type='back_2'):
    start_pos = pos
    pos = pos
    max_pos = 123
    re = False
    type = type
    r = r

    # If roll is a 6, set re-roll to true so we can roll again
    if r == 6:
        re = True

    # If there's a halt between the start value and the end value, set position to the HALT and set re-roll to false
    if 18 in range(start_pos-r, start_pos + 1) and start_pos != 18:
        pos = 18
        re = False
    elif 50 in range(start_pos-r, start_pos + 1) and start_pos != 50:
        pos = 50
        re = False
    elif pos == 51:
        if r in [3, 5]:
            pos -= r
        else:
            pass
    elif 83 in range(start_pos-r, start_pos + 1) and start_pos != 83:
        pos = 83
        re = False
    elif pos == 83:
        if r in [2, 4]:
            pos -= r
        elif r in [6]:
            pos -= r
            re = True
        else:
            pass
    else:
        pos -= r

    # Code that carries out a re-roll if you are allowed one
    if re == True:
        r = 6
        while r == 6 and pos < max_pos:
            r = roll(6)
            print("Roll: {}".format(r))
            if 17 in range(pos-r, pos + 1):
                pos = 17
                break
            elif pos - r <= max_pos:
                pos -= r
            else:
                pos = pos

    # If your position is greater than the last square, and you are not on the shortcut, stay on the last square
    if pos > 123:
        pos = start_pos

    if type == 'back_2':
        type='back_1'
    elif type=='back_1':
        type='none'
    else:
        pass

    return pos, type


def move(n=6,pos=0,type='none'):
    start_pos=pos
    pos=pos
    max_pos = 123
    re=False
    type=type
    r = roll(n)
    print("Roll: {}".format(r))

    # Move onto position 1 if you roll a 6
    if pos == 0:
        if r == 6:
            pos=1
            r=0
            re=True
        else:
            pos=0
            #r=0
            return pos,type

    if type == 'odd':
        pos,type=odd_move(start_pos,r)
        r = 0
        re = False
    elif type == 'back_2':
        pos,type=back_move(6,start_pos,r,type='back_2')
        r = 0
        re = False
    elif type == 'back_1':
        pos,type=back_move(6,start_pos,r,type='back_1')
        r = 0
        re = False
    else:
        pass

    # If roll is a 6, set re-roll to true so we can roll again
    if r == 6:
        re=True

    # If there's a halt between the start value and the end value, set position to the HALT and set re-roll to false
    if 18 in range(start_pos,start_pos+r+1) and start_pos != 18:
        pos = 18
        re = False
        type = 'odd'
    elif 50 in range(start_pos,start_pos+r+1) and start_pos != 50:
        pos = 50
        re = False
    elif pos == 51:
        if r in [3,5]:
            pos+=r
        else:
            pass
    elif 83 in range(start_pos,start_pos+r+1) and start_pos != 83:
        pos = 83
        re = False
    elif pos == 83:
        if r in [2,4]:
            pos+=r
        elif r in [6]:
            pos+=r
            re = True
        else:
            pass
    else:
        pos+=r

    # Code that carries out a re-roll if you are allowed one
    if re == True:
        r = 6
        while r == 6 and pos<max_pos:
            r = roll(6)
            print("Roll: {}".format(r))
            if 18 in range(start_pos, start_pos + r + 1) and start_pos != 18:
                pos = 18
                type = 'odd'
                break
            elif 50 in range(start_pos, start_pos + r + 1) and start_pos != 50:
                pos = 50
                break
            elif 83 in range(start_pos, start_pos + r + 1) and start_pos != 83:
                pos = 83
                break
            elif pos+r <= max_pos:
                pos+=r
            else:
                pos=pos

    # If your position is greater than the last square, and you are not on the shortcut, stay on the last square
    if pos > 123:
        pos = start_pos

    return pos,type

def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    pos=0
    type='none'
    print("Position: {}".format(pos))
    rolls=[0]*10000000
    i=0
    j=0.5
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawGrid(12,11,pos)
        pygame.display.update()
        time.sleep(0.5)
        j*=0.99
        pos,type=move(6,pos,type)
        print("Position: {}".format(pos))
        if pos in [5]:
            pos=1
            rolls[i]+=1
        elif pos in [7]:
            pos=10
            rolls[i]+=1
        elif pos in [35]:
            pos=43
            rolls[i]+=1
        elif pos in [41]:
            rolls[i]+=2
        elif pos in [49]:
            pos=50
            rolls[i]+=1
        elif pos in [64]:
            rolls[i]+=2
        elif pos in [65]:
            pos=72
            rolls[i]+=1
        elif pos in [71]:
            pos=53
            rolls[i]+=1
        elif pos in [74]:
            type='back_2'
            rolls[i]+=1
        elif pos in [80]:
            rolls[i]+=3
        elif pos in [89]:
            pos=80
            rolls[i]+=1
        elif pos in [111]:
            pos=116
            rolls[i]+=1
        else:
            rolls[i]+=1
        print("Total Rolls: {}".format(rolls[i]))
        if pos == 123:
            if (i + 1) % 10000 == 0:
                print("Total rolls of game {}: {}".format(i+1,rolls[i]))
            checkEvents()
            _VARS['surf'].fill(GREY)
            drawGrid(12,11,pos)
            pygame.display.update()
            #time.sleep(j)
            i+=1
            #j*=0.75
            pos=0
            type='none'
        if i == 10000000:
            print("Average rolls: {}".format(sum(rolls)/10000000))
            with open('PR_{}.csv'.format(i), 'w') as file:
                file.write('\n'.join(str(num) for num in rolls))
            time.sleep(2)
            break

def drawGrid(divisionsx,divisionsy,pos):

    CONTAINER_HEIGHT = divisionsx*30 # Not to be confused with SCREENSIZE
    CONTAINER_WIDTH = divisionsy*30
    cont_x, cont_y = 10, 10  # TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (CONTAINER_WIDTH + cont_x, cont_y), 2)
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, CONTAINER_HEIGHT + cont_y),
      (CONTAINER_WIDTH + cont_x, CONTAINER_HEIGHT + cont_y), 2)
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + CONTAINER_HEIGHT), 2)
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (CONTAINER_WIDTH + cont_x, cont_y),
      (CONTAINER_WIDTH + cont_x, CONTAINER_HEIGHT + cont_y), 2)

    # Get cell size, just one since its a square grid.
    cellSizex = CONTAINER_HEIGHT/divisionsx
    cellSizey = CONTAINER_WIDTH/divisionsy

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisionsy):
        pygame.draw.line(
           _VARS['surf'], BLACK,
           (cont_x + (cellSizey * x), cont_y),
           (cont_x + (cellSizey * x), CONTAINER_HEIGHT + cont_y), 2)
    # # HORIZONTAl DIVISIONS
    for x in range(divisionsx):
        pygame.draw.line(
          _VARS['surf'], BLACK,
          (cont_x, cont_y + (cellSizex*x)),
          (cont_x + CONTAINER_WIDTH, cont_y + (cellSizex*x)), 2)

    posy = math.floor(pos/11)
    posx = pos - math.floor(pos/11)*11

    pygame.draw.rect(
        _VARS['surf'], PR,
        (10+((posx)*30)+2, (10+((posy)*30))+2, cellSizex-2, cellSizey-2)
    )

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()