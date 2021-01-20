import tkinter as tk
import math
import keyboard
from time import sleep, time
from PIL import ImageTk, Image
import random  # noqa: F401
import datetime
# import canReadCamera as canrd  # noqa: F401


class App(tk.Frame):
    def __init__(self, master):
        self.now = datetime.datetime.now()
        self._time = ['{:02d}'.format(self.now.hour),
                      '{:02d}'.format(self.now.minute)]
        self.extTemp = 25
        self.tsRightAux = False
        self.tsRightAuxx = False
        self.tsLeftAux = False
        self.tsLeftAuxx = False
        self.tsTime = time()
        self.tsTimee = time()
        self.right = .91
        self.left = .91
        tk.Frame.__init__(self, master)
        master.winfo_toplevel().title("Python Interfaces")
        self.mainFrame = tk.Frame(master, background='black')
        self.mainFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
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
        self.bg = self.bg.resize((2*self.hDim2, (self.vDim2)),
                                 Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.canvas1.create_image((0, .73*self.vDim2),
                                  image=self.bg)
        self.canvas2.create_image((0, .73*self.vDim2),
                                  image=self.bg)
        self.canvas3.create_image((0, .73*self.vDim2),
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
                                                  text='',
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
        self.img = Image.open('truck.png')
        self.truckPos = [self.hDim2/2, .7*self.vDim2]
        self.img = self.img.resize((int(self.hDim2*3/10),
                                    int(self.hDim2*3/10)),
                                   Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.truckW, self.truckH = self.img.width(), self.img.height()
        self.meter = round(self.truckW/1.82, 2)
        self.ldwHolder = self.canvas2.create_text(self.hDim2/2,
                                                  self.vDim2*.45,
                                                  justify=tk.CENTER,
                                                  text='LANE DEPARTURE',
                                                  fill='red',
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
                                                     text='',
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
        self.turnSignalLeft = self.canvas2.create_polygon([.1*self.hDim2,
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
                                                          fill='SpringGreen2',
                                                          width=self.hDim2 *
                                                          .005)
        self.turnSignalRight = self.canvas2.create_polygon([.9*self.hDim2,
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
                                                           fill='SpringGreen2',
                                                           width=self.hDim2 *
                                                           .005)
        self.lLanePos = [(self.hDim2/2)-self.meter,
                         self.vDim2,
                         (self.hDim2/2)-(self.meter+.2*self.meter),
                         self.vDim2,
                         (self.hDim2/2)-(self.meter-1.4*self.meter),
                         self.vDim2/2]
        self.rLanePos = [(self.hDim2/2)+self.meter,
                         self.vDim2,
                         (self.hDim2/2)+(self.meter+.2*self.meter),
                         self.vDim2,
                         (self.hDim2/2)+(self.meter-1.4*self.meter),
                         self.vDim2/2]
        self.rLane = self.canvas2.create_polygon(self.rLanePos,
                                                 fill='silver',
                                                 width=self.hDim2*.02)
        self.lLane = self.canvas2.create_polygon(self.lLanePos,
                                                 fill='silver',
                                                 width=self.hDim2*.02)
        self.canvas2.create_polygon([1.18*self.hDim2,
                                     self.vDim2,
                                     1.16*self.hDim2,
                                     self.vDim2,
                                     .8*self.hDim2,
                                     self.vDim2/2],
                                    fill='white')
        self.canvas2.create_polygon([-.18*self.hDim2,
                                     self.vDim2,
                                     -.16*self.hDim2,
                                     self.vDim2,
                                     .2*self.hDim2,
                                     self.vDim2/2],
                                    fill='white')
        self.canvas3.create_polygon([.18*self.hDim2,
                                     self.vDim2,
                                     .16*self.hDim2,
                                     self.vDim2,
                                     -.2*self.hDim2,
                                     self.vDim2/2],
                                    fill='white')
        self.canvas1.create_polygon([.59*self.hDim2,
                                     self.vDim2,
                                     .57*self.hDim2,
                                     self.vDim2,
                                     .951*self.hDim2,
                                     self.vDim2/2],
                                    fill='white')
        self.canvas2.create_line([0, self.vDim2/2, self.hDim2,
                                 self.vDim2/2], fill='white', width=1)
        # self.canvas2.create_line(self.points, fill='white', width=2)
        self.truck = self.canvas2.create_image(self.truckPos,
                                               image=self.img)
        self.clock = self.canvas2.create_text(.25*self.hDim2,
                                              .05*self.vDim2,
                                              fill='white',
                                              text=self._time[0] +
                                                   ":"+self._time[1],
                                              font=('Helvetica',
                                                    '18'))
        self.extTempHolder = self.canvas2.create_text(.75*self.hDim2,
                                                      .05*self.vDim2,
                                                      fill='white',
                                                      text=str(self.extTemp) +
                                                           ' ºC',
                                                      font=('Helvetica',
                                                            '18'))
        self.canvas2.itemconfigure(self.velSign, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignValue, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignUnit, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.rLane, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.lLane, state=tk.HIDDEN)
        # self.canvas2.itemconfigure(self.truck, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.turnSignalLeft, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.turnSignalRight, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.ldwHolder, state=tk.HIDDEN)

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
            self.master.update()
            self.angle += 1.8
            round(self.angle, 1)
        elif op == 'dec' and self.angle >= 1.7:
            self.pointsP1 = self.rotate(self.pointsP1, -1.8,
                                        [(self.hDim/2), (self.vDim/2)])
            self.canvas1.coords(self.p1, self.pointsP1[0][0],
                                self.pointsP1[0][1],
                                self.pointsP1[1][0],
                                self.pointsP1[1][1])
            self.master.update()
            self.angle -= 1.8
            round(self.angle, 1)
            if not (0 <= self.angle <= 288):
                if self.angle < 0:
                    self.angle = 0
                elif self.angle > 288:
                    self.angle = 288

    def turnSigns(self):
        if self.tsRightAux or self.tsLeftAux:
            self.tsTimee = time()
            if (self.tsTimee - self.tsTime) >= .5:
                if self.tsRightAux:
                    self.tsRightAuxx = True
                elif self.tsLeftAux:
                    self.tsLeftAuxx = True
            if self.tsRightAux and self.tsRightAuxx:
                state = self.canvas2.itemconfig(self.turnSignalRight,
                                                'state')[4]
                if state == 'hidden':
                    self.canvas2.itemconfigure(self.turnSignalRight,
                                               state=tk.NORMAL)
                elif state == 'normal':
                    self.canvas2.itemconfigure(self.turnSignalRight,
                                               state=tk.HIDDEN)
                self.tsTime = self.tsTimee
                self.tsRightAuxx = False
            elif self.tsLeftAux and self.tsLeftAuxx:
                state = self.canvas2.itemconfig(self.turnSignalLeft,
                                                'state')[4]
                if state == 'hidden':
                    self.canvas2.itemconfigure(self.turnSignalLeft,
                                               state=tk.NORMAL)
                elif state == 'normal':
                    self.canvas2.itemconfigure(self.turnSignalLeft,
                                               state=tk.HIDDEN)
                self.tsTime = self.tsTimee
                self.tsLeftAuxx = False

    def updateInfo(self):
        self.now = datetime.datetime.now()
        self._time = ['{:02d}'.format(self.now.hour),
                      '{:02d}'.format(self.now.minute)]
        self.canvas2.itemconfig(app.clock,
                                text=app._time[0] +
                                ":"+app._time[1])
        self.canvas1.itemconfigure(self.velHolder,
                                   text=int(self.velValue))
        while self.velValue > self.angle/1.8:
            self.vAngle('inc')
        while self.velValue < self.angle/1.8:
            self.vAngle('dec')

    def moveLanes(self, right, left):
        if left > 0 > right:
            right, left = left, right
        if left < 0 < right:
            self.right, self.left = right, left
            ampl = (abs(left)+right+(self.truckW/self.meter)) / 2
            self.truckPos[0] = ((ampl - right)*self.meter) + \
                               ((self.hDim2/2) - (self.truckW/2))
            right, left = ampl * self.meter, -ampl * self.meter
            self.lLanePos = [.5*self.hDim2 + left,
                             self.vDim2,
                             .5*self.hDim2 + left - .2*self.meter,
                             self.vDim2,
                             .5*self.hDim2 + left + 1.4*self.meter,
                             .5*self.vDim2]
            self.rLanePos = [.5*self.hDim2 + right,
                             self.vDim2,
                             .5*self.hDim2 + right + .2*self.meter,
                             self.vDim2,
                             .5*self.hDim2 + right - 1.4*self.meter,
                             .5*self.vDim2]
            self.canvas2.coords(self.rLane,
                                self.rLanePos[0],
                                self.rLanePos[1],
                                self.rLanePos[2],
                                self.rLanePos[3],
                                self.rLanePos[4],
                                self.rLanePos[5])
            self.canvas2.coords(self.lLane,
                                self.lLanePos[0],
                                self.lLanePos[1],
                                self.lLanePos[2],
                                self.lLanePos[3],
                                self.lLanePos[4],
                                self.lLanePos[5])
            self.canvas2.coords(self.truck, self.truckPos[0], self.truckPos[1])
            self.canvas2.itemconfigure(self.rLane, state=tk.NORMAL)
            self.canvas2.itemconfigure(self.lLane, state=tk.NORMAL)
            # self.canvas2.itemconfigure(self.truck, state=tk.NORMAL)
        else:
            self.canvas2.itemconfigure(self.rLane, state=tk.HIDDEN)
            self.canvas2.itemconfigure(self.lLane, state=tk.HIDDEN)
            # self.canvas2.itemconfigure(self.truck, state=tk.HIDDEN)
            self.truckPos[0] = self.hDim2/2
            self.canvas2.coords(self.truck, self.truckPos[0], self.truckPos[1])

    def ldw(self):
        '''ldwR = self.rLanePos[0]
        ldwL = self.lLanePos[0]
        tRightEdge = self.truckPos[0] - .5*self.truck
        tLeftEdge = self.truckPos[0] - .5*self.truckW'''
        if self.right <= .05:
            self.canvas2.itemconfig(self.rLane, fill='red')
            self.canvas2.itemconfigure(self.ldwHolder, state=tk.NORMAL)
        elif self.left >= -.05:
            self.canvas2.itemconfig(self.lLane, fill='red')
            self.canvas2.itemconfigure(self.ldwHolder, state=tk.NORMAL)
        else:
            self.canvas2.itemconfig(self.lLane, fill='silver')
            self.canvas2.itemconfig(self.rLane, fill='silver')
            self.canvas2.itemconfigure(self.ldwHolder, state=tk.HIDDEN)
        # print(ldwR, tRightEdge, ldwL, tLeftEdge)


'''conection = (canrd.connect())
while not conection[0]:
    print('Trying to connect...')
    conection = (canrd.connect())
    sleep(1)
print(conection[1])
conection = conection[0]'''
root = tk.Tk()
app = App(root)
aux = True
while aux:
    try:
        app.velValue = random.uniform(80, 85)
        right = random.uniform(1, 1.15)
        left = random.uniform(-.06, -.03)
        # right, left = float(input('right: ')), float(input('left: '))
        app.moveLanes(right, left)
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
            pass
            '''app.truckPos[0] = .73*app.hDim2
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            app.canvas2.itemconfig(app.rLane, fill='red')
            app.canvas2.itemconfig(app.lLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   text='Lane departure - right side')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.NORMAL)'''
            if not app.tsRightAux:
                # print('right')
                if app.tsLeftAux:
                    app.tsLeftAuxx = False
                    app.tsLeftAux = False
                    app.canvas2.itemconfigure(app.turnSignalLeft,
                                              state=tk.HIDDEN)
                app.tsRightAux = True
                app.tsTime = time()
        elif keyboard.is_pressed('a'):
            pass
            '''app.truckPos[0] = .27*app.hDim2
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            app.canvas2.itemconfig(app.lLane, fill='red')
            app.canvas2.itemconfig(app.rLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   text='Lane departure - left side')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.NORMAL)'''
            if not app.tsLeftAux:
                # print('left')
                if app.tsRightAux:
                    app.tsRightAuxx = False
                    app.tsRightAux = False
                    app.canvas2.itemconfigure(app.turnSignalRight,
                                              state=tk.HIDDEN)
                app.tsLeftAux = True
                app.tsTime = time()
        elif keyboard.is_pressed('s'):
            pass
            '''app.truckPos[0] = .5*app.hDim2
            app.canvas2.coords(app.truck, app.truckPos[0], app.truckPos[1])
            app.canvas2.itemconfig(app.lLane, fill='silver')
            app.canvas2.itemconfig(app.rLane, fill='silver')
            app.canvas2.itemconfig(app.ldwHolder,
                                   state=tk.HIDDEN)'''
            if app.tsRightAux or app.tsLeftAux:
                # print('disabled')
                app.canvas2.itemconfigure(app.turnSignalLeft, state=tk.HIDDEN)
                app.canvas2.itemconfigure(app.turnSignalRight, state=tk.HIDDEN)
                app.tsLeftAux = False
                app.tsLeftAuxx = False
                app.tsRightAux = False
                app.tsRightAuxx = False
        app.turnSigns()
        app.updateInfo()
        app.ldw()
        sleep(.15)
        root.update()
    except Exception as e:  # noqa: F841
        print(e)
        aux = False
