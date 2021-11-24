import tkinter
import math
from random import randrange

WIDTH = 1280
HEIGHT = 900
root = tkinter.Tk()
root.title('Solar System')
root.geometry('1280x900')
canv = tkinter.Canvas(root)
canv.pack(fill=tkinter.BOTH, expand=1)

bg = tkinter.PhotoImage(file='space.png')
canv.create_image(WIDTH/2, HEIGHT/2, image=bg)

class Planet:

    def __init__(self, name, r, days=365):
        self.r = r
        self.days = days
        self.x = WIDTH / 2
        self.angle = randrange(0, 6)
        self.y = HEIGHT / 2
        self.image = tkinter.PhotoImage(file=name+'.png')
        self.id = canv.create_image(self.x, self.y, image=self.image)

    def show_info(self):
        pass

    def move(self):
        global earthv
        self.v = (365 / self.days) * earthv
        self.angle += self.v
        self.x = WIDTH / 2 + self.r * math.cos(self.angle)
        self.y = HEIGHT / 2 + self.r * math.sin(self.angle)       
        canv.coords(self.id,
                    self.x,
                    self.y,)
        canv.after(15, self.move)

def init_planets():
    global planets
    mercury = Planet('mercury', 100, 88)
    venus = Planet('venus', 150, 225)
    earth = Planet('earth', 200, 365)
    mars = Planet('mars', 250, 687)
    jupiter = Planet('jupiter', 300, 12*365)
    saturn = Planet('saturn', 350, 29*365)
    uranus = Planet('uranus', 400, 84*365)
    neptune = Planet('neptune', 450, 165*365)
    planets.append(mercury)
    planets.append(venus)
    planets.append(earth)
    planets.append(mars)
    planets.append(jupiter)
    planets.append(saturn)
    planets.append(uranus)
    planets.append(neptune)
    
earthv = 0.01
planets = []
init_planets()
for planet in planets:
    planet.move()
root.mainloop()        
        
