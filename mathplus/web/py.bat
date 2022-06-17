@echo off
start C:\Users\Administrator.WIN8-1705181640\AppData\Roaming\Lantern\lantern.exe &
ping localhost -n 1
d:  
cd d:\mypython\math113
start python math113id.py &
ping localhost -n 1
start python mycopy.py &
ping localhost -n 1
exit