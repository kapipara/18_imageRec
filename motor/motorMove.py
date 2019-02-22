# 各種ライブラリ
import serial     # シリアル通信用
import time       # 時間待ち用
import threading  # 並行処理用

# --- シリアル通信用諸元 --- #
#COM番号は決め打ちやで^^
# 肩モータ(1番)  MDH7012-64800E
shoulderMotorCOM = 'COM11'  
# 腕回転モータ(2番) MDH7012-64800E
armRotateMotorCOM = 'COM12'
# 肘モータ(3番) MDH-7012-648KE
elbowMotorCOM = 'COM13'
# 手握り込み巻取り用モータ(4番) MDS-4018-6750E
handMotorCOM = 'COM10'
# 手首折り曲げモータ(5番) MDH-4018-135KE
wristMotorCOM = 'COM9'
# モータドライバ接続シリアルボーレート (標準38400)
motorBaudrate = 38400
# 読み取り待機時間
readTimeout = 0.1 

# モータ制御クラス
class moveMotor():
    # コンストラクタ (クラス生成時にシリアル通信確立，確認を行う)
    def __init__(self):
        #try:
        # シリアル接続
        self.shoulder  = serial.Serial(shoulderMotorCOM,  motorBaudrate, timeout=readTimeout)
        self.armRotate = serial.Serial(armRotateMotorCOM, motorBaudrate, timeout=readTimeout)
        self.elbow     = serial.Serial(elbowMotorCOM,     motorBaudrate, timeout=readTimeout)
        self.hand      = serial.Serial(handMotorCOM,      motorBaudrate, timeout=readTimeout)
        self.wrist     = serial.Serial(wristMotorCOM,     motorBaudrate, timeout=readTimeout)

        # 接続確認(バージョン情報取得)
        self.shoulder.write('$V\r\n'.encode())     # バイト型に変換，CR+LFで改行コードを送信(CRで十分だけど)
        s_v = self.shoulder.readline().decode()    # 接続が正常ならバージョン情報が帰ってくるはず
        self.armRotate.write('$V\r\n'.encode())
        a_v = self.armRotate.readline().decode()
        self.elbow.write('$V\r\n'.encode())
        e_v = self.elbow.readline().decode()
        self.hand.write('$V\r\n'.encode())
        h_v = self.hand.readline().decode()
        self.wrist.write('$V\r\n'.encode())
        w_v = self.wrist.readline().decode()

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
        '''
        except:
            print("[ERROR!] : COMポート接続時にエラーが発生しました。\n")
            exit()
        '''

    # 指定モータのサーボをONにする
    def servoON(self, motorNum):
        if(motorNum == 1):
            self.shoulder.write('$O\r\n'.encode())
            tmp = self.shoulder.readline().decode()
            self.shoulder.write('$X\r\n'.encode())
            tmp2 = self.shoulder.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 肩モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 2):
            self.armRotate.write('$O\r\n'.encode())
            tmp = self.armRotate.readline().decode()
            self.armRotate.write('$X\r\n'.encode())
            tmp2 = self.armRotate.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 腕回転モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 3):
            self.elbow.write('$O\r\n'.encode())
            tmp = self.elbow.readline().decode()
            self.elbow.write('$X\r\n'.encode())
            tmp2 = self.elbow.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 肘モータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 4):
            self.hand.write('$O\r\n'.encode())
            tmp = self.hand.readline().decode()
            self.hand.write('$X\r\n'.encode())
            tmp2 = self.hand.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 手握り込み用巻取りモータのサーボをONにできませんでした。\n")
                return False
            return True
        elif(motorNum == 5):
            self.wrist.write('$O\r\n'.encode())
            tmp = self.wrist.readline().decode()
            self.wrist.write('$X\r\n'.encode())
            tmp2 = self.wrist.readline().decode()
            if(tmp == None or tmp2 == None):
                print("[ INFO ] : 手首モータのサーボをONにできませんでした。\n")
                return False
            return True
        else:
            print("[ INFO ] : サーボON時のモータ番号指定が不正です。\n")
            return False
    
    # モータ回転関数 (モータ番号，回転モード，回転速度，回転時間を指定)
    def rotateMotor(self, motorNum, mode, speed, rotateTime):
        if(mode == 'CW'):
            if(motorNum == 1):
                self.shoulder.write(('$J'+str(speed)+'\r\n').encode())
                self.shoulder.write('+\r\n'.encode())
                time.sleep(rotateTime)
                self.shoulder.write('$J0\r\n'.encode())
                self.shoulder.write('*\r\n'.encode())
            if(motorNum == 2):
                self.armRotate.write(('$J'+str(speed)+'\r\n').encode())
                self.armRotate.write('+\r\n'.encode())
                time.sleep(rotateTime)
                self.armRotate.write('$J0\r\n'.encode())
                self.armRotate.write('*\r\n'.encode())
            if(motorNum == 3):
                self.elbow.write(('$J'+str(speed)+'\r\n').encode())
                self.elbow.write('+\r\n'.encode())
                time.sleep(rotateTime)
                self.elbow.write('$J0\r\n'.encode())
                self.elbow.write('*\r\n'.encode())
            if(motorNum == 4):
                self.hand.write(('$J'+str(speed)+'\r\n').encode())
                self.hand.write('+\r\n'.encode())
                time.sleep(rotateTime)
                self.hand.write('$J0\r\n'.encode())
                self.hand.write('*\r\n'.encode())
            if(motorNum == 5):
                self.wrist.write(('$J'+str(speed)+'\r\n').encode())
                self.wrist.write('+\r\n'.encode())
                time.sleep(rotateTime)
                self.wrist.write('$J0\r\n'.encode())
                self.wrist.write('*\r\n'.encode())

        elif(mode == 'CCW'):
            if(motorNum == 1):
                self.shoulder.write(('$J'+str(speed)+'\r\n').encode())
                self.shoulder.write('-\r\n'.encode())
                time.sleep(rotateTime)
                self.shoulder.write('$J0\r\n'.encode())
                self.shoulder.write('*\r\n'.encode())
            if(motorNum == 2):
                self.armRotate.write(('$J'+str(speed)+'\r\n').encode())
                self.armRotate.write('-\r\n'.encode())
                time.sleep(rotateTime)
                self.armRotate.write('$J0\r\n'.encode())
                self.armRotate.write('*\r\n'.encode())
            if(motorNum == 3):
                self.elbow.write(('$J'+str(speed)+'\r\n').encode())
                self.elbow.write('-\r\n'.encode())
                time.sleep(rotateTime)
                self.elbow.write('$J0\r\n'.encode())
                self.elbow.write('*\r\n'.encode())
            if(motorNum == 4):
                self.hand.write(('$J'+str(speed)+'\r\n').encode())
                self.hand.write('-\r\n'.encode())
                time.sleep(rotateTime)
                self.hand.write('$J0\r\n'.encode())
                self.hand.write('*\r\n'.encode())
            if(motorNum == 5):
                self.wrist.write(('$J'+str(speed)+'\r\n').encode())
                self.wrist.write('-\r\n'.encode())
                time.sleep(rotateTime)
                self.wrist.write('$J0\r\n'.encode())
                self.wrist.write('*\r\n'.encode())

        elif(mode == 'STOP'):
            if(motorNum == 1):
                self.shoulder.write('$Q\r\n'.encode())
            if(motorNum == 2):
                self.armRotate.write('$Q\r\n'.encode())
            if(motorNum == 3):
                self.elbow.write('$Q\r\n'.encode())
            if(motorNum == 4):
                self.hand.write('$Q\r\n'.encode())
            if(motorNum == 5):
                self.wrist.write('$Q\r\n'.encode())
            
        else:
            print("[ INFO ] : MODEの指定が間違っているため，回転動作は行えていません。\n")
    
    def emergency(self): #緊急回避 for sabbat of the witch
        self.shoulder.write('$F\r\n'.encode())
        self.armRotate.write('$F\r\n'.encode())
        self.elbow.write('$F\r\n'.encode())
        self.hand.write('$F\r\n'.encode())
        self.wrist.write('$F\r\n'.encode())

    def getpos(self,motorNum):  #エンコーダの現在位置，指令位値の取得
        if(motorNum == 1):
            self.shoulder.write('$E\r\n'.encode())
            enc = self.shoulder.readline().decode()
            self.shoulder.write('$R\r\n'.encode())
            cmd = self.shoulder.readline().decode()
        if(motorNum == 2):
            self.armRotate.write('$E\r\n'.encode())
            enc = self.armRotate.readline().decode()
            self.armRotate.write('$R\r\n'.encode())
            cmd = self.armRotate.readline().decode()
        if(motorNum == 3):
            self.elbow.write('$E\r\n'.encode())
            enc = self.elbow.readline().decode()
            self.elbow.write('$R\r\n'.encode())
            cmd = self.elbow.readline().decode()
        if(motorNum == 4):
            self.hand.write('$E\r\n'.encode())
            enc = self.hand.readline().decode()
            self.hand.write('$R\r\n'.encode())
            cmd = self.hand.readline().decode()
        if(motorNum == 5):
            self.wrist.write('$E\r\n'.encode())
            enc = self.wrist.readline().decode()
            self.wrist.write('$R\r\n'.encode())
            cmd = self.wrist.readline().decode()
        print('エンコーダ位置:'+str(enc))
        print('指令位置'+str(cmd))
        if(motorNum == 5):
            self.wrist.close()
    
    # デストラクタ (main文のexcept内で実行，全シリアルポートを破棄)
    def __del_(self):
        self.shoulder.close()
        self.armRotate.close()
        self.elbow.close()
        self.hand.close()
        self.wrist.close()

if __name__ == '__main__':
    m = moveMotor()
    
    m.servoON(1)
    m.servoON(2)
    m.servoON(3)
    m.servoON(4)
    m.servoON(5)

    m.rotateMotor(1, 'CW', 100, 5)
    m.rotateMotor(2, 'CW',   5, 5)
    m.rotateMotor(3, 'CW',  80, 5)
    m.rotateMotor(4, 'CW',   5, 5)
    m.rotateMotor(5, 'CW',   2, 5)
    m.emergency()

    print("move Ended.\n")