namespace SerialPortSample
{
	partial class MainForm
	{
		/// <summary>
		/// 必要なデザイナー変数です。
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// 使用中のリソースをすべてクリーンアップします。
		/// </summary>
		/// <param name="disposing">マネージ リソースが破棄される場合 true、破棄されない場合は false です。</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows フォーム デザイナーで生成されたコード

		/// <summary>
		/// デザイナー サポートに必要なメソッドです。このメソッドの内容を
		/// コード エディターで変更しないでください。
		/// </summary>
		private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			this.serialPort = new System.IO.Ports.SerialPort(this.components);
			this.ComNoLabel = new System.Windows.Forms.Label();
			this.BaudRateLabel = new System.Windows.Forms.Label();
			this.ComNoComboBox = new System.Windows.Forms.ComboBox();
			this.BaudRateComboBox = new System.Windows.Forms.ComboBox();
			this.ConnectButton = new System.Windows.Forms.Button();
			this.RXtextBox = new System.Windows.Forms.TextBox();
			this.TXbutton = new System.Windows.Forms.Button();
			this.SuspendLayout();
			// 
			// ComNoLabel
			// 
			this.ComNoLabel.AutoSize = true;
			this.ComNoLabel.Font = new System.Drawing.Font("MS UI Gothic", 10F);
			this.ComNoLabel.Location = new System.Drawing.Point(47, 16);
			this.ComNoLabel.Name = "ComNoLabel";
			this.ComNoLabel.Size = new System.Drawing.Size(47, 14);
			this.ComNoLabel.TabIndex = 28;
			this.ComNoLabel.Text = "COM ：";
			// 
			// BaudRateLabel
			// 
			this.BaudRateLabel.Font = new System.Drawing.Font("MS UI Gothic", 10F);
			this.BaudRateLabel.Location = new System.Drawing.Point(12, 39);
			this.BaudRateLabel.Name = "BaudRateLabel";
			this.BaudRateLabel.Size = new System.Drawing.Size(82, 21);
			this.BaudRateLabel.TabIndex = 29;
			this.BaudRateLabel.Text = "ボーレート ：";
			this.BaudRateLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// ComNoComboBox
			// 
			this.ComNoComboBox.DropDownWidth = 84;
			this.ComNoComboBox.Font = new System.Drawing.Font("MS UI Gothic", 10F);
			this.ComNoComboBox.FormattingEnabled = true;
			this.ComNoComboBox.Location = new System.Drawing.Point(96, 13);
			this.ComNoComboBox.Name = "ComNoComboBox";
			this.ComNoComboBox.Size = new System.Drawing.Size(112, 21);
			this.ComNoComboBox.TabIndex = 30;
			// 
			// BaudRateComboBox
			// 
			this.BaudRateComboBox.Font = new System.Drawing.Font("MS UI Gothic", 10F);
			this.BaudRateComboBox.FormattingEnabled = true;
			this.BaudRateComboBox.Items.AddRange(new object[] {
            "9600",
            "19200",
            "38400",
            "57600"});
			this.BaudRateComboBox.Location = new System.Drawing.Point(96, 39);
			this.BaudRateComboBox.Name = "BaudRateComboBox";
			this.BaudRateComboBox.Size = new System.Drawing.Size(112, 21);
			this.BaudRateComboBox.TabIndex = 31;
			// 
			// ConnectButton
			// 
			this.ConnectButton.Font = new System.Drawing.Font("MS UI Gothic", 12F);
			this.ConnectButton.Location = new System.Drawing.Point(225, 12);
			this.ConnectButton.Name = "ConnectButton";
			this.ConnectButton.Size = new System.Drawing.Size(99, 48);
			this.ConnectButton.TabIndex = 32;
			this.ConnectButton.Text = "接続";
			this.ConnectButton.UseVisualStyleBackColor = true;
			this.ConnectButton.Click += new System.EventHandler(this.ConnectButton_Click);
			// 
			// RXtextBox
			// 
			this.RXtextBox.BackColor = System.Drawing.SystemColors.Info;
			this.RXtextBox.Font = new System.Drawing.Font("MS UI Gothic", 12F);
			this.RXtextBox.Location = new System.Drawing.Point(15, 85);
			this.RXtextBox.Multiline = true;
			this.RXtextBox.Name = "RXtextBox";
			this.RXtextBox.ReadOnly = true;
			this.RXtextBox.Size = new System.Drawing.Size(193, 52);
			this.RXtextBox.TabIndex = 34;
			// 
			// TXbutton
			// 
			this.TXbutton.Font = new System.Drawing.Font("MS UI Gothic", 12F);
			this.TXbutton.Location = new System.Drawing.Point(225, 85);
			this.TXbutton.Name = "TXbutton";
			this.TXbutton.Size = new System.Drawing.Size(99, 52);
			this.TXbutton.TabIndex = 35;
			this.TXbutton.Text = "送信";
			this.TXbutton.UseVisualStyleBackColor = true;
			this.TXbutton.Click += new System.EventHandler(this.TXbutton_Click);
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(347, 151);
			this.Controls.Add(this.TXbutton);
			this.Controls.Add(this.RXtextBox);
			this.Controls.Add(this.ConnectButton);
			this.Controls.Add(this.ComNoLabel);
			this.Controls.Add(this.BaudRateLabel);
			this.Controls.Add(this.ComNoComboBox);
			this.Controls.Add(this.BaudRateComboBox);
			this.Name = "MainForm";
			this.Text = "SerialPortSample";
			this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.MainForm_FormClosed);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.IO.Ports.SerialPort serialPort;
		private System.Windows.Forms.Label ComNoLabel;
		private System.Windows.Forms.Label BaudRateLabel;
		private System.Windows.Forms.ComboBox ComNoComboBox;
		private System.Windows.Forms.ComboBox BaudRateComboBox;
		private System.Windows.Forms.Button ConnectButton;
		private System.Windows.Forms.TextBox RXtextBox;
		private System.Windows.Forms.Button TXbutton;
	}
}

