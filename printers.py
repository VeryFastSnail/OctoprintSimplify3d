import tkinter as tk 
import sys
import os
from tkinter import ttk 

if(len(sys.argv) < 1):
    exit()
 
print(len(sys.argv)) 
 
myPrinters = {
    'Printer 1' : {
                                'ip' : '192.168.0.0',
                                'auth': 'secret',
                              },
    'Printer 2' : {
                                'ip' : '192.168.0.1',
                                'auth': 'secret',
                              },
    'Printer 3' : {
                                'ip' : '192.168.0.2',
                                'auth': 'secret',
                              }
}

#

def sendFile():
    printer = myPrinters[monthchoosen.get()]
    request = r'curl -k -H "X-Api-Key: {api}" -F "select=false" -F "print=false" -F "file={file}" "http://{ip}/api/files/local"'.format(api=printer['auth'], ip=printer['ip'], file=sys.argv[1])
    os.popen(request)
    exit()

printersNames = list(myPrinters.keys())

print(printersNames)
  
window = tk.Tk() 
window.title('Select your printer') 
window.geometry('300x150') 
  
ttk.Label(window, text = "Please select octoprint instance",  
          foreground ="black",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
 
ttk.Label(window, 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, state='readonly', width = 27, textvariable = n) 
  

monthchoosen['values'] = printersNames
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current(0)

submit = ttk.Button(window, text ="Send File", command = sendFile).grid(column = 1, row = 7)


window.mainloop() 