from paramiko import SSHClient,AutoAddPolicy
from shutil import make_archive
from subprocess import getoutput
from os import remove

def ExcuteCommandServer(Ip:str,Username:str,Password:str,Command:str):
    Client = SSHClient()
    Client.set_missing_host_key_policy(AutoAddPolicy())
    Client.connect(Ip,username=Username,password=Password)
    Input,Log=Client.exec_command(Command)[1:]
    ResultLog=(Input.read().decode(),Log.read().decode())
    Client.close()
    return ResultLog

def ZipDirctory(Filename:str,Pathdirctory:str):
    IsExists=getoutput("dir /b").split("\n")
    if (Filename in IsExists) is True:
        remove(Filename)
    make_archive(Filename.replace('.zip',''),'zip',Pathdirctory)

def GetDir(Ip:str,Username:str,Password:str,Commandls):
    ResultLs=ExcuteCommandServer(Ip,Username,Password,Commandls)
    return ResultLs

def RmDir(Ip:str,Username:str,Password:str):
    RmDirctory="cd ..;cd home/GrayHat;rm -rf *"
    Results=ExcuteCommandServer(Ip,Username,Password,RmDirctory)
    return Results
    
def CheckExitstFolder(Ip:str,Username:str,Password:str):
    ResultDir=GetDir(Ip,Username,Password,'cd ..;cd home/GrayHat;ls')[0]
    if ResultDir == '':
        CreateDir='cd ..;cd home/GrayHat;mkdir Sell_virtual_number_panel'
        ExcuteCommandServer(Ip,Username,Password,CreateDir)
        if 'Sell_virtual_number_panel' in GetDir(Ip,Username,Password,'cd ..;cd home/GrayHat;ls')[0]:
            print("Dirctory \'Sell_virtual_number_panel.zip\' Created Succsess..")
            return 'Create'
    else:
        return 'Exists'

def CopyZipToServer(Ip:str,Username:str,Password:str,NameZipFile:str,PathOrginalToZip:str,Localpath:str,Serverpath:str):
    Client = SSHClient()
    Client.set_missing_host_key_policy(AutoAddPolicy())
    if CheckExitstFolder(Ip,Username,Password) == 'Exists':
        print("Find \'Sell_virtual_number_panel.zip\' !")
        RmDir(Ip,Username,Password)
        print("Remove \'Sell_virtual_number_panel.zip\' Exitst Succsess..")
    if CheckExitstFolder(Ip,Username,Password) == 'Create':
        ZipDirctory(NameZipFile,PathOrginalToZip)
    Client.connect(Ip,username=Username,password=Password)
    Scp=Client.open_sftp()
    Scp.put(Localpath,Serverpath)
    Scp.close()
    Client.close()
    return GetDir(Ip,Username,Password,'cd ..;cd home/GrayHat/Sell_virtual_number_panel;ls')[0]


