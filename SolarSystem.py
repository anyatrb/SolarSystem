import tkinter
import math
import time

root = tkinter.Tk()
root.geometry('1280x720')
canv = tkinter.Canvas(root)
canv.focus()
canv.pack(fill=tkinter.BOTH, expand=1)

class Planet:

    def __init__(self, r=200, days=365):
        self.r = r
        self.days = days
        self.x = 640
        self.angle = 0
        self.y = 360
        self.image = tkinter.PhotoImage(file='test.png')
        self.id = canv.create_image(self.x, self.y, image=self.image)

    def show_info(self):
        pass

    def move(self):
        global earthv
        self.v = (365 / self.days) * earthv
        self.angle += self.v
        self.x = 640 + self.r * math.cos(self.angle)
        self.y = 360 + self.r * math.sin(self.angle)       
        canv.coords(self.id,
                    self.x,
                    self.y,)
        canv.after(32, self.move)

        
earthv = 0.01
earth = Planet()
earth.move()
root.mainloop()        
        
