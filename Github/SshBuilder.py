from ConnectServer import ExcuteCommandServer
from os import system
from ServerInfo import *
try:

    Commands=[
        'cd ..',
        'cd home/GrayHat',
        'rm -rf *',
        'git clone {0}'.format("Github SshKey or Link"), #git@github.com:Faridreza/{NameRepo}.git https://github.com/Faridreza/{NameRepo}.git
        'cd {FolderName Clone}',
        'touch Config.py', #مربوط به پروژه منه شما میتونید پاک کنید
        'echo -e "TOKEN=\\"{0}\\"" >> Config.py'.format(TOKEN),
        'nohup python3.10 Main.py &>/dev/null &' #رانش کن تو بک گراند
        ]

    Command=""

    for i in Commands:
        Command+=i+';'
    
    Command=Command.replace(Command[len(Command)-2:],'&')

    Ip=IP
    Username=USERNAME
    Password=PASSWORD   

    Log=ExcuteCommandServer(Ip,Username,Password,Command)

    if Log=="Cloning into 'Sell_virtual_number_panel'...\n":
        print("Run :)")
        if input("Kill Project => [ Y-N ]: ") == 'Y':
            LogKill=ExcuteCommandServer(Ip,Username,Password,"killall python3.10")
            print("Kill :)")
    else:
        print(Log)

except Exception as e:
    print(str(e))

finally:
    system("rmdir /s /q __pycache__")
    print("Bye :)")