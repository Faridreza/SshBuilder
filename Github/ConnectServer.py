from paramiko import SSHClient,AutoAddPolicy

def ExcuteCommandServer(Ip:str,Username:str,Password:str,Command:str):
    Client = SSHClient()
    Client.set_missing_host_key_policy(AutoAddPolicy())
    Client.connect(Ip,username=Username,password=Password)
    Log=Client.exec_command(Command)[-1]
    ResultLog=Log.read().decode()
    Client.close()
    return ResultLog