import pygame, sys
from pygame.locals import QUIT
import datetime as dt
from random import randint
import colour # another file in this project
#imports

SCREENWIDTH = 400
SCREENHEIGHT = 600
FPS = 60
#constants
today = 0
mode = 0
last = 0
boxes = -1

pygame.init()
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('Countdown to Christmas!')
pygame.mouse.set_visible(False)
miniFont = pygame.font.SysFont('dejavuserif',10)
smallFont = pygame.font.SysFont('dejavuserif',20)
mediumFont = pygame.font.SysFont('dejavuserif',30)
largeFont = pygame.font.SysFont('dejavuserif',50)
Clock = pygame.time.Clock()
tree = pygame.image.load('xmas tree smol.jpg')
troll1 = pygame.image.load('troll xmas smol.png')
troll2 = troll1
#initialisations, including a clock

monthData = [31,28,31,30,31,30,31,31,30,31,30,31]
monthDataCopy = [31,30,31,30,31,31,30,31,30,31,28,31]
test1 = '2023-12-07 10:29:51.474829'
test2 = '2024-03-01 11:15:29.293838'
test3 = '2024-02-29 22:58:53.999999'
test4 = '2025-12-25 13:32:37.246435'
test5 = '5602-24-75 41:86:98.885545'
test6 = '9999-99-99 99:99:99.999999'# erroneous data

class textbox:
    '''A more compact way of making a text box.
    message --> string of some kind
    font --> a valid font name
    textCol --> a tuple, (redval,greenval,blueval)
    backgroundCol --> also a tuple, (redval,greenval,blueval)
    pos  --> a tuple again, (x coord,y coord)'''
    def __init__(self, message, font, pos, textCol=colour.white, backgroundCol=colour.black):
        self.message = message
        self.font = font
        self.textCol = textCol
        self.backgroundCol = backgroundCol
        self.pos = pos
        self.textRect = None

    def display(self):
        text = self.font.render(str(self.message),True,self.textCol,self.backgroundCol)
        self.textRect = text.get_rect()
        self.textRect.center = self.pos
        SCREEN.blit(text,self.textRect)

    def update_message(self,message='Textbox'):
        self.message = message

    def update_colour(self,textCol=colour.white,backgroundCol=colour.black):
        self.textCol = textCol
        self.backgroundCol = backgroundCol

    def isPressed(self):
        pressed = False
        left, right, up, down = False, False, False, False

        try:
            if pygame.mouse.get_pos()[0] > self.textRect[0]:
                left = True
            if pygame.mouse.get_pos()[0] < self.textRect[0]+self.textRect[2]:
                right = True
            if pygame.mouse.get_pos()[1] > self.textRect[1]:
                up = True
            if pygame.mouse.get_pos()[1] < self.textRect[1]+self.textRect[3]:
                down = True 
        except:
            left, right, up, down = False, False, False, False

        if up and down and left and right:
            pressed = True

        return(pressed)

todayBox = textbox(today,smallFont,(SCREENWIDTH/2,100))
monthsTilXmasBox = textbox('...',smallFont,(SCREENWIDTH/2,290))
daysTilXmasBox = textbox('...',largeFont,(SCREENWIDTH/2,150))
weeksTilXmasBox = textbox('...',smallFont,(SCREENWIDTH/2,330))
hoursTilXmasBox = textbox('...',smallFont,(SCREENWIDTH/2,370))
minutesTilXmasBox = textbox('...',smallFont,(SCREENWIDTH/2,410))
secondsTilXmasBox = textbox('...',smallFont,(SCREENWIDTH/2,450))
milisecondsBox = textbox('...',smallFont,(SCREENWIDTH/2,490))
warningBox = textbox('Time may be innacurate to some degree, based on GMT time zone',miniFont,(SCREENWIDTH/2,SCREENHEIGHT-10))
xmasBox = textbox('IT\'S CHRISTMAS',mediumFont,(SCREENWIDTH/2,200))
textboxes = [todayBox,daysTilXmasBox,monthsTilXmasBox,weeksTilXmasBox,hoursTilXmasBox,minutesTilXmasBox,secondsTilXmasBox,milisecondsBox,xmasBox]

                   
def go_quit():
    pygame.quit()
    sys.exit()
#define the quit function

def show_textboxes():
    todayBox.update_message(today)
    daysTilXmasBox.update_message('Days Left: '+str(timesData[0]))
    weeksTilXmasBox.update_message('Weeks Left: '+str(timesData[2]))
    monthsTilXmasBox.update_message('Months Left: '+str(timesData[1]))
    hoursTilXmasBox.update_message('Hours Left: '+str(timesData[3]))
    minutesTilXmasBox.update_message('Minutes Left: '+str(timesData[4]))
    secondsTilXmasBox.update_message('Seconds Left: '+str(timesData[5]))
    milisecondsBox.update_message('Miliseconds Left: '+str(timesData[6]))
    warningBox.display()
    for i in range(len(textboxes)+boxes):
        textboxes[i].display()

def get_times():
    global today
    today = str(dt.datetime.now())
    #today=test4
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:10])
    hour = int(today[11:13])
    minute = int(today[14:16])
    seconds = int(today[17:19])
    miliseconds = int(today[20:23])
    return(year,month,day,hour,minute,seconds,miliseconds)

def times_left():
    global boxes
    data = get_times()
    #print(data)
    monthsLeft = 12 - data[1]
    daysLeft = 0
    #monthDataCopy.reverse()
    #print(monthDataCopy)
    if data[1] == 12 and data[2] > 25:
        monthsLeft = 12
    
    if monthsLeft > 0:
        for i in range(monthsLeft):
            daysLeft += monthDataCopy[i]

    if not (data[1] == 12 and data[2] == 25):
        #print(daysLeft)
        daysLeft += (25-data[2])
    
        weeksLeft = daysLeft // 7
    
        hoursLeft = 24-data[3]
        hoursLeft += 24*daysLeft

        minutesLeft = 60 - data[4]
        minutesLeft += hoursLeft * 60

        secondsLeft = 60 - data[5]
        secondsLeft += minutesLeft * 60

        milisecondsLeft = secondsLeft * 1000
        milisecondsLeft += 999 - data[6]
        boxes = -1
    else:
        daysLeft = 0
        monthsLeft = 0
        weeksLeft = 0
        hoursLeft = 0
        minutesLeft = 0
        secondsLeft = 0
        milisecondsLeft = 0
        boxes = 0
        celebrate()
        
    return(daysLeft,monthsLeft,weeksLeft,hoursLeft, minutesLeft, secondsLeft, milisecondsLeft)


def celebrate():
    global last, mode
    troll1x = randint(20,38)
    troll1y = randint(0,16)
    troll2x = randint(325,349)
    troll2y = randint(35,50)
    SCREEN.blit(troll1,(troll1x,troll1y))
    SCREEN.blit(troll2,(troll2x,troll2y))

    
    if mode == 0:
        col = colour.red
    else:
        col = colour.green
        
    for box in textboxes:
        box.update_colour(colour.white,col)
    
    now = pygame.time.get_ticks()
    if now - last > 500:
        if mode == 0:
            mode = 1
        else:
            mode = 0
        last = now

#main loop
while True:
    pygame.display.update()
    Clock.tick(FPS)
    #SCREEN.fill(colour.white)
    SCREEN.blit(tree,(-40,0))
    # fills the screen with a blank colour
    
    for event in pygame.event.get():
        if event.type == QUIT:
            go_quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                go_quit()

    #YOUR CODE HERE
    timesData = times_left()
    show_textboxes()