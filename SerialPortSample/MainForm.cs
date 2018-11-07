using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// 定義追加
using System.IO.Ports;
using System.Threading;

namespace SerialPortSample {
	public partial class MainForm : Form {

	/*----------------------------------------------------------------------------------*/
	//																					//
	//　変数定義																		//
	//																					//
	/*----------------------------------------------------------------------------------*/

		Encoding encSjis = Encoding.GetEncoding("shift-jis");		// エンコード用
		Encoding encUni = Encoding.GetEncoding("utf-16");			// エンコード用
		List<string> PortList = new List<string>();					// シリアルポート リスト


	/*----------------------------------------------------------------------------------*/
	//																					//
	//　初期動作 (起動時)																//
	//																					//
	/*----------------------------------------------------------------------------------*/

		public MainForm() {
			InitializeComponent();

			TXbutton.Enabled = false;	// 送信ボタン Enable = off
			SerialPort_Init();			// 起動したらシリアルポート検索
		}

		// シリアルポート検索
		private bool SerialPort_Init() {
			try {
				int SelectCom = 0;
				PortList.RemoveRange(0, PortList.Count);	// リスト全削除
				ComNoComboBox.Items.Clear();
				ComNoComboBox.Text = "";
				try {
					string[] ports = SerialPort.GetPortNames();
					foreach (string port in ports) {
						ComNoComboBox.Items.Add(port);
						PortList.Add(port);
					}
				} catch { }

				if (ComNoComboBox.Items.Count > 0) {
					ComNoComboBox.SelectedIndex = SelectCom;
					BaudRateComboBox.SelectedIndex = 2;
					return true;
				} else {
					return false;
				}
			} catch {
				ComNoComboBox.Items.Clear();
				ComNoComboBox.Text = "";
				ComNoComboBox.Items.Add("読込エラー");
				ComNoComboBox.SelectedIndex = 0;
				return false;
			}
		}


	/*----------------------------------------------------------------------------------*/
	//																					//
	//　シリアルポート接続／切断処理													//
	//																					//
	/*----------------------------------------------------------------------------------*/

		// シリアルポート接続ボタン
		private void ConnectButton_Click(object sender, EventArgs e) {
			if (PortConnection(PortList[ComNoComboBox.SelectedIndex], int.Parse(BaudRateComboBox.Text))) {
				ConnectButton.Enabled = false;
				ComNoComboBox.Enabled = false;
				BaudRateComboBox.Enabled = false;
				TXbutton.Enabled = true;
			}
		}

		// 画面が閉じる際はシリアルポート切断
		private void MainForm_FormClosed(object sender, FormClosedEventArgs e) {
			PortNonConnection();
		}

		// シリアルポート接続
		private bool PortConnection(string _com, int _baudrate) {
			if (!serialPort.IsOpen) {
				serialPort.PortName = _com;
				serialPort.BaudRate = _baudrate;
				serialPort.Parity = Parity.None;
				serialPort.DataBits = 8;
				serialPort.StopBits = StopBits.One;
				serialPort.Handshake = Handshake.None;
				serialPort.Encoding = Encoding.Default;
				serialPort.NewLine = "\r\n";
			}

			try {
				serialPort.Open();
				serialPort.DtrEnable = true;
				serialPort.RtsEnable = true;

				serialPort.ReadTimeout = 500;
				serialPort.WriteTimeout = 500;
			} catch (Exception ex) {
				MessageBox.Show(ex.Message);
				return false;
			}

			return true;
		}

		// シリアルポート切断
		private void PortNonConnection() {
			if (serialPort.IsOpen) {
				try {
					serialPort.DiscardInBuffer();
					serialPort.Close();
				} catch { }
			}
		}


	/*----------------------------------------------------------------------------------*/
	//																					//
	//　コマンド双信／データ受信処理													//
	//																					//
	/*----------------------------------------------------------------------------------*/

		// コマンド送信ボタン
		private void TXbutton_Click(object sender, EventArgs e) {
			RXtextBox.Text = CommandSendReceive("$E");		// MC-110 エンコーダカウント値取得コマンド送信
		}

		// コマンド送信、データ受信
		private string CommandSendReceive(string Command) {
			try {
				// 送信部
				string strSend = Command;
				strSend += '\r';
				Byte[] byteArry = encSjis.GetBytes(strSend);
				serialPort.Write(byteArry, 0, byteArry.Length);

				// wait
				Thread.Sleep(50);

				// 受信部
				byte[] byteRead = new byte[serialPort.BytesToRead];
				serialPort.Read(byteRead, 0, serialPort.BytesToRead);
				byte[] byteUni = Encoding.Convert(encSjis, encUni, byteRead);
				string strUni = encUni.GetString(byteUni);

				return strUni;
			} catch {
				return "?";
			}
		}
	}
}