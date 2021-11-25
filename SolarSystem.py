import tkinter
import math
from random import randrange

WIDTH = 1280
HEIGHT = 900
root = tkinter.Tk()
root.title('Solar System')
root.resizable(False, False)
root.geometry('1280x900')
canv = tkinter.Canvas(root, highlightthickness=0)
canv.pack(fill=tkinter.BOTH, expand=1)

bg = tkinter.PhotoImage(file='space.png')
canv.create_image(WIDTH/2, HEIGHT/2, image=bg)

canv.create_rectangle(1, 0, 150, HEIGHT, fill='purple',
                      outline='white', width=3)
canv.create_rectangle(1130, 0, WIDTH, HEIGHT, fill='purple',
                      outline='white', width=3)
info = canv.create_text(75, HEIGHT/2, fill='white',
                        width=150, justify=tkinter.CENTER)

class Planet:

    def __init__(self, img, r, days, e, ov, m, pr, d, temp, atm, name=''):
        self.r = r
        self.days = days
        self.name = name
        self.e = e
        self.ov = ov
        self.m = m
        self.pr = pr
        self.d = d
        self.temp = temp
        self.atm = atm
        self.x = WIDTH / 2
        self.angle = randrange(0, 6)
        self.y = HEIGHT / 2
        self.image = tkinter.PhotoImage(file=img+'.png')
        self.trail = canv.create_oval(WIDTH/2 - self.r,
                                      HEIGHT/2 + self.r,
                                      WIDTH/2 + self.r,
                                      HEIGHT/2 - self.r, fill='',
                                      outline='blue', width=2,
                                      activeoutline='lightblue')
        self.id = canv.create_image(self.x, self.y, image=self.image)
        
    def show_info(self, event):
        for planet in planets:
            canv.itemconfig(planet.trail, outline='blue')
        canv.itemconfig(self.trail, outline='lightblue')
        canv.itemconfig(info, text=self.name + '\n\n' +
                        'Период обращения вокруг Солнца: \n' +
                        str(self.days) + ' сут.\n' +
                        'Эксцентриситет: \n' + str(self.e) + '\n' +
                        'Средняя орбитальная скорость: \n' +
                        str(self.ov) + ' км/с\n' +
                        'Масса: \n' + str(self.m) + 'x10^24 кг\n' +
                        'Средний радиус планеты: \n' +
                        str(self.pr) + ' км\n' +
                        'Средняя плотность: \n' + str(self.d) + ' г/см3\n' +
                        'Средняя температура поверхности: \n' +
                        str(self.temp) + ' К\n\n' +
                        'Атмосфера ' + self.atm)
    
    def move(self):
        self.v = (365 / self.days) * earthv
        self.angle += self.v
        self.x = WIDTH / 2 + self.r * math.cos(self.angle)
        self.y = HEIGHT / 2 + self.r * math.sin(self.angle)       
        canv.coords(self.id,
                    self.x,
                    self.y,)
        canv.after(15, self.move)

def init_planets():
    mercury = Planet('mercury', 100, 88, 0.2056, 47.87, 0.33, 2439,
                     5.427, 340, 'имеет низкую плотность и состоит из' +
                     ' водорода, гелия, кислорода, паров кальция и натрия',
                     'Меркурий')
    venus = Planet('venus', 150, 225, 0.0068, 35.02, 4.869, 6052,
                   5.204, 735, 'на 96% состоит из углекислого газа и' +
                   ' небольшого количества азота.', 'Венера')
    earth = Planet('earth', 200, 365, 0.0167, 29.79, 5.974, 6371,
                   5.515, 288, 'состоит в основном из газов(кислород, азот)' +
                   ' и различных примесей (пыль, капли воды, кристаллы льда,' +
                   ' морские соли, продукты горения)', 'Земля')
    mars = Planet('mars', 250, 687, 0.0934, 24.13, 0.642, 3389,
                  3.9335, 227, 'имеет следующий состав: углекислый газ — 95%' +
                   ', азот — 2,5, атомарный водород, аргон — 1,6%, остальное' +
                   ' — водяные пары, кислород', 'Марс')
    jupiter = Planet('jupiter', 300, 12*365, 0.0485, 13.06, 1898.6, 69911,
                     1.326, 165, 'состоит из водорода (89 %) и гелия (11 %)' +
                     ', напоминая по химическому составу Солнце', 'Юпитер')
    saturn = Planet('saturn', 350, 29*365, 0.0555, 9.66, 568.46, 58232,
                    0.687, 134, 'очень плотная, она состоит на 94 % из' +
                    ' водорода и на 6 % из гелия', 'Сатурн')
    uranus = Planet('uranus', 400, 84*365, 0.0463, 6.8, 86.81, 25362,
                    1.27, 76, 'состоит из метана(метановой дымки),' +
                    ' ацетилена и других углеводородов', 'Уран')
    neptune = Planet('neptune', 450, 165*365, 0.00899, 5.44, 102.43, 24622,
                     1.638, 72, '- грозовая, состоит из тонких пористых' +
                     ' облаков, состоящих из замерзшего метана', 'Нептун')
    planets.append(mercury)
    planets.append(venus)
    planets.append(earth)
    planets.append(mars)
    planets.append(jupiter)
    planets.append(saturn)
    planets.append(uranus)
    planets.append(neptune)

def change_speed(button):
    global earthv
    dv = 0.005
    if earthv >= 0.0:
        if button == 1:
            earthv += dv
        elif button == 2:
            earthv -= dv
        elif button == 3:
            earthv += 10 * dv
        elif button == 4:
            earthv -= 10 * dv
        elif button == 6:
            earthv = 0.01
    if earthv <= 0.0 or button == 5:
        earthv = 0.0
    canv.itemconfig(speedtxt, text='Текущая орбитальная скорость Земли: \n' +
                              str(round(earthv * 2979, 3)) + ' км/с')        

earthv = 0.01
up = tkinter.Button(canv, cursor='top_side', width=10,
                    command=lambda b=1: change_speed(b), text='Скорость+')
down = tkinter.Button(canv, cursor='bottom_side', width=10,
                      command=lambda b=2: change_speed(b), text='Скорость-')
up2 = tkinter.Button(canv, cursor='sb_up_arrow', width=10,
                      command=lambda b=3: change_speed(b), text='Скорость+++')
down2 = tkinter.Button(canv, cursor='sb_down_arrow', width=10,
                      command=lambda b=4: change_speed(b), text='Скорость---')
set0 = tkinter.Button(canv, cursor='X_cursor', width=10,
                      command=lambda b=5: change_speed(b), text='0.0 км/с')
default = tkinter.Button(canv, cursor='exchange', width=10,
                      command=lambda b=6: change_speed(b), text='Сбросить')
up.place(x=1167, y=HEIGHT/2 - 100)
down.place(x=1167, y=HEIGHT/2 + 100)
up2.place(x=1167, y=HEIGHT/2 - 150)
down2.place(x=1167, y=HEIGHT/2 + 150)
set0.place(x=1167, y=HEIGHT/2 + 200)
default.place(x=1167, y=HEIGHT/2 + 250)
speedtxt = canv.create_text(1205, HEIGHT/2, fill='white', width=150,
                            justify=tkinter.CENTER,
                            text='Текущая орбитальная скорость Земли: \n' +
                            str(earthv * 2979) + ' км/с')

planets = []
init_planets()
for planet in planets:
    canv.tag_bind(planet.id, '<Button-1>', planet.show_info)
    canv.tag_bind(planet.trail, '<Button-1>', planet.show_info)
    planet.move()
root.mainloop()             
