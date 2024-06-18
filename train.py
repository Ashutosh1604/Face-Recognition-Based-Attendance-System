

from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",20,"bold"),bg="lightgreen",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

        img_top = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images\top.jpg")
        img_top=img_top.resize((1530, 325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="green",fg="white")
        b1_1.place(x=0,y=400,width=1530,height=60)
        



    def train_classifier(self):

        data_dir = (r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)



        
    

    
if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()