from os import system
from time import sleep
from ServerInfo import *
from ConnectServer import *

if __name__=="__main__":

    def RunApplication(Ip:str,Username:str,Password:str):
            print("Start :)")
            if 'Sell_virtual_number_panel.zip' in CopyZipToServer(Ip=Ip,Username=Username,Password=Password,NameZipFile='Sell_virtual_number_panel.zip',PathOrginalToZip='E:\Projects\Python\Sell_virtual_number_panel',Localpath='./Sell_virtual_number_panel.zip',Serverpath='/home/GrayHat/Sell_virtual_number_panel/Sell_virtual_number_panel.zip'):
                print("Copy \'Sell_virtual_number_panel.zip\' File Succsess..")
                ConstCommand="cd ..;cd home/GrayHat/Sell_virtual_number_panel;"
                CommandUnzip="{0}unzip Sell_virtual_number_panel.zip".format(ConstCommand)
                Log=ExcuteCommandServer(Ip,Username,Password,CommandUnzip)
                if 'Archive:  Sell_virtual_number_panel.zip' in Log[0]:
                    print("Unzip \'Sell_virtual_number_panel.zip\' Succsess..")
                    CommandRun="{0}cd Telegram-Bot;nohup python3.10 Main.py &>/dev/null & ".format(ConstCommand)
                    Log=ExcuteCommandServer(Ip,Username,Password,CommandRun)
                    if Log == ('',''):
                        print("Run \' Main.py \' :)")
                        if input("Kill Project => [ Y-N ]: ") == 'Y':
                            LogKill=ExcuteCommandServer(Ip,Username,Password,"killall python3.10")
                            print("Kill \' Main.py \' :)")

    def KillApplication(Ip:str,Username:str,Password:str):
         if input("Kill Project => [ Y-N ]: ") == 'Y':
            LogKill=ExcuteCommandServer(Ip,Username,Password,"killall python3.10")
            print("Kill \' Main.py \' :)")

    def Run():
        try:
            print("[1] Run Application.")
            print("[2] Kill Application.")
            print("[3] Kill And Run Application.")
            print("[4] Exit.")
            NumberInput=int(input("[?] : "))
            if type(NumberInput)==int:
                Ip=IP
                Username=USERNAME
                Password=PASSWORD
                system("cls")
                match NumberInput:
                    case 1:
                        RunApplication(Ip,Username,Password)
                        sleep(1)
                    case 2:
                        KillApplication(Ip,Username,Password)
                        sleep(1)
                    case 3:
                        KillApplication(Ip,Username,Password)
                        RunApplication(Ip,Username,Password)
                        sleep(1)
                    case 4:
                        return
                    case _:
                        print("Error Number Not Found..")
                system("cls")
        except Exception as e:
            print(str(e))
            sleep(1)
        system("rmdir /s /q __pycache__")
        system("cls")
        Run()
        
    Run()