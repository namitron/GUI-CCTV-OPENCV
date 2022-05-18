import cv2
import tkinter  
from PIL import Image, ImageTk
#import numpy as np
from tkvideo import tkvideo

port = tkinter.Tk()
t3 = tkinter.StringVar()
t4 = tkinter.StringVar()


port.minsize(width=400, height=670)
port.maxsize(width=400, height=670)
port.geometry('400x100+0+0')


a = 100
b = 100
c = 100
d = 100
e = 0

#def image():
    #size = (200,200)
   # haha = cv2.resize(logo2, size, interpolation=cv2.INTER_AREA)
    #img = Image.fromarray(haha)
   # imgtk = ImageTk.PhotoImage(img)
    #label.configure(image=imgtk)
    #label.image = imgtk
    

def show():

    captura1 = cv2.VideoCapture(a, cv2.CAP_FFMPEG) 
    captura2 = cv2.VideoCapture(b, cv2.CAP_FFMPEG)
    captura3 = cv2.VideoCapture(c, cv2.CAP_FFMPEG)
    capturanya = cv2.VideoCapture(d, cv2.CAP_FFMPEG)
    

    


#TUNGGAL
    while (a != 100 and e==1):                              
        ret1, frame = captura1.read()
        print(frame)
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break
            

        
            #frame_width = int(cap.get(3))
            #frame_height = int(cap.get(4))


           # out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))



    while (b != 100 and e==1):                                
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
                
                                   
 
    while (c != 100 and e==1):  
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('ketiga', 4)<1:
            break                
                    
                    

    while (d != 100 and e==1):  
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        if cv2.getWindowProperty('keempat', 4)<1:
            break 
        
#DOUBLE
    while (a != 100 and b != 100 and e==2):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break  
        if cv2.getWindowProperty('kedua', 4)<1:
            break                     
    while (a != 100 and c != 100 and e==2):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)

        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break  
        if cv2.getWindowProperty('ketiga', 4)<1:
            break  
 
    while (a != 100 and d != 100 and e==2):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break                
        if cv2.getWindowProperty('keempat', 4)<1:
            break                



    while (b != 100 and c != 100 and e==2):                              
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)  
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)  
             
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('kedua' ,4)<1:
            break
        if cv2.getWindowProperty('ketiga', 4)<1:
            break 
            
    while (b != 100 and d != 100 and e==2):                              
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310)        
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break 
  
    while (c != 100 and d != 100 and e==2):                              
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)  
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310) 
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('ketiga', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break 
#TRIPLE
    while (a != 100 and b != 100 and c != 100 and e==3):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
            
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)                

        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break 
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
        if cv2.getWindowProperty('ketiga', 4)<1:
            break                

    while (a != 100 and b != 100 and d != 100 and e==3):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
            
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)                
    
    
            
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310) 
            
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break 
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break         
        
        
    while (a != 100 and c != 100 and d != 100 and e==3):                              
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
            
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)

        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break 
        if cv2.getWindowProperty('ketiga', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break         
            
    while (b != 100 and c != 100 and d != 100 and e==3):                              
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)                
                    
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)
        
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
        if cv2.getWindowProperty('ketiga', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break         
                    
#QUART
    while (b != 100 and c != 100 and d != 100 and e==4):          
        ret1, frame = captura1.read()
        if ret1:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo    
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)        
        ret2, frame2 = captura2.read() 
        if ret2:
            #frame2 = cv2.flip(frame2, 2)
            #roi2 = frame2[-size-10:-10, -size-10:-10]
            #roi2[np.where(logo)] = 0
            #roi2 += logo   
            cv2.namedWindow('kedua', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('kedua',frame2)
            cv2.resizeWindow('kedua', 460, 310)                
                    
        ret3, framenya = captura3.read() 
        if ret3:
            #framenya = cv2.flip(framenya, 3)
            #roi3 = framenya[-size-10:-10, -size-10:-10]
            #roi3[np.where(logo)] = 0
            #roi3 += logo 
            cv2.namedWindow('ketiga', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('ketiga',framenya)
            cv2.resizeWindow('ketiga', 460,310)
        
        ret4, framenyakamu = capturanya.read() 
        if ret4:
            #framenyakamu = cv2.flip(framenyakamu, 4)
            #roi4 = framenyakamu[-size-10:-10, -size-10:-10]
            #roi4[np.where(logo)] = 0
            #roi4 += logo 
            cv2.namedWindow('keempat', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('keempat',framenyakamu)
            cv2.resizeWindow('keempat', 460,310) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('pertama', 4)<1:
            break        
        if cv2.getWindowProperty('kedua', 4)<1:
            break 
        if cv2.getWindowProperty('ketiga', 4)<1:
            break 
        if cv2.getWindowProperty('keempat', 4)<1:
            break         
        
        
        
        
        
        
        
        
        
#t1 = tkinter.Label(port, text="port1 = ")
#t2 = tkinter.Label(port, text="port2 = ")
#t3 = tkinter.Label(port, text="port3 = ")
#t4 = tkinter.Label(port, text="port4 = ")

#t1.place(x=40, y=340)
#t2.place(x=552, y=340)
#t3.place(x=40, y=680)
#t4.place(x=552, y=680)

def p1():
    global a
    global warna
    
    
    a = e1.get()
    a = str(a)
    print(a)
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,  command=p1, bd=5, fg='white', bg='red')
    c1.place(x=210, y=350)
    c2 = tkinter.Button(port, text='Usb',width=5, height=1, command=p2,bd=5,fg='black')
    c2.place(x=260, y=350)
    
def p2():
    global a
    global warna
    a = e1.get()
    a = int(a)
    print(a)
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,  command=p1,bd=5 ,fg='black')
    c1.place(x=210, y=350)
    c2 = tkinter.Button(port, text='Usb',width=5, height=1, command=p2,bd=5, fg='white', bg='red')
    c2.place(x=260, y=350)

    
def q1():
    global b
    b = e2.get()
    b = str(b)
    print(b)
    c3 = tkinter.Button(port, text='Ip',width=5, height=1,  command=q1,bd=5, fg='white', bg = 'red')
    c4 = tkinter.Button(port, text='Usb',width=5, height=1, command=q2,bd=5 ,fg='black')
    c3.place(x=210, y=400)
    c4.place(x=260, y=400)
    
def q2():
    global b
    b = e2.get()
    b = int(b)
    print(b)
    c3 = tkinter.Button(port, text='Ip',width=5, height=1,  command=q1,bd=5 ,fg='black')
    c4 = tkinter.Button(port, text='Usb',width=5, height=1, command=q2,bd=5, fg='white',  bg ='red')
    c3.place(x=210, y=400)
    c4.place(x=260, y=400)
def r1():
    global c
    c = e3.get()
    c = str(c)
    print(c)
    c5 = tkinter.Button(port, text='Ip',width=5, height=1,  command=r1,bd=5,fg='white',  bg = 'red')
    c6 = tkinter.Button(port, text='Usb',width=5, height=1, command=r2,bd=5 ,fg='black')
    c5.place(x=210, y=450)
    c6.place(x=260, y=450)
    
def r2():
    global c
    c = e3.get()
    c = int(c)
    print(c)
    c5 = tkinter.Button(port, text='Ip',width=5, height=1,  command=r1,bd=5 ,fg='black')
    c6 = tkinter.Button(port, text='Usb',width=5, height=1, command=r2,bd=5, fg='white' , bg = 'red')
    c5.place(x=210, y=450)
    c6.place(x=260, y=450)
    
def s1():
    global d
    d = e4.get()
    d = str(d)
    print(d)
    c7 = tkinter.Button(port, text='Ip',width=5, height=1,  command=s1,bd=5,fg='white',  bg = 'red')
    c8 = tkinter.Button(port, text='Usb',width=5, height=1, command=s2,bd=5 ,fg='black')
    c7.place(x=210, y=500)
    c8.place(x=260, y=500)
def s2():
    global d
    d = e4.get()
    d = int(d)
    print(d)
    c7 = tkinter.Button(port, text='Ip',width=5, height=1,  command=s1,bd=5 ,fg='black')
    c8 = tkinter.Button(port, text='Usb',width=5, height=1, command=s2,bd=5, fg='white' , bg = 'red')
    c7.place(x=210, y=500)
    c8.place(x=260, y=500)







def set_1():
    reset()
    global e
    
    e = 1
    print(e)
 
    
    
    global t1
    global e1
    global c1
    global c2

    t1 = tkinter.Label(port, text="Port1" )
    t1.place(x=15, y=350)

    e1 = tkinter.Entry(port, bd=5)
    e1.pack(side=tkinter.LEFT)
    e1.place(x=50, y=350)
    
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
    c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,command=p2)
    c1.place(x=210, y=350)
    c2.place(x=260, y=350)

    
def set_2():
    reset()
    global e
    
    e = 2         
    print(e)

    
    global t1
    global e1
    global c1
    global c2


    t1 = tkinter.Label(port, text="Port1 ")
    t1.place(x=15, y=350)

    e1 = tkinter.Entry(port, bd=5)
    e1.pack(side=tkinter.LEFT)
    e1.place(x=50, y=350)
    
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
    c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)
    c1.place(x=210, y=350)
    c2.place(x=260, y=350)
    
    global t2
    global e2
    global c3
    global c4

    t2 = tkinter.Label(port, text="Port2 ")

    t2.place(x=15, y=400)
    e2 = tkinter.Entry(port, bd=5)
    e2.pack(side=tkinter.LEFT)
    e2.place(x=50, y=400)
    c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
    c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
    c3.place(x=210, y=400)
    c4.place(x=260, y=400)

def set_3():
    reset()
    global e
    
    e = 3         
    print(e)

    
    global t1
    global e1
    global c1
    global c2

    t1 = tkinter.Label(port, text="Port1 ")
    t1.place(x=15, y=350)

    e1 = tkinter.Entry(port, bd=5)
    e1.pack(side=tkinter.LEFT)
    e1.place(x=50, y=350)
    
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
    c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)
    c1.place(x=210, y=350)
    c2.place(x=260, y=350)
    
    global t2
    global e2
    global c3
    global c4
 
    t2 = tkinter.Label(port, text="Port2 ")

    t2.place(x=15, y=400)
    e2 = tkinter.Entry(port, bd=5)
    e2.pack(side=tkinter.LEFT)
    e2.place(x=50, y=400)
    c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
    c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
    c3.place(x=210, y=400)
    c4.place(x=260, y=400)
    global t3
    global e3
    global c5
    global c6

    t3 = tkinter.Label(port, text="Port3 ")
    t3.place(x=15, y=450)
    e3 = tkinter.Entry(port, bd=5)
    e3.pack(side=tkinter.LEFT)
    e3.place(x=50, y=450)
    c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
    c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
    c5.place(x=210, y=450)
    c6.place(x=260, y=450)

def set_4():
    reset()
    global e
    
    e = 4         
    print(e)

    
    global t1
    global e1
    global c1
    global c2

    
    t1 = tkinter.Label(port, text="Port1 ")
    t1.place(x=15, y=350)

    e1 = tkinter.Entry(port, bd=5)
    e1.pack(side=tkinter.LEFT)
    e1.place(x=50, y=350)
    
    c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
    c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)
    c1.place(x=210, y=350)
    c2.place(x=260, y=350)
    
    global t2
    global e2
    global c3
    global c4

    t2 = tkinter.Label(port, text="Port2 ")
    t2.place(x=15, y=400)
    e2 = tkinter.Entry(port, bd=5)
    e2.pack(side=tkinter.LEFT)
    e2.place(x=50, y=400)
    c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
    c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
    c3.place(x=210, y=400)
    c4.place(x=260, y=400)
    
    global t3
    global e3
    global c5
    global c6

    t3 = tkinter.Label(port, text="Port3 ")
    t3.place(x=15, y=450)
    e3 = tkinter.Entry(port, bd=5)
    e3.pack(side=tkinter.LEFT)
    e3.place(x=50, y=450)
    c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
    c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
    c5.place(x=210, y=450)
    c6.place(x=260, y=450)
    global t4
    global e4
    global c7
    global c8
    

    t4 = tkinter.Label(port, text="Port4 ")
    t4.place(x=15, y=500)   
    e4 = tkinter.Entry(port, bd=5)    
    e4.pack(side=tkinter.LEFT) 
    e4.place(x=50, y=500)
    c7 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=s1)
    c8 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=s2)
    c7.place(x=210, y=500)
    c8.place(x=260, y=500)
            
def reset2():
    global a,b,c,d
    a = 100
    b = 100
    c = 100
    d = 100
    
    if e == 1 :
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
    if e == 2:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
    if e == 3:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
        c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
        c5.place(x=210, y=450)
        c6.place(x=260, y=450)
    if e == 4:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
        c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
        c7 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=s1)
        c8 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=s2)    
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
        c5.place(x=210, y=450)
        c6.place(x=260, y=450)    
        c7.place(x=210, y=500)
        c8.place(x=260, y=500) 
        
def reset():
    global a,b,c,d
    a = 100
    b = 100
    c = 100
    d = 100
    
    if e == 1 :
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
    if e == 2:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
    if e == 3:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
        c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
        c5.place(x=210, y=450)
        c6.place(x=260, y=450)
    if e == 4:
        c1 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=p1)
        c2 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=p2)        
        c3 = tkinter.Button(port, text='Ip',width=5, height=1, bd=5, command=q1)
        c4 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=q2)
        c5 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=r1)
        c6 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=r2)
        c7 = tkinter.Button(port, text='Ip',width=5, height=1,bd=5 , command=s1)
        c8 = tkinter.Button(port, text='usb',width=5, height=1,bd=5,  command=s2)    
        c1.place(x=210, y=350)
        c2.place(x=260, y=350)
        c3.place(x=210, y=400)
        c4.place(x=260, y=400)
        c5.place(x=210, y=450)
        c6.place(x=260, y=450)    
        c7.place(x=210, y=500)
        c8.place(x=260, y=500)    

    wrapper2 = tkinter.LabelFrame(port,bg="#EEEEF5", width=380, height=280)
    wrapper2.pack(side=tkinter.LEFT)
    wrapper2.place(x=10, y=340)


#logo = cv2.imread('mico3.png')
#size = 250
#logo = cv2.resize(logo, (size, size))
#img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

def recordvideo():

    captura1 = cv2.VideoCapture(a, cv2.CAP_DSHOW) 
    if (captura1.isOpened() == False): 
      print("Unable to read camera feed")
    frame_width = int(captura1.get(3))
    frame_height = int(captura1.get(4))
    out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
  
    #TUNGGAL
    while (a != 100 and e==1):                              
        ret1, frame = captura1.read()
        if ret1==True:
            #frame = cv2.flip(frame, 1)
            #roi = frame[-size-10:-10, -size-10:-10]
            #roi[np.where(logo)] = 0
            #roi += logo
            out.write(frame) 
            cv2.namedWindow('pertama', cv2.WINDOW_KEEPRATIO)
            cv2.imshow('pertama',frame)
            cv2.resizeWindow('pertama', 460, 310)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
        if cv2.getWindowProperty('pertama', 4)<1:
            break

    if cv2.getWindowProperty('pertama', 4)<1:
        global wrapper2
        wrapper2 = tkinter.Label(wrapper, bg="#1C1C2F", width=369, height=198)
        wrapper2.pack(side=tkinter.LEFT)
        wrapper2.place(x=8, y=0)
        
        wrapper3 = tkinter.Label(wrapper, bg="#4d5763", width=3, height=198)
        wrapper3.pack(side=tkinter.LEFT)
        wrapper3.place(x=0, y=0)        

        c12 = tkinter.Button(wrapper, width=20, bd='0', bg='#4d5763', height=20, command=viewvideo)
        c12.place(x=2, y=2)
        c12.configure(image=view)
       
    captura1.release()
    out.release() 

def viewvideo():
    c12 = tkinter.Button(wrapper, width=20, bd='0', bg='#1C1C2F', height=20, command=viewvideo)
    c12.place(x=2, y=2)
    c12.configure(image=view)
    
    player = tkvideo("outpy.mp4", wrapper2, size = (369,198))
    player.play()
    
    print(player)
    

    
    
    
width = 20
height = 20

img = Image.open("resetgambar.png")
img = img.resize((width,height), Image.ANTIALIAS)
resetimage =  ImageTk.PhotoImage(img)

run = Image.open("run.png")
run = run.resize((width,height), Image.ANTIALIAS)
run =  ImageTk.PhotoImage(run)

logo = Image.open("mico3.png")
logo = logo.resize((100,100), Image.ANTIALIAS)
logo =  ImageTk.PhotoImage(logo)

record = Image.open("record.png")
record = record.resize((width,height), Image.ANTIALIAS)
record =  ImageTk.PhotoImage(record)

record1 = Image.open("record1.png")
record1 = record1.resize((width,height), Image.ANTIALIAS)
record1 =  ImageTk.PhotoImage(record1)

view = Image.open("run2.png")
view = view.resize((10,10), Image.ANTIALIAS)
view =  ImageTk.PhotoImage(view)

toolbar = tkinter.Frame( port, bg="#4d5763", width=400, height=50)
toolbar.pack(side=tkinter.TOP)
toolbar.place(x=0, y=0)

port.configure(bg='#1C1C2F')

frame1 = tkinter.LabelFrame(port, text="Video View", fg ="white" , bg="#4d5763", width=390, height=230)
frame1.pack(side=tkinter.LEFT)
frame1.place(x=5, y=70)


frame2 = tkinter.LabelFrame(port, text="Port Configure", fg ="white" ,  bg="#4d5763", width=390, height=320)
frame2.pack(side=tkinter.LEFT)
frame2.place(x=5, y=310)

wrapper = tkinter.Label(port, image=logo, bg="#EEEEF5", width=372, height=190)
wrapper.pack(side=tkinter.LEFT)
wrapper.place(x=12, y=100)
#player = tkvideo("outpy.mkv", wrapper, loop = 1, size = (300,150))
#player.play()

wrapper2 = tkinter.LabelFrame(port,bg="#EEEEF5", width=377, height=280)
wrapper2.pack(side=tkinter.LEFT)
wrapper2.place(x=12, y=340)






menubar = tkinter.Menu(port)

fileMenu = tkinter.Menu(menubar)

submenu = tkinter.Menu(fileMenu)

submenu.add_command(label="Single", command=set_1)
submenu.add_command(label="Double", command=set_2)
submenu.add_command(label="Tripel", command=set_3)
submenu.add_command(label="Quad", command=set_4)

fileMenu.add_cascade(label='Input', menu=submenu, underline=0)

fileMenu.add_separator()

menubar.add_cascade(label="Edit",  underline=0, menu=fileMenu)



c9 = tkinter.Button(toolbar,bd=1, width=35, height=35, command=show, bg="#4d5763")
c9.place(x=10, y=5)
c9.configure(image=run)

c10 = tkinter.Button(toolbar,bd=1, width=35, height=35,  command=reset2, bg="#4d5763")
c10.place(x=88, y=5)
c10.configure(image=resetimage)

c11 = tkinter.Button(toolbar, bd=1, width=35, height=35, command=recordvideo, bg="#4d5763")
c11.place(x=49, y=5)
c11.configure(image=record)





port.config(menu=menubar)
port.title('Madeena Monitoring System V1.2')
port.mainloop()  

