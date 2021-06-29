# ======================================= import dependences =======================================
from tkinter import * 
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk

# ======================================= importing face detector =======================================
import face_detector_image as fdi
import face_detector_video as fdv
import face_detector_video_live as fdvl

# ======================================= importing face recognizer =======================================
import face_recognizer_training as frt
import face_recognizer_prediction as frp

# ======================================= css =======================================
color = '#0CAFFF'
color_heading = '#0076CE'

font_heading = ('Times', 22, 'bold', 'underline')
font_label= ("Open Sans", 12)

padx = 8
pady = 8
ipadx = 8
ipady = 8
thickness = 1


# ======================================= root =======================================
root = Tk()
root.geometry('900x600')
root.title('Face Check ✅')

# ======================================= images =======================================
arrow1 = Image.open('./icons/arrow.png')
arrow2 = arrow1.resize((20, 20))
arrow = ImageTk.PhotoImage(arrow2)

label1_image_old = Image.open('./icons/face_detector.png')
label1_image = label1_image_old.resize((40, 40))

label2_image_old = Image.open('./icons/face_recognizer.png')
label2_image = label2_image_old.resize((40, 40))


# ================================== frame1 : face detector frame ===================================
frame1 = Frame(root)
frame1.pack()

# ======================================= frame2 : face recognizer frame =======================================
frame2 = Frame(root)
frame2.pack()


people = [ 'Elon Musk', 'Robert Downey' ]


# face detector functions 
def select_image():
    image_loc = filedialog.askopenfilename(initialdir="./images/", title="Image",  filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp'])]) 
    fdi.select_image = str(image_loc)

def select_video():
    video_loc = filedialog.askopenfilename(initialdir="./videos", title="Video",  filetypes=[('Video Files', ['.mp4', '.mov', '.wmv', '.avi', '.mkv' ])]) 
    fdv.select_video = str(video_loc)

#  face recognizer functions
def add_person():
    people.append( placeholder.get() )
    frp.people.append( placeholder.get() )
    frt.people.append( placeholder.get() )
    placeholder.delete(0,  END)

def remove_person():
    people.remove(placeholder.get())
    placeholder.delete(0,  END)

def see_people():
    label = Label(root, text=people )
    label.pack()

def predict_image():
    image_loc = filedialog.askopenfilename(initialdir="./images/", title="image",  filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp'])]) 
    frp.predict_image = str(image_loc)



# ====================================== frame1 : face detector =========================================== 

    # ------------ 1 -----------------
label_heading1 = Label( frame1, text='Face Detector', justify='center', fg=color_heading, font = font_heading )

label1_img = ImageTk.PhotoImage(label1_image)
label1_image = Label( frame1, image=label1_img)

    # ----------------- 2 -----------------
label1 = Label(frame1, text=f'Detect faces \n in image', bg=color, font=font_label )

arrow1 = Label(frame1, image = arrow)

select_image_button = Button( frame1, text="See image", command=select_image, highlightthickness = thickness, font = font_label )
select_image_button.config( highlightbackground = color, highlightcolor= color )

arrow2 = Label(frame1, image = arrow, justify='center')

face_detector_image = Button( frame1, text="Detect Faces in image", command=lambda : fdi.face_detector_image(), highlightthickness = thickness, font = font_label )
face_detector_image.config( highlightbackground = color, highlightcolor= color )

    # ----------------- 3 -----------------
label2 = Label(frame1, text=f'Detect faces \n in video', bg=color, font= font_label )

arrow3 = Label(frame1, image = arrow)

select_video_button = Button(frame1, text='Select Video', command=select_video, highlightthickness= thickness, font = font_label )
select_video_button.config( highlightbackground = color, highlightcolor= color )

arrow4 = Label(frame1, image = arrow )

face_detector_video = Button( frame1, text="Detect Faces in video", command=lambda : fdv.face_detector_video(), highlightthickness=thickness, font = font_label )
face_detector_video.config( highlightbackground = color, highlightcolor= color )

    # ----------------- 4 -----------------
label3 = Label(frame1, text=f'Detect faces \n in image', bg=color, font = font_label )

arrow5 = Label(frame1, image = arrow)

face_detector_video_live = Button( frame1, text="Detect Faces in live video", command=lambda : fdvl.face_detector_video_live(),  justify='center', highlightthickness=thickness, font = font_label )
face_detector_video_live.config( highlightbackground = color, highlightcolor= color )


# ========================================== grid frame1 ============================================

    # ----------------- 1 -----------------
label_heading1.grid         ( row=0, columnspan=5, pady=(20,20) )
label1_image.grid           ( row=0, column=4, pady=(10,20) )

    # ----------------- 2 -----------------
label1.grid                 ( row=1, column=0, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady )
arrow1.grid                 ( row=1, column=1, padx=padx, pady=pady )
select_image_button.grid    ( row=1, column=2, padx=padx, pady=pady )
arrow2.grid                 ( row=1, column=3, padx=padx, pady=pady )
face_detector_image.grid    ( row=1, column=4, padx=padx, pady=pady )

    # ----------------- 3 -----------------
label2.grid                 ( row=2, column=0, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady )
arrow3.grid                 ( row=2, column=1, padx=padx, pady=pady )
select_video_button.grid    ( row=2, column=2, padx=padx, pady=pady )
arrow4.grid                 ( row=2, column=3, padx=padx, pady=pady )
face_detector_video.grid    ( row=2, column=4, padx=padx, pady=pady )

    # ----------------- 4 -----------------
label3.grid                 ( row=3, column=0, padx=5, pady=5, ipadx=ipadx, ipady=ipady )
arrow5.grid                 ( row=3, column=1, columnspan=3, padx=padx, pady=pady )
face_detector_video_live.grid( row=3, column=2, columnspan=3, padx=padx, pady=pady, sticky=E )





# =================================== frame2 : face recognizer ========================================= 

    # ----------------- 1 -----------------
label_heading2 = Label( frame2, text='Face Recognizer', justify='center', fg=color_heading, font=font_heading )

label2_img = ImageTk.PhotoImage(label2_image)
label2_image = Label( frame2, image=label2_img)

    # ----------------- 2  -----------------
placeholder = Entry(frame2, width=20, highlightthickness=thickness, font=font_label )
placeholder.config( highlightbackground = color, highlightcolor= color )

arrow6 = Label(frame2, image = arrow, justify='center')

button_add_person = Button(frame2, text="Add Person" ,command=add_person, highlightthickness=thickness, font=font_label )
button_add_person.config( highlightbackground = color, highlightcolor= color )

button_remove = Button( frame2, text="Remove Person", command=remove_person, highlightthickness=thickness, font=font_label )
button_remove.config( highlightbackground = color, highlightcolor= color )

button_see_people = Button( frame2, text="See Persons", command=see_people, highlightthickness=thickness, font=font_label )
button_see_people.config( highlightbackground = color, highlightcolor= color )

    # ----------------- 3 -----------------
train_model = Button( frame2, text= "train_model", command=lambda: frt.train_model(), highlightthickness=thickness, font=font_label )
train_model.config( highlightbackground = color, highlightcolor= color )

arrow7 = Label(frame2, image = arrow, justify='center')

predict_image = Button(frame2, text="choose image...", command=predict_image, highlightthickness=thickness, font=font_label )
predict_image.config( highlightbackground = color, highlightcolor= color )

arrow8 = Label(frame2, image = arrow, justify='center')

face_recognizer = Button( frame2, text="Recognize face", command=lambda: frp.face_recognizer(), highlightthickness=thickness, font=font_label )
face_recognizer.config( highlightbackground = color, highlightcolor= color )



# ======================================== grid frame2 =============================================

    # ----------------- 1 -----------------
label_heading2.grid     ( row=0, pady=(50,20), columnspan=5 )
label2_image.grid       ( row=0, pady=(40,15), column=3, sticky=E )
    
    # ----------------- 2 -----------------
placeholder.grid        ( row=1, column=0, padx=padx, pady=pady+5 )
arrow6.grid             ( row=1, column=1, padx=padx, pady=pady+5 )
button_add_person.grid  ( row=1, column=2, padx=padx, pady=pady+5 )
button_remove.grid      ( row=1, column=3, padx=padx, pady=pady+5 )
button_see_people.grid  ( row=1, column=4, padx=padx, pady=pady+5 )
    
    # ----------------- 3 -----------------
train_model.grid        ( row=2, column=0, padx=padx, pady=pady+5 )
arrow7.grid             ( row=2, column=1, padx=padx, pady=pady+5 )
predict_image.grid      ( row=2, column=2, padx=padx, pady=pady+5 )
arrow8.grid             ( row=2, column=3, padx=padx, pady=pady+5 )
face_recognizer.grid    ( row=2, column=4, padx=padx, pady=pady+5 )
    

root.mainloop()