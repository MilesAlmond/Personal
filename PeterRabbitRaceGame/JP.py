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
JP = (220,91,113)

# VARS:
_VARS = {'surf': False}
j=0

def roll(n=6):
    return random.randint(1,n)

def two_or_three(start_pos=0,r=0):
    if r in [2,3]:
        pos = start_pos + r
    elif r in [6]:
        pos = start_pos
        while r in [6]:
            r=roll(6)
            #print("Roll: {}".format(r))
            if r in [2,3]:
                pos+=r
            else:
                pos=pos
    else:
        pos=start_pos

    if pos >= 90:
        type='none'
    else:
        type='2or3'
    return pos,type

def odd_move(start_pos=0,r=0):
    if r in [1,3,5]:
        pos = start_pos + r
    elif r in [6]:
        pos = start_pos
        while r in [6]:
            r=roll(6)
            #print("Roll: {}".format(r))
            if r in [1,3,5]:
                pos+=r
            else:
                pos=pos
    else:
        pos=start_pos

    if pos >= 110:
        pos=110
        type='none'
    else:
        type='odd'
    return pos,type

def cut_move(start_pos=0,r=0,type='none'):
    pos=start_pos+r
    type=type
    #print(pos)
    #print(type)

    if pos > 171 and r != 6:
        pos = pos-171+33
        return pos,type
    elif r == 6 and pos > 171:
        pos = pos-171+33
        pos,type = move(6,pos,type)
        return pos,type
    elif r == 6 and pos <=171:
        while r == 6:
            r = roll(6)
            #print("Roll: {}".format(r))
            pos+=r
            if pos > 171:
                pos = pos-171+33
                if r == 6:
                    pos,type = move(6,pos,type)
                    return pos,type
                else:
                    return pos,type
            else:
                pass
        return pos,type
    else:
        #print(pos)
        #print(type)
        return pos,type

def cut_move_2(start_pos=0,r=0,type='none'):
    pos=start_pos+r
    #print(pos)
    type=type

    if pos > 262 and r != 6:
        pos = pos-262+47
        return pos,type
    elif r == 6 and pos > 262:
        pos = pos-262+47
        pos,type = move(6,pos,type)
        return pos,type
    elif r == 6 and pos <=262:
        while r == 6:
            r = roll(6)
            #print("Roll: {}".format(r))
            pos+=r
            if pos > 262:
                pos = pos-262+47
                if r == 6:
                    pos,type = move(6,pos,type)
                    return pos,type
                else:
                    return pos,type
            else:
                pass
        return pos,type
    else:
        return pos,type

def move(n=6,pos=0,type='none'):
    start_pos=pos
    pos=pos
    max_pos = 123
    re=False
    type=type
    r = roll(n)
    #print("Roll: {}".format(r))

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

    if type == '2or3':
        pos,type=two_or_three(start_pos,r)
        r = 0
        re = False
    elif type == 'odd':
        pos,type=odd_move(start_pos,r)
    else:
        pass

    # If roll is a 6, set re-roll to true so we can roll again
    if r == 6:
        re=True

    if pos >= 150 and pos < 250:
        pos,type = cut_move(pos,r,'none')
        r = 0
        re = False
    elif pos >= 250:
        pos,type = cut_move_2(pos,r,'none')
        r = 0
        re = False
    else:
        pass


    # If there's a halt between the start value and the end value, set position to the HALT and set re-roll to false
    if 78 in range(start_pos,start_pos+r+1) and start_pos != 78:
        pos = 78
        re = False
        type = '2or3'
    elif 110 in range(start_pos,start_pos+r+1) and start_pos != 110:
        pos = 110
        re = False
    else:
        pos+=r

    # Code that carries out a re-roll if you are allowed one
    if re == True:
        r = 6
        while r == 6 and pos<max_pos:
            r = roll(6)
            #print("Roll: {}".format(r))
            if 17 in range(pos,pos+r+1):
                pos=17
                break
            elif 110 in range(start_pos, start_pos + r + 1) and start_pos != 110:
                pos = 110
                break
            elif pos+r <= max_pos:
                pos+=r
            else:
                pos=pos

    # If your position is greater than the last square, and you are not on the shortcut, stay on the last square
    if pos > 123 and pos < 150:
        pos = start_pos

    return pos,type

def main():
    #pygame.init()
    #_VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    pos=0
    type='none'
    #print("Position: {}".format(pos))
    rolls=[0]*10000000
    i=0
    j=0.5
    while True:
        #checkEvents()
        #_VARS['surf'].fill(GREY)
        #drawGrid(12,11,pos)
        #pygame.display.update()
        #time.sleep(j)
        j*=0.99
        pos,type=move(6,pos,type)
        #print("Position: {}".format(pos))
        if pos in [6]:
            pos=1
            rolls[i]+=1
        elif pos in [12]:
            pos=20
            rolls[i]+=1
        elif pos in [26]:
            pos=150
            rolls[i]+=1
        elif pos in [34]:
            rolls[i]+=3
        elif pos in [42]:
            pos=250
            rolls[i]+=1
        elif pos in [50]:
            pos=35
            rolls[i]+=1
        elif pos in [66]:
            pos=77
            rolls[i]+=1
        elif pos in [90]:
            rolls[i]+=3
        elif pos in [91]:
            type='odd'
            rolls[i]+=1
        elif pos in [113]:
            pos=123
            rolls[i]+=1
        else:
            rolls[i]+=1
        #print("Total Rolls: {}".format(rolls[i]))
        if pos == 123:
            if (i + 1) % 10000 == 0:
                print("Total rolls of game {}: {}".format(i+1,rolls[i]))
            #checkEvents()
            #_VARS['surf'].fill(GREY)
            #drawGrid(12,11,pos)
            #pygame.display.update()
            #time.sleep(j)
            i+=1
            #j*=0.75
            pos=0
            type='none'
        if i == 10000000:
            print("Average rolls: {}".format(sum(rolls)/10000000))
            with open('JP_{}.csv'.format(i), 'w') as file:
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
        _VARS['surf'], JP,
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