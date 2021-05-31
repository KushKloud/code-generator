import string
import random
import pygame
pygame.init()

def code_gen1(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
def code_gen2(size=6, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def code_gen3(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


def redrawWindow():
    global win
    width = 500
    win = pygame.display.set_mode((width, width))
    win.fill((255,255,255))
    Button1.draw(win)
    Button2.draw(win)
    Button3.draw(win)

run = True

#This takes all the info from __init__
Button1 = button((0,255,0), 125, 15, 250, 100, 'Letter Password')
Button2 = button((0,255,0), 125, 150, 250, 100, 'Numbers Password')
Button3 = button((0,255,0), 125, 285, 250, 100, 'Letters and Numbers Password')
Display = button ((0,255,0), 125, 420, 250, 100, 'Output: ' )

while run:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
           if Button1.isOver(pos):
               print(code_gen1())
                

        if event.type == pygame.MOUSEBUTTONDOWN:
           if Button2.isOver(pos):
                print(code_gen2())

        if event.type == pygame.MOUSEBUTTONDOWN:
           if Button3.isOver(pos):
               print(code_gen3())



def closing_tab():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def main():
    global win, result
    width = 500
    win = pygame.display.set_mode((width, width))
    flag = True
    pygame.event.get()
    
    
    clock = pygame.time.Clock()
    
    while flag:
        for event in pygame.event.get():
            pygame.time.delay(50)
            clock.tick(10)
            redrawWindow(win)
            


main()


        
