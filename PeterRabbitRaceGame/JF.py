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
JF = (129, 155, 113)
RED = (150,0,0)
# VARS:
_VARS = {'surf': False}
j=0

def roll(n=6):
    return random.randint(1,n)

# def cut_move(start_pos=0,r=0,type='none'):
#     pos = start_pos + r
#     type=type
#
#     if pos > 157 and r != 6:
#         pos = pos-157+50
#         return pos,type
#     elif r == 6 and pos > 157:
#         pos = pos-157+50
#         if pos == 56:
#             return pos,type
#         else:
#             pos,type = move(6,pos,type)
#             return pos,type
#     elif r == 6 and pos <=157:
#         while r == 6:
#             r = roll(6)
#             print("Roll: {}".format(r))
#             pos+=r
#             if pos > 157:
#                 pos = pos-157+50
#                 if pos == 56:
#                     return pos,type
#                 else:
#                     if r == 6:
#                         pos,type = move(6,pos,type)
#                         return pos,type
#                     else:
#                         return pos,type
#             else:
#                 pass
#             return pos,type
#     else:
#         return pos,type

def even_move(start_pos=0,r=0):
    if r in [2,4]:
        pos = start_pos + r
    elif r in [6]:
        pos = start_pos + r
        while r in [6]:
            if pos >= 103:
                pos,type = move(6,pos,'none')
                break
            else:
                r=roll(6)
                #print("Roll: {}".format(r))
                if r in [2,4,6]:
                    pos+=r
                else:
                    pos=pos
    else:
        pos=start_pos

    if pos >= 96:
        type='none'
    else:
        type='even'
    return pos,type

def back_move(n=6,pos=0,r=0,type='back_2'):
    start_pos=pos
    pos=pos
    max_pos = 123
    re=False
    type=type
    r = r

    # Move ahead by 1s only if in position 33 or 34
    if start_pos in [33,34]:
        if r == 1:
            pos+=r
            r=0
        else:
            pos=pos
            r=0


    # If roll is a 6, set re-roll to true so we can roll again
    if r == 6:
        re=True

    # If there's a halt between the start value and the end value, set position to the HALT and set re-roll to false
    if 33 in range(start_pos-r,start_pos+1) and start_pos != 33:
        pos = 33
        re = False
    elif 56 in range(start_pos-r,start_pos+1) and start_pos != 56:
        pos = 56
        re = False
    else:
        pos-=r

    # Code that carries out a re-roll if you are allowed one
    if re == True:
        r = 6
        while r == 6 and pos<max_pos:
            r = roll(6)
            #print("Roll: {}".format(r))
            if 33 in range(pos-r,pos+1):
                pos=33
                break
            elif 56 in range(pos-r,pos+1):
                pos=56
                break
            elif pos-r <= max_pos:
                pos-=r
            else:
                pos=pos

    # If your position is greater than the last square, and you are not on the shortcut, stay on the last square
    if pos > 123:
        pos = start_pos

    if type == 'back_2':
        type='back_1'
    elif type=='back_1':
        type='none'
    else:
        pass

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
            return pos,type

    if type == 'even':
        pos,type=even_move(start_pos,r)
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

    # Move ahead by 1s only if in position 33 or 34
    if start_pos in [33, 34]:
        if r == 1:
            pos += r
            r = 0
        else:
            pos = pos
            r = 0

    # If there's a halt between the start value and the end value, set position to the HALT and set re-roll to false
    if 33 in range(start_pos,start_pos+r+1) and start_pos != 33:
        pos = 33
        re = False
    elif 56 in range(start_pos,start_pos+r+1) and start_pos != 56:
        pos = 56
        re = False
    else:
        pos+=r

    # Code that carries out a re-roll if you are allowed one
    if re == True:
        r = 6
        while r == 6 and pos<max_pos:
            r = roll(6)
            #print("Roll: {}".format(r))
            if 33 in range(pos,pos+r+1):
                pos=33
                break
            elif 56 in range(pos,pos+r+1):
                pos=56
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
    #pygame.init()
    #_VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    pos=0
    type='none'
    #print("Position: {}".format(pos))
    rolls=[0]*100000000
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
        if pos in [7]:
            rolls[i]+=3
        elif pos in [8]:
            pos+=3
            rolls[i]+=1
        elif pos in [12]:
            pos=7
            rolls[i]+=3
        elif pos in [22]:
            pos=28
            rolls[i]+=1
        elif pos in [32]:
            pos+=1
            rolls[i]+=1
        elif pos in [41]:
            pos=43
            rolls[i]+=1
        elif pos in [52]:
            pos=40
            rolls[i]+=1
        elif pos in [57]:
            pos=62
            rolls[i]+=1
        elif pos in [68]:
            pos=54
            rolls[i]+=1
        elif pos in [77]:
            pos=78
            rolls[i]+=1
        elif pos in [79]:
            rolls[i]+=3
        elif pos in [85,88]:
            pos=88
            type='even'
            rolls[i]+=1
        elif pos in [112]:
            type='back_2'
            rolls[i]+=1
        else:
            rolls[i]+=1
        #print("Total Rolls: {}".format(rolls[i]))
        if pos == 123:
            if (i+1) % 10000 == 0:
                print("Total rolls of game {}: {}".format(i+1, rolls[i]))
            #checkEvents()
            #_VARS['surf'].fill(GREY)
            #drawGrid(12,11,pos)
            #pygame.display.update()
            #time.sleep(j)
            i+=1
            #j*=0.75
            pos=0
            type='none'
        if i == 100000000:
            print("Average rolls: {}".format(sum(rolls)/100000000))
            with open('JF_{}.csv'.format(i), 'w') as file:
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
        _VARS['surf'], JF,
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