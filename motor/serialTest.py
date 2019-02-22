'''
シリアルポートは予めどこのモータが対応しているかを決め打ちする。
モータとドライバの組み合わせを固定して，シリアルナンバーから特定してもいいかも。
'''

# 各種ライブラリ
import serial   # シリアル通信用


# --- シリアル通信用諸元 --- #
# 肩モータ(1番)
shoulderMotorCOM = 'COM'
# 腕回転モータ(2番)
armRotateMotorCOM = 'COM'
# 肘モータ(3番)
elbowMotorCOM = 'COM'
# 手握り込み巻取り用モータ(4番)
handMotorCOM = 'COM'
# 手首折り曲げモータ(5番)
wristMotorCOM = 'COM'
# モータボーレート
motorBaudrate = 38400
# 読み取り待機時間
readTimeout = 0.1 

class moveMotor():
    def __init__(self):
        try:
            # シリアル接続
            shoulder  = serial.Serial(shoulderMotorCOM, motorBaudrate, readTimeout)
            armRotate = serial.Serial(armRotateMotorCOM, motorBaudrate, readTimeout)
            elbow     = serial.Serial(elbowMotorCOM, motorBaudrate, readTimeout)
            hand      = serial.Serial(handMotorCOM, motorBaudrate, readTimeout)
            wrist     = serial.Serial(wristMotorCOM, motorBaudrate, readTimeout)

            # 接続確認(バージョン情報取得)
            shoulder.write('$V\r\n'.encode())     # バイト型に変換，CR+LFで改行コードを送信(CRで十分だけど)
            s_v = shoulder.readline().decode()    # 接続が正常ならバージョン情報が帰ってくるはず
            armRotate.write('$V\r\n'.encode())
            a_v = armRotate.readline().decode()
            elbow.write('$V\r\n'.encode())
            e_v = elbow.readline().decode()
            hand.write('$V\r\n'.encode())
            h_v = hand.readline().decode()
            wrist.write('$V\r\n'.encode())
            w_v = wrist.readline().decode()

            # 接続失敗時のログ出力処理
            if(s_v == None):
                print(shoulderMotorCOM, "[ERROR!] : 肩モータ接続失敗\n")
                raise Exception
            if(a_v == None):
                print(armRotateMotorCOM, "[ERROR!] : 腕回転モータ接続失敗\n")
                raise Exception
            if(e_v == None):
                print(elbowMotorCOM, "[ERROR!] : 肘モータ接続失敗\n")
                raise Exception
            if(h_v == None):
                print(handMotorCOM, "[ERROR!] : 手握り込み用巻取りモータ接続失敗\n")
                raise Exception
            if(w_v == None):
                print(wristMotorCOM, "[ERROR!] : 手首用モータ接続失敗\n")
                raise Exception

        except:
            print("[ERROR!] : COMポート接続時にエラーが発生しました。\n")
            exit()

    def servoON(self, motorNum):
        if(motorNum == 1):
            self.shoulder.write('&O\r\n'.encode())
            tmp = self.shoulder.readline().decode()
            self.shoulder.write('&X\r\n'.encode())
            tmp2 = self.shoulder.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 肩モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 2):
            self.armRotate.write('&O\r\n'.encode())
            tmp = self.armRotate.readline().decode()
            self.armRotate.write('&X\r\n'.encode())
            tmp2 = self.armRotate.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 腕回転モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 3):
            self.elbow.write('&O\r\n'.encode())
            tmp = self.elbow.readline().decode()
            self.elbow.write('&X\r\n'.encode())
            tmp2 = self.elbow.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 肘モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 4):
            self.hand.write('&O\r\n'.encode())
            tmp = self.hand.readline().decode()
            self.hand.write('&X\r\n'.encode())
            tmp2 = self.hand.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 手握り込み用巻取りモータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 5):
            self.wrist.write('&O\r\n'.encode())
            tmp = self.wrist.readline().decode()
            self.wrist.write('&X\r\n'.encode())
            tmp2 = self.wrist.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 手首モータのサーボをONにできませんでした。\n")
                return False
            return True
        else:
            print("[ INFO ] : サーボON時のモータ番号指定が不正です。\n")
            return False
    
    def rotateMotor(self, motorNum, mode, speed, rotateTime):
        if(mode == 'CW'):
            if(motorNum == 1):
                self.shoulder.write('$J %d\r\n'%speed.encode())
                self.shoulder.write('+\r\n'.encode())
                sleep(rotateTime)
                self.shoulder.write('$J 0\r\n'.encode())
                self.shoulder.write('*\r\n'.encode())
            if(motorNum == 2):
                self.armRotate.write('$J %d\r\n'%speed.encode())
                self.armRotate.write('+\r\n'.encode())
                sleep(rotateTime)
                self.armRotate.write('$J 0\r\n'.encode())
                self.armRotate.write('*\r\n'.encode())
            if(motorNum == 3):
                self.elbow.write('$J %d\r\n'%speed.encode())
                self.elbow.write('+\r\n'.encode())
                sleep(rotateTime)
                self.elbow.write('$J 0\r\n'.encode())
                self.elbow.write('*\r\n'.encode())
            
            

