import os

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    
def shutdown_pc():
    os.system("shutdown -s")
    
    
    
