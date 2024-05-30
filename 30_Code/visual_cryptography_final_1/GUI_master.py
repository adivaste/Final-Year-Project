from tkinter import messagebox
from tkinter import * 
import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
import pandas as pd
import openpyxl
#import xlwrite,firebase.firebase_ini as fire
from tkinter import messagebox as ms
from pkg_resources import parse_version
if parse_version(Image.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS


##############################################+=============================================================

def runme():
    root = tk.Tk()
    root.configure(background="seashell2")
    #root.geometry("1300x700")
    import sqlite3
    my_conn = sqlite3.connect('face.db')

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Face Authentication")


    #++++++++++++++++++++++++++++++++++++++++++++
    #####For background Image
    image2 =Image.open('face.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


    lbl = tk.Label(root, text="Face Authentication System", font=('times', 40,' bold '), height=1, width=30,bg="Black",fg="indian red")
    lbl.place(x=330, y=5)

    frame_alpr = tk.LabelFrame(root, text="", width=280, height=400, bd=5, font=('times', 15, ' bold '),bg="seashell4")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=70, y=130)




    ################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 


    def Create_database():
            
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        cap = cv2.VideoCapture(0)
        
    #    id = input('enter user id')
        id=1
        
        sampleN=0
        
        while 1:
        
            ret, img = cap.read()
        
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
            for (x,y,w,h) in faces:
        
                sampleN=sampleN+1;
        
                cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                cv2.waitKey(100)
        
            cv2.imshow('img',img)
        
            cv2.waitKey(1)
        
            if sampleN > 40:
        
                break
        
        cap.release()
        entry2.delete(0,'end')
        cv2.destroyAllWindows()
    def mail():
        print("Mail Sending")
        from subprocess import call
        call(["python", "mail.py"])
    def update_label(str_T):
        #clear_img()
        result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
        result_label.place(x=450, y=400)

    def Train_database():
            
        recognizer =cv2.face.LBPHFaceRecognizer_create();
        
        path="facesData"
        
        def getImagesWithID(path):
        
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   
        
        # print image_path   
        
        #getImagesWithID(path)
        
            faces = []
        
            IDs = []
        
            for imagePath in imagePaths:      
        
        # Read the image and convert to grayscale
        
                facesImg = Image.open(imagePath).convert('L')
        
                faceNP = np.array(facesImg, 'uint8')
        
                # Get the label of the image
                
                samp = os.path.split(imagePath)
                ID= os.path.split(imagePath)[1].split(".")[1]
                print(samp, ID)
        
                # Detect the face in the image
        
                faces.append(faceNP)
        
                IDs.append(ID)
        
                cv2.imshow("Adding faces for traning",faceNP)
        
                cv2.waitKey(10)
        
            return np.array(IDs), faces
        
        Ids,faces  = getImagesWithID(path)
        recognizer.train(faces,Ids)
        
        recognizer.save("trainingdata.yml")
        
        cv2.destroyAllWindows()

    def Test_database():
        flag=0
        recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
    #    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);
        
        recognizer.read('trainingdata.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX
        #iniciate id counter
        id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person'] 
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        
        while True:
            ret, img =cam.read()
    #        img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))
            
            

            filename='pandas_to_excel.xls'
            dict = {
                'item1': 1
                }
            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
                
                if confidence > 50:
                
                    #print(id)
                    #name = names[id]
                    id = id
                    
                    print(type(id))
                    
                    #
                    #id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                    
                            
                    cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                    cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                    cv2.putText(img, 'Number of Faces : ' + str(len(faces)), (40, 40), font, 1, (255, 0, 0), 2)
                    update_label('Authenticated User Successful !')
                    
                    
                    cam.release()
                    cv2.destroyAllWindows()                      
                    #root.destroy()
                    # from subprocess import call
                    # call(["python","reg.py"])

                    messagebox.showinfo("Login Successful", "You have been logged in successfully.")
                
        
                else:
    #                print(confidence)
                    id = "unknown Person Identified"
                    confidence = "  {0}%".format(round(100 - confidence))
                    
                    cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                    cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                    
                
                    update_label('Unauthenticated User !')
                    messagebox.showinfo("Login Unsuccessful", "You are not logged in.")
            
            
    #        time.sleep(0.2)
            cv2.imshow('camera',img) 
    #        print(flag)
            if flag==10:
                flag=0
                cam.release()
                cv2.destroyAllWindows()
                from subprocess import call
        
            
        
            if cv2.waitKey(1) == ord('Q'):
                break

        
        
    def registration():
        
    ##### tkinter window ######
        
        print("Registration")
        from subprocess import call
        call(["python", "registration.py"]) 



    def display():
        
    ##### tkinter window ######
        
        print("Display")
        from subprocess import call
        call(["python", "display.py"]) 
            
    def ID():  
        
        framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=600,height=50, bd=5, font=('times', 14, ' bold '),bg="pink")
        framed.grid(row=0, column=0, sticky='nw')
        framed.place(x=500, y=100)
        my_conn = sqlite3.connect('face.db')
        r_set=my_conn.execute("SELECT * FROM User")
        i=0 # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                e =tk.Entry(framed, width=15, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
            

    #################################################################################################################
    def window():
        root.destroy()


    # button1 = tk.Button(frame_alpr, text="Registration Of User",bd=5, command=registration,width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    # button1.place(x=10, y=20)

    button1 = tk.Button(frame_alpr, text="Create Face Data",bd=5, command=Create_database,width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    button1.place(x=10, y=40)

    button2 = tk.Button(frame_alpr, text="Train Face Data",bd=5, command=Train_database, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    button2.place(x=10, y=100)

    button3 = tk.Button(frame_alpr, text="Face Authentication", bd=5,command=Test_database, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    button3.place(x=10, y=160)


    # button3 = tk.Button(frame_alpr, text="Display",bd=5, command=ID, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    # button3.place(x=10, y=80)


    # entry2=tk.Entry(frame_alpr,bd=5,width=7)
    # entry2.place(x=210, y=150)

    exit = tk.Button(frame_alpr, text="Exit",bd=5, command=window, width=20, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
    exit.place(x=10, y=320)



    root.mainloop()

runme()