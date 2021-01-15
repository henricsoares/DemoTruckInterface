import tkinter as tk
import math
import keyboard
from time import sleep, time
from PIL import ImageTk, Image
import random  # noqa: F401


class App(tk.Frame):
    def __init__(self, master):
        self.rArrowAux = False
        self.rArrowAuxx = False
        self.lArrowAux = False
        self.lArrowAuxx = False
        self.arrowTime = time()
        self.arrowTimee = time()
        tk.Frame.__init__(self, master)
        master.winfo_toplevel().title("Python Interfaces")
        self.mainFrame = tk.Frame(master)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)
        self.frameW, self.framH = (self.mainFrame.winfo_screenwidth()), \
                                  (self.mainFrame.winfo_screenheight())
        self.canvas1 = tk.Canvas(self.mainFrame, width=(3/10)*self.frameW,
                                 height=(3/10)*self.frameW,
                                 background='black',
                                 bd=0, highlightthickness=0)
        self.canvas2 = tk.Canvas(self.mainFrame, width=(4/10)*self.frameW,
                                 height=(3/10)*self.frameW,
                                 background='black',
                                 bd=0, highlightthickness=0)
        self.canvas3 = tk.Canvas(self.mainFrame, width=(3/10)*self.frameW,
                                 height=(3/10)*self.frameW,
                                 background='black',
                                 bd=0, highlightthickness=0)
        self.hDim2 = int(self.canvas2['width'])
        self.vDim2 = int(self.canvas2['height'])
        self.bg = Image.open('bg.png')
        self.bg = self.bg.resize((2*self.hDim2, 2*(self.vDim2)),
                                 Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.canvas1.create_image((0, 0),
                                  image=self.bg)
        self.canvas2.create_image((0, 0),
                                  image=self.bg)
        self.canvas3.create_image((0, 0),
                                  image=self.bg)
        self.canvas1.grid(column=0, row=0)
        self.canvas2.grid(column=1, row=0)
        self.canvas3.grid(column=2, row=0)
        # canvas 1
        self.hDim = int(self.canvas1['width'])
        self.vDim = int(self.canvas1['height'])
        self.canvas1.create_oval((self.hDim/2) - .48*self.hDim,
                                 (self.vDim/2) - .48*self.vDim,
                                 (self.hDim/2) + .48*self.hDim,
                                 (self.vDim/2) + .48*self.vDim,
                                 fill='', outline='white',
                                 width=3)
        self.canvas1.create_oval((self.hDim/2) - .2*self.hDim,
                                 (self.vDim/2) - .2*self.vDim,
                                 (self.hDim/2) + .2*self.hDim,
                                 (self.vDim/2) + .2*self.vDim,
                                 fill='',
                                 outline='white', width=3)
        self.canvas3.create_oval((self.hDim/2) - .48*self.hDim,
                                 (self.vDim/2) - .48*self.vDim,
                                 (self.hDim/2) + .48*self.hDim,
                                 (self.vDim/2) + .48*self.vDim,
                                 fill='', outline='white',
                                 width=3)
        self.canvas3.create_oval((self.hDim/2) - .2*self.hDim,
                                 (self.vDim/2) - .2*self.vDim,
                                 (self.hDim/2) + .2*self.hDim,
                                 (self.vDim/2) + .2*self.vDim,
                                 fill='',
                                 outline='white', width=3)
        self.velValue = 0
        self.velHolder = self.canvas1.create_text(self.hDim/2, self.vDim/2,
                                                  text=self.velValue,
                                                  fill='white',
                                                  font=('Helvetica', '36',
                                                        'bold'))
        self.canvas1.create_text(self.hDim/2, 1.2*self.vDim/2,
                                 fill='white',
                                 text='km/h',
                                 font=('Helvetica', '11',
                                       'bold'))
        self.rpmHolder = self.canvas3.create_text(self.hDim/2, self.vDim/2,
                                                  text='0', fill='white',
                                                  font=('Helvetica', '36',
                                                        'bold'))
        self.canvas3.create_text(self.hDim/2, 1.25*(self.vDim/2),
                                 fill='white',
                                 text='x1000 \n RPM',
                                 font=('Helvetica', '11',
                                       'bold'))
        self.angle = 0
        self.points = [[self.hDim/2, .98*self.vDim],
                       [self.hDim/2, .90*self.vDim]]
        self.pointss = [[self.hDim/2, .98*self.vDim],
                        [self.hDim/2, .94*self.vDim]]
        self.pointss = self.rotate(self.pointss, -18,
                                   [(self.hDim/2), (self.vDim/2)])
        self.pointsP1 = [[self.hDim/2, .01*self.vDim],
                         [self.hDim/2, self.vDim/2 - .2*self.vDim]]
        self.pointsP2 = [[self.hDim/2, .01*self.vDim],
                         [self.hDim/2, self.vDim/2 - .2*self.vDim]]
        for i in range(1, 10, 1):
            self.points = self.rotate(self.points, 36,
                                      [(self.hDim/2), (self.vDim/2)])
            self.canvas1.create_line(self.points, fill='white', width=3)
            self.canvas3.create_line(self.points, fill='white', width=3)
            if 1 < i < 10:
                self.pointss = self.rotate(self.pointss, -36,
                                           [(self.hDim/2), (self.vDim/2)])
                self.canvas1.create_line(self.pointss, fill='white', width=3)
                self.canvas3.create_line(self.pointss, fill='white', width=3)
        self.pointsP1 = self.rotate(self.pointsP1, 216,
                                    [(self.hDim/2), (self.vDim/2)])
        self.pointsP2 = self.rotate(self.pointsP2, 216,
                                    [(self.hDim/2), (self.vDim/2)])
        self.p1 = self.canvas1.create_line(self.pointsP1, fill='red',
                                           width=9, smooth=True)
        self.p2 = self.canvas3.create_line(self.pointsP2, fill='red',
                                           width=9, smooth=True)
        # canvas 2
        self.lLanePos = [.45*self.hDim2,
                         self.vDim2/2,
                         0*self.hDim2,
                         self.vDim2,
                         .05*self.hDim2,
                         self.vDim2]
        self.rLanePos = [.55*self.hDim2,
                         self.vDim2/2,
                         1*self.hDim2,
                         self.vDim2,
                         .95*self.hDim2,
                         self.vDim2]
        self.rLane = self.canvas2.create_polygon(self.rLanePos,
                                                 fill='silver',
                                                 width=self.hDim2*.02)
        self.lLane = self.canvas2.create_polygon(self.lLanePos,
                                                 fill='silver',
                                                 width=self.hDim2*.02)
        self.img = Image.open('truck.png')
        self.truckPos = [self.hDim2/2, .65*self.vDim2]
        self.img = self.img.resize((int(self.hDim2*4/10),
                                    int(self.hDim2*4/10)),
                                   Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.truck = self.canvas2.create_image(self.truckPos,
                                               image=self.img)
        self.ldwHolder = self.canvas2.create_text(self.hDim2/2,
                                                  self.vDim*.95,
                                                  justify=tk.CENTER,
                                                  text='', fill='white',
                                                  font=('Helvetica', '14',
                                                        'bold'))
        self.velSign = self.canvas2.create_oval((self.hDim2/2) - .1*self.hDim2,
                                                (.16*self.vDim2) -
                                                .1*self.hDim2,
                                                (self.hDim2/2) + .1*self.hDim2,
                                                (.16*self.vDim) +
                                                .1*self.hDim2,
                                                fill='white', outline='red',
                                                width=self.hDim2*.02)
        self.velSignValue = self.canvas2.create_text(self.hDim2/2,
                                                     .16*self.vDim2,
                                                     fill='black',
                                                     text='80',
                                                     font=('Helvetica',
                                                           '36',
                                                           'bold'))
        self.velSignUnit = self.canvas2.create_text(self.hDim2/2,
                                                    .16*self.vDim2 +
                                                    .06*self.hDim2,
                                                    fill='black',
                                                    text='km/h',
                                                    font=('Helvetica',
                                                          '11',
                                                          'bold'))
        self.leftArrow = self.canvas2.create_polygon([.1*self.hDim2,
                                                     .2*self.vDim2],
                                                     [.15*self.hDim2,
                                                     .1*self.vDim2],
                                                     [.15*self.hDim2,
                                                     .15*self.vDim2],
                                                     [.2*self.hDim2,
                                                     .15*self.vDim2],
                                                     [.2*self.hDim2,
                                                     .25*self.vDim2],
                                                     [.15*self.hDim2,
                                                     .25*self.vDim2],
                                                     [.15*self.hDim2,
                                                     .3*self.vDim2],
                                                     [.1*self.hDim2,
                                                     .2*self.vDim2],
                                                     fill='green',
                                                     width=self.hDim2*.005)
        self.rightArrow = self.canvas2.create_polygon([.9*self.hDim2,
                                                      .2*self.vDim2],
                                                      [.85*self.hDim2,
                                                      .1*self.vDim2],
                                                      [.85*self.hDim2,
                                                      .15*self.vDim2],
                                                      [.8*self.hDim2,
                                                      .15*self.vDim2],
                                                      [.8*self.hDim2,
                                                      .25*self.vDim2],
                                                      [.85*self.hDim2,
                                                      .25*self.vDim2],
                                                      [.85*self.hDim2,
                                                      .3*self.vDim2],
                                                      [.9*self.hDim2,
                                                      .2*self.vDim2],
                                                      fill='green',
                                                      width=self.hDim2*.005)
        self.canvas2.itemconfigure(self.velSign, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignValue, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignUnit, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.leftArrow, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.rightArrow, state=tk.HIDDEN)

    def rotate(self, points, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center[0], center[1]
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points

    def vAngle(self, op):
        if op == 'inc' and self.angle < 288:
            self.pointsP1 = self.rotate(self.pointsP1, 1.8,
                                        [(self.hDim/2), (self.vDim/2)])
            self.canvas1.coords(self.p1, self.pointsP1[0][0],
                                self.pointsP1[0][1],
                                self.pointsP1[1][0],
                                self.pointsP1[1][1])
            sleep(.00001)
            self.master.update()
            self.angle += 1.8
            round(self.angle, 1)
            self.canvas1.itemconfigure(self.velHolder,
                                       text=int(self.angle/1.8))
        elif op == 'dec' and self.angle >= 1.7:
            self.pointsP1 = self.rotate(self.pointsP1, -1.8,
                                        [(self.hDim/2), (self.vDim/2)])
            self.canvas1.coords(self.p1, self.pointsP1[0][0],
                                self.pointsP1[0][1],
                                self.pointsP1[1][0],
                                self.pointsP1[1][1])
            sleep(.00001)
            self.master.update()
            self.angle -= 1.8
            round(self.angle, 1)
            if not (0 <= self.angle <= 288):
                if self.angle < 0:
                    self.angle = 0
                elif self.angle > 288:
                    self.angle = 288
            self.canvas1.itemconfigure(self.velHolder,
                                       text=int(self.angle/1.8))

    def arrows(self, opt='verify'):
        if opt == 'right':
            pass
        elif opt == 'left':
            pass
        if opt == 'verify':
            if self.rArrowAux or self.lArrowAux:
                self.arrowTimee = time()
                if (self.arrowTimee - self.arrowTime) >= .5:
                    if self.rArrowAux:
                        self.rArrowAuxx = True
                    elif self.lArrowAux:
                        self.lArrowAuxx = True
                    '''if not self.blinkauxx:
                        self.bTimeee = time()
                    self.warnings('verif', 'blink')'''
                if self.rArrowAux and self.rArrowAuxx:
                    # print('right arrow')
                    state = self.canvas2.itemconfig(self.rightArrow,
                                                    'state')[4]
                    if state == 'hidden':
                        self.canvas2.itemconfigure(self.rightArrow,
                                                   state=tk.NORMAL)
                        # print(state)
                    elif state == 'normal':
                        self.canvas2.itemconfigure(self.rightArrow,
                                                   state=tk.HIDDEN)
                        # print(state)
                    self.arrowTime = self.arrowTimee
                    self.rArrowAuxx = False
                elif self.lArrowAux and self.lArrowAuxx:
                    # print('left arrow')
                    state = self.canvas2.itemconfig(self.leftArrow,
                                                    'state')[4]
                    if state == 'hidden':
                        self.canvas2.itemconfigure(self.leftArrow,
                                                   state=tk.NORMAL)
                        # print(state)
                    elif state == 'normal':
                        self.canvas2.itemconfigure(self.leftArrow,
                                                   state=tk.HIDDEN)
                        # print(state)
                    self.arrowTime = self.arrowTimee
                    self.lArrowAuxx = False


root = tk.Tk()
app = App(root)
aux = True
while aux:
    try:
        '''newPos = random.uniform(.9*app.truckPos[0], 1.1*app.truckPos[0])
        newRLPos = random.uniform(25, 50)
        app.canvas2.coords(app.truck, newPos, app.truckPos[1])
        app.canvas2.coords(app.rLane,
                           app.rLanePos[0]+newRLPos,
                           app.rLanePos[1],
                           app.rLanePos[2]+newRLPos,
                           app.rLanePos[3],
                           app.rLanePos[4]+newRLPos,
                           app.rLanePos[5])
        app.canvas2.coords(app.lLane,
                           app.lLanePos[0]-newRLPos,
                           app.lLanePos[1],
                           app.lLanePos[2]-newRLPos,
                           app.lLanePos[3],
                           app.lLanePos[4]-newRLPos,
                           app.lLanePos[5])'''
        if keyboard.is_pressed('d'):
            '''app.truckPos[0] = .73*app.hDim2
            # app.truckPos[0] += 1
            # print(app.truckPos[0])
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            # app.vAngle('inc')
            app.canvas2.itemconfig(app.rLane, fill='red')
            app.canvas2.itemconfig(app.lLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   text='Lane departure - right side')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.NORMAL)'''
            if not app.rArrowAux:
                # print('right')
                if app.lArrowAux:
                    app.lArrowAuxx = False
                    app.lArrowAux = False
                    app.canvas2.itemconfigure(app.leftArrow, state=tk.HIDDEN)
                app.rArrowAux = True
                app.arrowTime = time()
        elif keyboard.is_pressed('a'):
            '''app.truckPos[0] = .27*app.hDim2
            # app.truckPos[0] -= 1
            # print(app.truckPos[0])
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            # app.vAngle('dec')
            app.canvas2.itemconfig(app.lLane, fill='red')
            app.canvas2.itemconfig(app.rLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   text='Lane departure - left side')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.NORMAL)'''
            if not app.lArrowAux:
                # print('left')
                if app.rArrowAux:
                    app.rArrowAuxx = False
                    app.rArrowAux = False
                    app.canvas2.itemconfigure(app.rightArrow, state=tk.HIDDEN)
                app.lArrowAux = True
                app.arrowTime = time()
        elif keyboard.is_pressed('s'):
            '''app.truckPos[0] = .5*app.hDim2
            # app.truckPos[0] -= 1
            # print(app.truckPos[0])
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            app.canvas2.itemconfig(app.lLane, fill='silver')
            app.canvas2.itemconfig(app.rLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.HIDDEN)'''
            if app.rArrowAux or app.lArrowAux:
                # print('disabled')
                app.canvas2.itemconfigure(app.leftArrow, state=tk.HIDDEN)
                app.canvas2.itemconfigure(app.rightArrow, state=tk.HIDDEN)
                app.lArrowAux = False
                app.lArrowAuxx = False
                app.rArrowAux = False
                app.rArrowAuxx = False
        app.arrows('verify')
        # sleep(.1)
        root.update()
    except Exception as e:  # noqa: F841
        print(e)
        aux = False
