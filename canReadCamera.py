import cantools
import PCANBasic as pcb
import keyboard  # noqa: F401
from threading import Thread  # noqa: F401
from time import sleep, time  # noqa: F401


class camera():
    def __init__(self):
        self.objPCAN = pcb.PCANBasic()
        self.ids = [218000407,  # TCO1_ICUC
                    285147519,  # MPC_C03
                    285147775,  # MPC_C04
                    419362081,  # AMB_SCA
                    419425151]  # MPC_MESS12
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
        self.msgPresent = False

    def connect(self):
        result = self.objPCAN.Initialize(pcb.PCAN_USBBUS1, pcb.PCAN_BAUD_666K)
        if result != pcb.PCAN_ERROR_OK:
            result = self.objPCAN.GetErrorText(result)
            self.connection = False
            print(result[1].decode())
        else:
            result = self.objPCAN.GetErrorText(result)
            self.objPCAN.FilterMessages(pcb.PCAN_USBBUS1,
                                        self.ids[0],
                                        self.ids[-1],
                                        pcb.PCAN_MODE_EXTENDED)
            self.connection = True
            print(result[1].decode())

    def release(self):
        result = self.objPCAN.Uninitialize(pcb.PCAN_USBBUS1)
        if result != pcb.PCAN_ERROR_OK:
            result = self.objPCAN.GetErrorText(result)
            print(result[1].decode())
        else:
            self.connection = False
            print("PCAN-USB (Ch-1) was released")

    def reading(self):
        while self.connection:
            try:
                msg = self.objPCAN.Read(pcb.PCAN_USBBUS1)
                if msg[0] == 0:
                    msg = msg[1]
                    if msg.ID in self.ids:
                        self.handleMsg(msg)
                        Thread(target=self.handleMsg, args=(msg,),
                               daemon=True).start()
                        self.emCount = 0
                        self.msgPresent = True
                elif msg[0] == 67108864:
                    print('No flow')
                    self.msgPresent = False
                elif msg[0] == 32:
                    self.emCount += 1
                    if self.emCount > 999999:
                        print('Empty message')
                        self.msgPresent = False
            except Exception as e:
                print(e)
        print('no connection')

    def handleMsg(self, msg):
        if msg.ID == self.ids[0]:  # vehicle speed
            msg = self.db.decode_message(msg.ID, msg.DATA)
            self.vehSpeed = msg['VehSpd_Cval_ICUC']
            if self.vehSpeed == 'SNA':
                self.vehSpeed = 0
        elif msg.ID == self.ids[1]:  # lanes distance
            msg = self.db.decode_message(msg.ID, msg.DATA)
            self.lLane = msg['DistLaneLineLt_Cval_MPC']
            self.rLane = msg['DistLaneLineRt_Cval_MPC']
            if self.rLane == 'SNA' or self.lLane == 'SNA' or \
               not self.conf:
                self.lLane = 9
                self.rLane = 9
            else:
                self.lLane, self.rLane = -self.lLane, \
                                            -self.rLane
        elif msg.ID == self.ids[2]:  # confidence lane value
            msg = self.db.decode_message(msg.ID, msg.DATA)
            cR = msg['ConfLaneRt_Cval_MPC']
            cL = msg['ConfLaneLt_Cval_MPC']
            self.conf = False
            if cR != 'SNA' and cL != 'SNA':
                if 70 <= cR < 150 and 70 <= cL < 150:
                    self.conf = True
        elif msg.ID == self.ids[3]:  # air temperature outside
            msg = self.db.decode_message(msg.ID, msg.DATA)
            self.temp = msg['AirTempOutsd_Cval_SCA']
            if self.temp == 'SNA':
                self.temp = 0
        elif msg.ID == self.ids[4]:  # speed limit detected
            msg = self.db.decode_message(msg.ID, msg.DATA)
            self.speedLim = msg['RSF_SpeedLimit1Detected']
            if self.speedLim == 'SNA':
                self.temp = 0


'''ap = camera()
time1 = time()
while not ap.connection:
    ap.connect()
    if time() - time1 > 1:
        print('.')
        time1 = time()
Thread(target=ap.reading, daemon=True).start()
while True:
    print(ap.vehSpeed, ap.speedLim, ap.temp,
          ap.rLane, ap.lLane)
    sleep(1)
ap.release()'''
