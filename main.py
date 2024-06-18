
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Face_Recognition_System:
    
    
    def __init__(self, root):
         self.root = root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recognition System")

#         # # first image
         img1 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/GEHU.jpg")
         img1 = img1.resize((550, 130), Image.Resampling.LANCZOS)  #setting size and convert hight level image to low level
         self.photoimg1 = ImageTk.PhotoImage(img1)        #store image in variable

         f_lbl = Label(self.root, image=self.photoimg1)
         f_lbl.place(x=0, y=0, width=550, height=130)  

#         # second image
         img2 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/p.jpg")
         img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
         self.photoimg2 = ImageTk.PhotoImage(img2)

         f_lbl = Label(self.root, image=self.photoimg2)
         f_lbl.place(x=550, y=0, width=550, height=130)

#         # # third image 
         img3 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/geu.jpg")
         img3 = img3.resize((550, 130), Image.Resampling.LANCZOS)
         self.photoimg3 = ImageTk.PhotoImage(img3)

         f_lbl = Label(self.root, image=self.photoimg3)
         f_lbl.place(x=1000, y=0, width=550, height=130)

#         # background image
         img4 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/face-recognition-logo.jpeg")
         img4 = img4.resize((1550, 790), Image.Resampling.LANCZOS)
         self.photoimg4 = ImageTk.PhotoImage(img4)
         bg_img = Label(self.root, image=self.photoimg4)
         bg_img.place(x=0, y=130, width=1550, height=790)

         title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                           font=("Algerian", 35, "bold"), bg="white")
         title_lbl.place(x=0, y=0, width=1550, height=45)  # using .place u can place things at any part of the window

        # different buttons with images
        # student button
         img5 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/stu.jpg")
         img5 = img5.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg5 = ImageTk.PhotoImage(img5)

         btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
         btn1.place(x=100, y=80, width=195, height=195)

         btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn1_1.place(x=100, y=245, width=195, height=40)

#         # Face Detection button
         img6 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/face-detector.jpg")
         img6 = img6.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg6 = ImageTk.PhotoImage(img6)

         btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_data)
         btn2.place(x=400, y=80, width=195, height=195)

         btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn2_2.place(x=400, y=245, width=195, height=40)

#         # attendance button
         img7 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/face.jpg")
         img7 = img7.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg7 = ImageTk.PhotoImage(img7)

         btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
         btn3.place(x=700, y=80, width=195, height=195)

         btn3_3 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn3_3.place(x=700, y=245, width=195, height=40)

#         # Help Desk button
         img8 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/help.jpg")
         img8 = img8.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg8 = ImageTk.PhotoImage(img8)

         btn4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
         btn4.place(x=1000, y=80, width=195, height=195)

         btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn4_4.place(x=1000, y=245, width=195, height=40)

#         # train data button
         img9 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/train.png")
         img9 = img9.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg9 = ImageTk.PhotoImage(img9)

         btn5 = Button(bg_img, image=self.photoimg9,command=self.train_data, cursor="hand2")
         btn5.place(x=100, y=350, width=195, height=195)

         btn5_5 = Button(bg_img, text="Train Data",command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn5_5.place(x=100, y=525, width=195, height=40)

#         # Photos button
         img10 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/photos.jpg")
         img10 = img10.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg10 = ImageTk.PhotoImage(img10)

         btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
         btn6.place(x=400, y=350, width=195, height=195)

         btn6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn6_6.place(x=400, y=525, width=195, height=40)

#         # Developer button
         img11 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/developer.jpg")
         img11 = img11.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg11 = ImageTk.PhotoImage(img11)

         btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
         btn7.place(x=700, y=350, width=195, height=195)

         btn7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn7_7.place(x=700, y=525, width=195, height=40)

#         # Exit button
         img12 = Image.open(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\Images/exit-sign-neon-style_77399-144.jpg")
         img12 = img12.resize((195, 195), Image.Resampling.LANCZOS)
         self.photoimg12 = ImageTk.PhotoImage(img12)

         btn8 = Button(bg_img, image=self.photoimg12, cursor="hand2")
         btn8.place(x=1000, y=350, width=195, height=195)

         btn8_8 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="black", fg="white")
         btn8_8.place(x=1000, y=525, width=195, height=40)

    def open_img(self):
         os.startfile(r"C:\Users\ACER\OneDrive\Desktop\final year project\Facial-Recognition-Based-Student-Attendance-System-main\data")

# #     # =================================== Functions =========================================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)

    def face_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Attendance(self.new_window)


# # defining object
if __name__ == "__main__":
     root = Tk()
     obj = Face_Recognition_System(root)
     root.mainloop()

