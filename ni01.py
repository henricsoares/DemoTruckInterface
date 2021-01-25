import tkinter as tk
import math
import keyboard
from time import sleep, time  # noqa: F401
from PIL import ImageTk, Image
import random  # noqa: F401
import datetime
import canReadCamera as canrd  # noqa: F401
from threading import Thread


class App(tk.Frame):
    def __init__(self, master):
        self.now = datetime.datetime.now()
        self._time = ['{:02d}'.format(self.now.hour),
                      '{:02d}'.format(self.now.minute)]
        self.extTemp = ''
        self.tsRightAux = False
        self.tsLeftAux = False
        self.rldwAux = False
        self.lldwAux = False
        self.rldwAuxx = False
        self.lldwAuxx = False
        self.lanesAux = False
        self.lanesAuxx = False
        self.tsTime = 0
        self.ldwTime = 0
        self.lanesTime = 0
        self.right = 1
        self.left = 1
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
        self.speedLim = 0
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
                                                      text='',
                                                      font=('Helvetica',
                                                            '18'))
        self.canvas2.itemconfigure(self.velSign, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignValue, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.velSignUnit, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.rLane, state=tk.HIDDEN)
        self.canvas2.itemconfigure(self.lLane, state=tk.HIDDEN)
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
            if (time() - self.tsTime) >= .5:
                if self.tsRightAux:
                    state = self.canvas2.itemconfig(self.turnSignalRight,
                                                    'state')[4]
                    if state == 'hidden':
                        self.canvas2.itemconfigure(self.turnSignalRight,
                                                   state=tk.NORMAL)
                    elif state == 'normal':
                        self.canvas2.itemconfigure(self.turnSignalRight,
                                                   state=tk.HIDDEN)
                    self.tsTime = time()
                elif self.tsLeftAux:
                    state = self.canvas2.itemconfig(self.turnSignalLeft,
                                                    'state')[4]
                    if state == 'hidden':
                        self.canvas2.itemconfigure(self.turnSignalLeft,
                                                   state=tk.NORMAL)
                    elif state == 'normal':
                        self.canvas2.itemconfigure(self.turnSignalLeft,
                                                   state=tk.HIDDEN)
                    self.tsTime = time()

    def updateInfo(self):
        self.now = datetime.datetime.now()
        self._time = ['{:02d}'.format(self.now.hour),
                      '{:02d}'.format(self.now.minute)]
        self.canvas2.itemconfig(app.clock,
                                text=app._time[0] +
                                ":"+app._time[1])
        self.canvas1.itemconfigure(self.velHolder,
                                   text=int(self.velValue))
        if self.extTemp > 0:
            self.canvas2.itemconfigure(self.extTempHolder,
                                       text=str(self.extTemp) + ' ºC')
        else:
            self.canvas2.itemconfigure(self.extTempHolder,
                                       text='')
        if self.speedLim > 0:
            self.canvas2.itemconfigure(self.velSignValue,
                                       text=self.speedLim)
            self.canvas2.itemconfigure(self.velSign, state=tk.NORMAL)
            self.canvas2.itemconfigure(self.velSignValue, state=tk.NORMAL)
            self.canvas2.itemconfigure(self.velSignUnit, state=tk.NORMAL)
        else:
            self.canvas2.itemconfigure(self.velSign, state=tk.HIDDEN)
            self.canvas2.itemconfigure(self.velSignValue, state=tk.HIDDEN)
            self.canvas2.itemconfigure(self.velSignUnit, state=tk.HIDDEN)
        while self.velValue > self.angle/1.8:
            self.vAngle('inc')
        while self.velValue < self.angle/1.8:
            self.vAngle('dec')

    def moveLanes(self):
        if self.left > 0 > self.right:
            self.right, self.left = self.left, self.right
        if self.left <= 0 <= self.right and self.right < 2 and self.left > -2:
            if not self.lanesAux:
                self.lanesTime = time()
                self.lanesAux = True
                self.lanesAuxx = False
            elif time() - self.lanesTime >= .5:
                ampl = (abs(self.left)+self.right+(self.truckW/self.meter)) / 2
                self.truckPos[0] = ((ampl - self.right)*self.meter) + \
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
                self.canvas2.coords(self.truck, self.truckPos[0],
                                    self.truckPos[1])
                self.canvas2.itemconfigure(self.rLane, state=tk.NORMAL)
                self.canvas2.itemconfigure(self.lLane, state=tk.NORMAL)
        else:
            if not self.lanesAuxx:
                self.lanesTime = time()
                self.lanesAuxx = True
                self.lanesAux = False
            elif time() - self.lanesTime >= .5:
                self.canvas2.itemconfigure(self.rLane, state=tk.HIDDEN)
                self.canvas2.itemconfigure(self.lLane, state=tk.HIDDEN)
                self.canvas2.itemconfigure(self.ldwHolder, state=tk.HIDDEN)
                self.truckPos[0] = self.hDim2/2
                self.canvas2.coords(self.truck, self.truckPos[0],
                                    self.truckPos[1])

    def ldw(self):
        if self.right <= .05 and not self.tsLeftAux and not self.tsRightAux:
            if not self.rldwAux:
                self.rldwAux = True
                self.rldwAuxx = False
                self.ldwTime = time()
            elif time() - self.ldwTime >= .5 and self.lanesAux:
                self.canvas2.itemconfig(self.rLane, fill='red')
                self.canvas2.itemconfigure(self.ldwHolder, state=tk.NORMAL)
        else:
            if not self.rldwAuxx:
                self.rldwAuxx = True
                self.ldwTime = time()
            elif time() - self.ldwTime >= .5:
                self.rldwAux = False
                self.canvas2.itemconfig(self.rLane, fill='silver')
                if not self.lldwAux:
                    self.canvas2.itemconfigure(self.ldwHolder, state=tk.HIDDEN)
        if self.left >= -.05 and not self.tsLeftAux and not self.tsRightAux:
            if not self.lldwAux:
                self.lldwAux = True
                self.lldwAuxx = False
                self.ldwTime = time()
            elif time() - self.ldwTime >= .5 and self.lanesAux:
                self.canvas2.itemconfig(self.lLane, fill='red')
                self.canvas2.itemconfigure(self.ldwHolder, state=tk.NORMAL)
        else:
            if not self.lldwAuxx:
                self.lldwAuxx = True
                self.ldwTime = time()
            elif time() - self.ldwTime >= .5:
                self.lldwAux = False
                self.canvas2.itemconfig(self.lLane, fill='silver')
                if not self.rldwAux:
                    self.canvas2.itemconfigure(self.ldwHolder, state=tk.HIDDEN)


root = tk.Tk()
app = App(root)

camera = canrd.camera()
camera.time1 = time()
while not camera.connection:
    camera.connect()
    if time() - camera.time1 > 1:
        print('.')
        camera.time1 = time()
Thread(target=camera.keepReading, daemon=True).start()
aux = True
while aux:
    try:
        '''app.velValue = random.uniform(80, 85)
        app.right = random.uniform(0, 0)
        app.left = random.uniform(-0, -0)'''
        if keyboard.is_pressed('d'):
            if not app.tsRightAux:
                if app.tsLeftAux:
                    app.tsLeftAux = False
                    app.canvas2.itemconfigure(app.turnSignalLeft,
                                              state=tk.HIDDEN)
                app.tsRightAux = True
                app.tsTime = time()
        elif keyboard.is_pressed('a'):
            if not app.tsLeftAux:
                if app.tsRightAux:
                    app.tsRightAux = False
                    app.canvas2.itemconfigure(app.turnSignalRight,
                                              state=tk.HIDDEN)
                app.tsLeftAux = True
                app.tsTime = time()
        elif keyboard.is_pressed('s'):
            if app.tsRightAux or app.tsLeftAux:
                app.canvas2.itemconfigure(app.turnSignalLeft, state=tk.HIDDEN)
                app.canvas2.itemconfigure(app.turnSignalRight, state=tk.HIDDEN)
                app.tsLeftAux = False
                app.tsRightAux = False
        if camera.connection:
            app.velValue = round(camera.vehSpeed, 2)
            app.extTemp = round(camera.temp, 1)
            app.speedLim = camera.speedLim
            app.left = round(camera.lLane, 2)
            app.right = round(camera.rLane, 2)
        else:
            app.velValue = 0
            app.extTemp = ''
            app.speedLim = 0
            app.left = 9
            app.right = 9
        app.moveLanes()
        app.turnSigns()
        app.updateInfo()
        app.ldw()
        sleep(.1)
        root.update()
    except Exception as e:  # noqa: F841
        print(e)
        aux = False
        camera.release()
