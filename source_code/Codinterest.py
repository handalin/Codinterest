# -*- coding:utf8 -*-
import wx
from RSA import *
import sys
import os

myCharset = 'latin-1'

reload(sys)
sys.setdefaultencoding(myCharset)
myDir = os.getcwd()
myDir = myDir[:myDir.rfind('\\')]
myDir = myDir + '\\keys'

class RSA_frame(wx.Frame):

    def __init__(self):
        self.key_length = 256
        wx.Frame.__init__(self, None, -1, "RSA-Toy", size=(750, 650) )
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('#ADADAD')

        # Init BoxSizers ###################
        V_Box = wx.BoxSizer(wx.VERTICAL)
        Alice_Static_Box = wx.StaticBox(self.panel, -1, 'My Keys')
        Bob_Static_Box = wx.StaticBox(self.panel, -1, "Other's Public Key")
        Plain_Static_Box = wx.StaticBox(self.panel, -1, 'Send Box')
        Cipher_Static_Box = wx.StaticBox(self.panel, -1, 'Receive Box')
        
        Alice_Box = wx.StaticBoxSizer(Alice_Static_Box, wx.HORIZONTAL)
        Bob_Box = wx.StaticBoxSizer(Bob_Static_Box, wx.HORIZONTAL)
        Plain_Box = wx.StaticBoxSizer(Plain_Static_Box, wx.HORIZONTAL)
        Cipher_Box = wx.StaticBoxSizer(Cipher_Static_Box, wx.HORIZONTAL)
        Alice_Keys = wx.BoxSizer(wx.VERTICAL)
        Alice_BTNs = wx.BoxSizer(wx.VERTICAL)
        Alice_Bottom = wx.BoxSizer(wx.HORIZONTAL)
        Alice_Read_Clear = wx.BoxSizer(wx.VERTICAL)
        Plain_BTNs = wx.BoxSizer(wx.HORIZONTAL)
        Cipher_BTNs = wx.BoxSizer(wx.HORIZONTAL)
        Plain_BTNs_LEFT = wx.BoxSizer(wx.VERTICAL)
        Plain_BTNs_RIGHT = wx.BoxSizer(wx.VERTICAL)
        Cipher_BTNs_LEFT = wx.BoxSizer(wx.VERTICAL)
        Cipher_BTNs_RIGHT = wx.BoxSizer(wx.VERTICAL)
        lineP = wx.BoxSizer(wx.HORIZONTAL)
        lineQ = wx.BoxSizer(wx.HORIZONTAL)
        lineN = wx.BoxSizer(wx.HORIZONTAL)
        lineE = wx.BoxSizer(wx.HORIZONTAL)
        lineD = wx.BoxSizer(wx.HORIZONTAL)
        lineN_Bob = wx.BoxSizer(wx.HORIZONTAL)
        lineE_Bob = wx.BoxSizer(wx.HORIZONTAL)        
        Bob_Key_Box = wx.BoxSizer(wx.VERTICAL)
        # little controls ####################

        # TextCtrls
        #self.MY_P_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2)
        #self.MY_Q_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2)
        self.MY_N_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2|wx.TE_MULTILINE)
        self.MY_E_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2|wx.TE_MULTILINE)
        self.MY_D_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2|wx.TE_MULTILINE)
        self.OTHER_N_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2)
        self.OTHER_E_Box = wx.TextCtrl(self.panel, style=wx.TE_RICH2)
        self.Send_Box = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE|wx.TE_RICH2)
        self.Receive_Box = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE|wx.TE_RICH2)
        
        # StaticTexts
        #TEXT_MY_P = wx.StaticText( self.panel, -1, 'P:')
        #TEXT_MY_Q = wx.StaticText( self.panel, -1, 'Q:')
        TEXT_MY_N = wx.StaticText( self.panel, -1, 'N:')
        TEXT_MY_E = wx.StaticText( self.panel, -1, 'E:')
        TEXT_MY_D = wx.StaticText( self.panel, -1, 'D:')
        
        TEXT_OTHER_N = wx.StaticText( self.panel, -1, 'N:')
        TEXT_OTHER_E = wx.StaticText( self.panel, -1, 'E:')
        
        # Buttons
        self.Gen_BTN = wx.Button(self.panel, -1, label='Generate Keys')
        self.Read_BTN = wx.Button(self.panel, -1, label='Load')
        self.Write_BTN = wx.Button(self.panel, -1, label='Save')
        self.Clear_BTN = wx.Button(self.panel, -1, label='Clear')
        self.Load_Key_BTN = wx.Button(self.panel, -1, label='Load')
        self.Encrypt_BTN = wx.Button(self.panel, -1, label='Encrypt')
        self.Decrypt_BTN = wx.Button(self.panel, -1, label='Decrypt')
        self.Sign_BTN = wx.Button(self.panel, -1, label='Sign')
        self.Validate_BTN = wx.Button(self.panel, -1, label='Validate')
        self.Load_Plain_BTN = wx.Button(self.panel, -1, label='Load')
        self.Load_Cipher_BTN = wx.Button(self.panel, -1, label='Load')
        self.Save_Plain_BTN = wx.Button(self.panel, -1, label='Save')
        self.Save_Cipher_BTN = wx.Button(self.panel, -1, label='Save')
        # Radio
        self.Chose_Radio = wx.RadioBox(self.panel, -1, 'Key Length', (0,0), wx.DefaultSize, \
                    ['256', '512', '1024'], 1, wx.RA_SPECIFY_COLS)
        
        # Set BoxSizers ###################
        #lineP.Add( TEXT_MY_P, proportion = 1, flag = wx.EXPAND)
        #lineP.Add( self.MY_P_Box, proportion = 17, flag = wx.EXPAND)
        #lineQ.Add( TEXT_MY_Q, proportion = 1, flag = wx.EXPAND)
        #lineQ.Add( self.MY_Q_Box, proportion = 17, flag = wx.EXPAND)
        lineN.Add( TEXT_MY_N, proportion = 1, flag = wx.EXPAND)
        lineN.Add( self.MY_N_Box, proportion = 17, flag = wx.EXPAND)
        lineE.Add( TEXT_MY_E, proportion = 1, flag = wx.EXPAND)
        lineE.Add( self.MY_E_Box, proportion = 17, flag = wx.EXPAND)
        lineD.Add( TEXT_MY_D, proportion = 1, flag = wx.EXPAND)
        lineD.Add( self.MY_D_Box, proportion = 17, flag = wx.EXPAND)
        #Alice_Keys.Add( lineP, proportion = 1, flag = wx.EXPAND)
        #Alice_Keys.Add( lineQ, proportion = 1, flag = wx.EXPAND)
        Alice_Keys.Add( lineN, proportion = 1, flag = wx.EXPAND)
        Alice_Keys.Add( lineE, proportion = 1, flag = wx.EXPAND)
        Alice_Keys.Add( lineD, proportion = 1, flag = wx.EXPAND)

        Alice_Read_Clear.Add( self.Read_BTN, proportion = 1, flag = wx.EXPAND|wx.ALL, border=5)
        Alice_Read_Clear.Add( self.Write_BTN, proportion = 1, flag = wx.EXPAND|wx.ALL, border=5)
        Alice_Read_Clear.Add( self.Clear_BTN, proportion = 1, flag = wx.EXPAND|wx.ALL, border=5)
        Alice_Bottom.Add( Alice_Read_Clear, proportion = 2, flag = wx.EXPAND|wx.ALL, border=10)
        Alice_Bottom.Add( self.Chose_Radio, proportion = 2, flag = wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, border=10)
        Alice_BTNs.Add( self.Gen_BTN, proportion = 2, flag = wx.EXPAND|wx.ALL, border=10)
        Alice_BTNs.Add( Alice_Bottom, proportion = 5, flag = wx.EXPAND)
        Alice_Box.Add( Alice_Keys, proportion = 6, flag = wx.EXPAND)
        Alice_Box.Add( Alice_BTNs, proportion = 2, flag = wx.EXPAND)

        lineN_Bob.Add( TEXT_OTHER_N, proportion = 1, flag = wx.EXPAND)
        lineN_Bob.Add( self.OTHER_N_Box, proportion = 17, flag = wx.EXPAND)
        lineE_Bob.Add( TEXT_OTHER_E, proportion = 1, flag = wx.EXPAND)
        lineE_Bob.Add( self.OTHER_E_Box, proportion = 17, flag = wx.EXPAND)
        Bob_Key_Box.Add( lineN_Bob, proportion = 1, flag = wx.EXPAND)
        Bob_Key_Box.Add( lineE_Bob, proportion = 1, flag = wx.EXPAND)
        Bob_Box.Add( Bob_Key_Box, proportion = 6, flag = wx.EXPAND )
        Bob_Box.Add( self.Load_Key_BTN, proportion = 2, flag = wx.EXPAND|wx.ALL, border=10)
        
        Plain_BTNs_RIGHT.Add( self.Encrypt_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Plain_BTNs_RIGHT.Add( self.Sign_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Plain_BTNs_LEFT.Add( self.Load_Plain_BTN, proportion = 1,  flag=wx.ALL, border=10)
        Plain_BTNs_LEFT.Add( self.Save_Plain_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Plain_BTNs.Add( Plain_BTNs_LEFT, proportion = 1, flag=wx.EXPAND )
        Plain_BTNs.Add( Plain_BTNs_RIGHT, proportion = 1, flag=wx.EXPAND )
        Plain_Box.Add( self.Send_Box, proportion = 6, flag = wx.EXPAND|wx.LEFT, border=30)
        Plain_Box.Add( Plain_BTNs, proportion = 2, flag = wx.EXPAND)

        Cipher_BTNs_RIGHT.Add( self.Decrypt_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Cipher_BTNs_RIGHT.Add( self.Validate_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Cipher_BTNs_LEFT.Add( self.Load_Cipher_BTN, proportion = 1,  flag=wx.ALL, border=10)
        Cipher_BTNs_LEFT.Add( self.Save_Cipher_BTN, proportion = 1, flag=wx.ALL, border=10 )
        Cipher_BTNs.Add( Cipher_BTNs_LEFT, proportion = 1, flag=wx.EXPAND )
        Cipher_BTNs.Add( Cipher_BTNs_RIGHT, proportion = 1, flag=wx.EXPAND )
        Cipher_Box.Add( self.Receive_Box, proportion = 6, flag = wx.EXPAND|wx.LEFT, border=30)
        Cipher_Box.Add( Cipher_BTNs, proportion = 2, flag = wx.EXPAND)

        
        #Cipher_BTNs.Add( self.Save_BTN, proportion = 1, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=30 )
        #Cipher_Box.Add( self.Receive_Box, proportion = 6, flag = wx.EXPAND|wx.LEFT, border=30)
        #Cipher_Box.Add( Cipher_BTNs, proportion = 2, flag = wx.EXPAND)

        V_Box.Add( Alice_Box, proportion = 6, flag = wx.EXPAND|wx.ALL, border=10)
        V_Box.Add( Bob_Box, proportion = 3, flag = wx.EXPAND|wx.ALL, border=10)
        V_Box.Add( Plain_Box, proportion = 4, flag = wx.EXPAND|wx.ALL, border=10)
        V_Box.Add( Cipher_Box, proportion = 4, flag = wx.EXPAND|wx.ALL, border=10)
        self.panel.SetSizer(V_Box)

        # Bind Objects to Handlers       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox)
        self.Gen_BTN.Bind( wx.EVT_BUTTON, self.generate_Key )
        self.Read_BTN.Bind( wx.EVT_BUTTON, self.read_MY_Key )
        self.Write_BTN.Bind( wx.EVT_BUTTON, self.write_MY_Key )
        self.Clear_BTN.Bind( wx.EVT_BUTTON, self.clear_Key )
        self.Load_Key_BTN.Bind( wx.EVT_BUTTON, self.load_OTHER_Key )
        self.Encrypt_BTN.Bind( wx.EVT_BUTTON, self.encrypt )
        self.Decrypt_BTN.Bind( wx.EVT_BUTTON, self.decrypt )
        self.Sign_BTN.Bind( wx.EVT_BUTTON, self.sign )
        self.Validate_BTN.Bind( wx.EVT_BUTTON, self.validate )
        self.Load_Plain_BTN.Bind( wx.EVT_BUTTON, self.load_plain )
        self.Load_Cipher_BTN.Bind( wx.EVT_BUTTON, self.load_cipher )
        self.Save_Plain_BTN.Bind( wx.EVT_BUTTON, self.save_plain )
        self.Save_Cipher_BTN.Bind( wx.EVT_BUTTON, self.save_cipher )

        self.fileDialog = wx.FileDialog(self.panel, defaultDir = myDir)

    def EvtRadioBox(self, event):
        self.key_length = int(self.Chose_Radio.GetStringSelection())
        #f = open('key_length', 'w')
        #f.write(str(self.key_length))
        #f.close()
        
    # File Save_Load
    # 是不是可以把函数的对象（Key还是Plain）抽成参数，只留下 Read和Write函数？
    # 先独立写好这几个函数，看看有没有很多公共部分吧，直路走得快，弯路走得远。
    def reading(self, filename):
        try:
            f = open(filename, 'r')
            lines = f.readlines()
            f.close()
            return lines
        except IOError:
            return []
        
    def writing(self, filename, lines):
        try:
            f = open(filename, 'w')
            f.writelines(lines)
            f.close()
        except IOError:
            pass
    
    def read_MY_Key(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            my_key = self.reading(self.fileDialog.GetPath())
            n = my_key[0]
            e = my_key[1]
            d = my_key[2]
            self.MY_N_Box.SetValue(n)
            self.MY_E_Box.SetValue(e)
            self.MY_D_Box.SetValue(d)
        
    def write_MY_Key(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            n = self.MY_N_Box.GetValue()
            e = self.MY_E_Box.GetValue()
            d = self.MY_D_Box.GetValue()
            self.writing(self.fileDialog.GetPath(), [n, '\n', e, '\n', d])
        
    def clear_Key(self, event):
        self.MY_N_Box.SetValue('')
        self.MY_E_Box.SetValue('')
        self.MY_D_Box.SetValue('')

    def load_OTHER_Key(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            other_key = self.reading(self.fileDialog.GetPath())
            n = other_key[0]
            e = other_key[1]
            self.OTHER_N_Box.SetValue(n)
            self.OTHER_E_Box.SetValue(e)

    def load_plain(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            plaintext = self.reading(self.fileDialog.GetPath())[0]
            self.Send_Box.SetValue(plaintext)

    def load_cipher(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            ciphertext = self.reading(self.fileDialog.GetPath())[0]
            self.Receive_Box.SetValue(ciphertext)

    def save_plain(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            plaintext = self.Send_Box.GetValue()
            self.writing(self.fileDialog.GetPath(), plaintext)

    def save_cipher(self, event):
        onclick = self.fileDialog.ShowModal()
        if onclick == wx.ID_OK:
            ciphertext = self.Send_Box.GetValue()
            self.writing(self.fileDialog.GetPath(), ciphertext)
            
    # RSA Algorithm
    def generate_Key(self, event):
        """
        f = open('key_length', 'r')
        lines = f.readlines()
        f.close()
        kl = lines[0]
        cnt = int(lines[1])
        f = open('key_length', 'w')
        f.write(kl)
        f.write(str(cnt+1) )
        f.close()
        """
        (p,q,n,e,d) = RSA_generate_key(self.key_length)
        #self.MY_P_Box.SetValue(unicode(p))
        #self.MY_Q_Box.SetValue(unicode(q))
        self.MY_N_Box.SetValue(unicode(n))
        self.MY_E_Box.SetValue(unicode(e))
        self.MY_D_Box.SetValue(unicode(d))        

    def bit_from_byte(self, byte): #@ pass testing
        return bin(ord(byte))[2:].zfill(8)

    def byte_from_bit(self, bits): #@ pass testing
        # type[bit] : 8 bit '0'/'1'        
        return chr( int(bits,2 ) )

    def bitStream_from_byteStream ( self, byteStream ):
        result = ''
        for byte in byteStream :
            result += self.bit_from_byte( byte )
        return result

    def byteStream_from_bitStream ( self, bitStream ):
        result = ''
        for i in range( len(bitStream)/8 ) :
            result += self.byte_from_bit( bitStream[i*8:(i+1)*8] )
        return result

    def split_byteStream(self, byteStream):
        # packet_length according to self.key_length
        packet_length = self.key_length / 8
        # auto-complete
        text_length = len(byteStream)
        byteStream = byteStream + '@' * ((packet_length - text_length % packet_length) % packet_length)
        result = []
        pt = 0
        while pt < text_length:
            result.append(byteStream[pt:pt+packet_length])
            pt += packet_length

        return result

    def split_bitStream(self, bitStream):
        # packet_length according to self.key_length
        packet_length = self.key_length
        text_length = len(bitStream)
        result = []
        pt = 0
        while pt < text_length:
            result.append(bitStream[pt:pt+packet_length])
            pt += packet_length
            
        return result
    
    def encrypt(self, event):
        # material
        plaintext = self.Send_Box.GetValue().encode(myCharset)
        try:
            n = int(self.OTHER_N_Box.GetValue())
            e = int(self.OTHER_E_Box.GetValue())
        except ValueError:
            pass
        packets = self.split_bitStream(plaintext)
        ciphertext = ''
        #tt = []
        #ss = []
        for packet in packets:
            pInt = int(packet,2)
            #tt.append(cInt)
            cInt = pow_and_mod(pInt, e, n)
            #ss.append(pInt)
            cInt = bin(cInt)[2:]
            cInt = '0' * (len(packet) % len(cInt)) + cInt
            ciphertext += cInt

        #print 'C:', tt
        #print 'P:', ss
        # plaintext got.
        self.Send_Box.SetValue(ciphertext)

    def decrypt(self, event):
        # material
        ciphertext = self.Receive_Box.GetValue().encode(myCharset)
        try:
            n = int(self.MY_N_Box.GetValue())
            d = int(self.MY_D_Box.GetValue())
        except ValueError:
            pass
        packets = self.split_bitStream(ciphertext)
        plaintext = ''
        #tt = []
        #ss = []
        for packet in packets:
            cInt = int(packet,2)
            #tt.append(cInt)
            pInt = pow_and_mod(cInt, d, n)
            #ss.append(pInt)
            pInt = bin(pInt)[2:]
            pInt = '0' * (len(packet) % len(pInt)) + pInt
            plaintext += pInt

        #print 'C:', tt
        #print 'P:', ss
        # plaintext got.
        self.Receive_Box.SetValue(plaintext)

    def sign(self, event):
        # material
        original_text = self.Send_Box.GetValue().encode(myCharset)
        try:
            n = int(self.MY_N_Box.GetValue())
            d = int(self.MY_D_Box.GetValue())
        except ValueError:
            pass
        packets = self.split_byteStream(original_text)
        signed_text = ''
        ss = []
        tt = []
        for packet in packets:
            ptxt = self.bitStream_from_byteStream(packet)
            pInt = int(ptxt,2)
            #ss.append(pInt)
            cInt = pow_and_mod(pInt, d, n)
            #tt.append(cInt)
            signed_text += bin(cInt)[2:].zfill(self.key_length)
        
        # signed_text got.
        #print 'P:', ss
        #print 'C:', tt
        self.Send_Box.SetValue(signed_text)

    def validate(self, event):
        # material
        signed_text = self.Receive_Box.GetValue().encode(myCharset)
        try:
            n = int(self.OTHER_N_Box.GetValue())
            e = int(self.OTHER_E_Box.GetValue())
        except ValueError:
            pass
        packets = self.split_bitStream(signed_text)
        original_text = ''
        #tt = []
        #ss = []
        for packet in packets:
            cInt = int(packet,2)
            #tt.append(cInt)
            pInt = pow_and_mod(cInt, e, n)
            #ss.append(pInt)
            pInt = bin(pInt)[2:]
            pInt = '0' * (len(packet) % len(pInt)) + pInt
            original_text += self.byteStream_from_bitStream(pInt)

        #print 'C:', tt
        #print 'P:', ss
        # original_text got.
        self.Receive_Box.SetValue(original_text)    
        
if __name__ == '__main__':
    app = wx.App()
    win = RSA_frame()
    win.Show()
    app.MainLoop()
