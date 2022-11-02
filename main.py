from cProfile import label
from fileinput import filename
import tkinter as tk   # create the GUI
from tkinter import Canvas, Frame, filedialog , Text #pick the apps
import os #run the apps that we will add to our app

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt' , 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',') #split the tempApps with the ,
        apps = [d for d in tempApps if d.strip()] #delete the white space

def addApp():
    for widget in Frame.winfo_children():   #delete the repeated file that come after we select again
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/' , title='Select File' , filetypes=(('executables', '*.exe') , ('all files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:    #show the doc inside the container
        label= tk.Label(Frame , text=app , bg='gray')
        label.pack()

def runApps():
    for app in apps :
        os.startfile(app)  #looping inside the app and start the file


Canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
Canvas.pack()  # to touch the root and the changes affect 

Frame = tk.Frame(root, bg="white") #adding container inside the canvas
Frame.place(relwidth=0.8 , relheight=0.8 , relx=0.1 , rely=0.1)

openFile= tk.Button(root , text="Open File" , padx=10 , pady=5 , fg="white" , bg="#263D42" , command=addApp) #adding button / command to run the addapp fnct
openFile.pack()

runApps= tk.Button(root , text="Run Apps" , padx=10 , pady=5 , fg="white" , bg="#263D42" , command=runApps) #adding button 
runApps.pack()


for app in apps:  # find the apps in the container when first runing the file
    label= tk.Label(Frame , text=app)
    label.pack()


root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')