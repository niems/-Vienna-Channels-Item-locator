import subprocess


for i in range(100):
    subprocess.call(['start', 'notepad'], shell=True)
    
subprocess.call(['TASKKILL', '/F', 'IM', 'cmd.exe'], shell=True)