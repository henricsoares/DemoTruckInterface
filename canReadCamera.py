import cantools
import PCANBasic as pcb
import keyboard  # noqa: F401
from threading import Thread  # noqa: F401
from multiprocessing import Process, freeze_support  # noqa: F401
from time import sleep, time  # noqa: F401


class camera():
    def __init__(self):
        self.objPCAN = pcb.PCANBasic()
        self.TCO1_ICUC = 218000407
        self.MPC_C03 = 285147519
        self.MPC_C04 = 285147775
        self.AMB_SCA = 419362081
        self.MPC_MESS12 = 419425151
        self.db = cantools.database.load_file('truck.dbc')
        self.temp, self.vehSpeed, self.speedLim = 0, 0, 0
        self.rLane, self.lLane = 9, 9
        self.emCount = 0
        self.time1, self.time2 = 0, 0
        self.conf = False
        self.vspeedAux = False
        self.speedlAux = False
        self.lanesAux = False
        self.confAux = False
        self.tempAux = False
        self.connection = False

    def connect(self):
        result = self.objPCAN.Initialize(pcb.PCAN_USBBUS1, pcb.PCAN_BAUD_666K)
        if result != pcb.PCAN_ERROR_OK:
            result = self.objPCAN.GetErrorText(result)
            self.connection = False
            print(result[1].decode())
        else:
            result = self.objPCAN.GetErrorText(result)
            self.objPCAN.FilterMessages(pcb.PCAN_USBBUS1,
                                        self.TCO1_ICUC,
                                        self.MPC_MESS12,
                                        pcb.PCAN_MODE_EXTENDED)
            self.connection = True
            print(result[1].decode())

    def release(self):
        result = self.objPCAN.Uninitialize(pcb.PCAN_USBBUS1)
        if result != pcb.PCAN_ERROR_OK:
            result = self.objPCAN.GetErrorText(result)
            return(False, result[1].decode())
        else:
            self.connection = False
            return([True, "PCAN-USB (Ch-1) was released"])

    def read(self, info):
        if self.connection:
            if info == 'vehSpeed':
                while not self.vspeedAux:
                    msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                    if msg[0] == 0:
                        msg = msg[1]
                        if msg.ID == self.TCO1_ICUC:
                            msg = self.db.decode_message(msg.ID, msg.DATA)
                            self.vehSpeed = msg['VehSpd_Cval_ICUC']
                            if self.vehSpeed == 'SNA':
                                self.vehSpeed = 0
                            self.vspeedAux = True
                    elif msg[0] == 67108864:
                        print('No flow')
                        self.connection = False
                        self.vspeedAux = True
                    elif msg[0] == 32:
                        self.emCount += 1
                        if self.emCount > 999999:
                            print('Empty message')
                            self.vspeedAux = True
                self.emCount = 0
                self.vspeedAux = False
            elif info == 'lanes':
                while not self.lanesAux:
                    msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                    if msg[0] == 0:
                        msg = msg[1]
                        if msg.ID == self.MPC_C03:
                            msg = self.db.decode_message(msg.ID, msg.DATA)
                            self.lLane = msg['DistLaneLineLt_Cval_MPC']
                            self.rLane = msg['DistLaneLineRt_Cval_MPC']
                            if self.rLane == 'SNA' or self.lLane == 'SNA' or \
                               not self.conf:
                                self.lLane = 9
                                self.rLane = 9
                            self.lanesAux = True
                    elif msg[0] == 67108864:
                        print('No flow')
                        self.connection = False
                        self.lanesAux = True
                    elif msg[0] == 32:
                        self.emCount += 1
                        if self.emCount > 999999:
                            print('Empty message')
                            self.lanesAux = True
                self.emCount = 0
                self.lanesAux = False
            elif info == 'conf':
                while not self.confAux:
                    msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                    if msg[0] == 0:
                        msg = msg[1]
                        if msg.ID == self.MPC_C04:
                            msg = self.db.decode_message(msg.ID, msg.DATA)
                            cR = msg['ConfLaneRt_Cval_MPC']
                            cL = msg['ConfLaneLt_Cval_MPC']
                            if cR != 'SNA' and cL != 'SNA':
                                if 70 <= cR < 150 and 70 <= cL < 150:
                                    self.conf = True
                                else:
                                    self.conf = False
                            else:
                                self.conf = False
                            self.confAux = True
                    elif msg[0] == 67108864:
                        print('No flow')
                        self.connection = False
                        self.confAux = True
                    elif msg[0] == 32:
                        self.emCount += 1
                        if self.emCount > 999999:
                            print('Empty message')
                            self.confAux = True
                self.emCount = 0
                self.confAux = False
            elif info == 'temp':
                while not self.tempAux:
                    msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                    if msg[0] == 0:
                        msg = msg[1]
                        if msg.ID == self.AMB_SCA:
                            msg = self.db.decode_message(msg.ID, msg.DATA)
                            self.temp = msg['AirTempOutsd_Cval_SCA']
                            if self.temp == 'SNA':
                                self.temp = 0
                            self.tempAux = True
                    elif msg[0] == 67108864:
                        print('No flow')
                        self.connection = False
                        self.tempAux = True
                    elif msg[0] == 32:
                        self.emCount += 1
                        if self.emCount > 999999:
                            print('Empty message')
                            self.tempAux = True
                self.emCount = 0
                self.tempAux = False
            elif info == 'speedLim':
                while not self.speedlAux:
                    msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                    if msg[0] == 0:
                        msg = msg[1]
                        if msg.ID == self.MPC_MESS12:
                            msg = self.db.decode_message(msg.ID, msg.DATA)
                            self.speedLim = msg['RSF_SpeedLimit1Detected']
                            if self.speedLim == 'SNA':
                                self.temp = 0
                            self.speedlAux = True
                    elif msg[0] == 67108864:
                        print('No flow')
                        self.connection = False
                        self.speedlAux = True
                    elif msg[0] == 32:
                        self.emCount += 1
                        if self.emCount > 999999:
                            print('Empty message')
                            self.speedlAux = True
                self.emCount = 0
                self.speedlAux = False
        else:
            print('No connection')

    def keepReading(self):
        self.time1, self.time2 = -.1, -5
        while self.connection:
            if time() - self.time1 > .1:
                Thread(target=self.read, args=('vehSpeed',),
                       daemon=True).start()
                Thread(target=self.read, args=('conf',), daemon=True).start()
                Thread(target=self.read, args=('lanes',), daemon=True).start()
                Thread(target=self.read, args=('speedLim',),
                       daemon=True).start()
                self.time1 = time()
            if time() - self.time2 > 5:
                Thread(target=self.read, args=('temp',), daemon=True).start()
                self.time2 = time()


'''ap = camera()
ap.time1 = time()
while not ap.connection:
    ap.connect()
    if time() - ap.time1 > 1:
        print('.')
        ap.time1 = time()
ap.time1, ap.time2 = -.1, -5
while ap.connection:
    try:
        if time() - ap.time1 > .1:
            Thread(target=ap.read, args=('vehSpeed',), daemon=True).start()
            Thread(target=ap.read, args=('conf',), daemon=True).start()
            Thread(target=ap.read, args=('lanes',), daemon=True).start()
            Thread(target=ap.read, args=('speedLim',), daemon=True).start()
            ap.time1 = time()
        if time() - ap.time2 > 5:
            Thread(target=ap.read, args=('temp',), daemon=True).start()
            ap.time2 = time()
    except Exception as e:
        print(e)
        ap.release()'''
