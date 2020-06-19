from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox

root=Tk()
root.title("Paint")
root.iconbitmap('paint.ico')
root.geometry("1000x1000")


b_color="black"
text_color="black"

#Change width function
def change_width(e):
    s_label.config(text='%0.0f'% float(slider.get()))

#Change eraser function
def change_eraser(e):   
    e_label.config(text='%0.0f'% float(e_slider.get()))
   
#Change brush color function
def change_brush_color():
    global b_color    
    b_color=colorchooser.askcolor(color=b_color)[1]
    c.bind('<B1-Motion>',paint)
    
#Change canvas color function
def change_canvas_color():
    global bg_color  
    bg_color='black'  
    bg_color=colorchooser.askcolor(color=bg_color)[1]
    c.config(bg=bg_color)
    c.bind('<B1-Motion>',paint)

#Clear screen function
def clear_screen():
    c.delete(ALL)
    c.config(bg="white")
    
#adding text up in canvas
def text_up():
    text1=StringVar
    text1=en.get()
    c.create_text(450,30,text=text1,fill=text_color)
    top.withdraw()
    
#adding text down in canvas
def text_down():
    text1=StringVar
    text1=en.get()
    c.create_text(450,370,text=text1,fill=text_color)
    top.withdraw()
    
    
#adding text left in canvas
def text_left():
    text1=StringVar
    text1=en.get()
    c.create_text(80,200,text=text1,fill=text_color)
    top.withdraw()
    
    
#adding text right in canvas
def text_right():
    text1=StringVar
    text1=en.get()
    c.create_text(820,200,text=text1,fill=text_color)
    top.withdraw()
    
    
#add text function
def add_text():
    global top,en
    top=Toplevel()
    top.geometry('310x70')
    l=Label(top,text="Enter the text")
    l.grid(row=0,column=0)
    en=Entry(top,width=50,relief=SUNKEN)
    en.grid(row=1,column=0)
    b=Button(top,text="OK",command=choose_position)
    b.grid(row=2,column=0)
    
     
#Save as function
def save():
    result=filedialog.asksaveasfilename(initialdir="C:\paint\images",filetypes=(("PNG files","*.png"),("ALL files","*.*")))
    if result.endswith(".png"):
        pass
    else:
        result=result+".png"
    if result:
        x=root.winfo_rootx()+c.winfo_x()
        y=root.winfo_rooty()+c.winfo_y()
        x1=x+c.winfo_width()
        y1=y+c.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)
    messagebox.showinfo("Image Saved","Your image has been saved successfully!!")
    
    
#paint function
def paint(e):
    #Brush parameters
    b_width='%0.0f'% float(slider.get())
    b_type=brush_type.get()
    x1=e.x-1
    y1=e.y-1    
    x2=e.x+1
    y2=e.y+1    
    c.create_line(x1,y1,x2,y2,fill=b_color,width=b_width,capstyle=b_type,smooth=True)

#Add text color function
def add_text_color():
    global text_color
    text_color=colorchooser.askcolor(color=text_color)[1]  

#Choosing posiitons
def choose_position():
    top.withdraw()
    global top1
    top1=Toplevel()
    top1.geometry('255x135')
    l1=Label(top1,text="Select text position:")
    l1.grid(row=0,column=0)  
    bup=Button(top1,text="UP",command=text_up).grid(row=1,column=2)
    bdown=Button(top1,text="DOWN",command=text_down).grid(row=3,column=2)
    bleft=Button(top1,text="LEFT",command=text_left).grid(row=2,column=1)
    bright=Button(top1,text="RIGHT",command=text_right).grid(row=2,column=3)
    exit=Button(top1,text="Close",command=top1.withdraw).grid(row=4,column=0)
    
#erase function
def erase():
    c.bind('<B1-Motion>',paint2)
    
def paint2(e):
    #Brush parameters
    b_width='%0.0f'% float(e_slider.get())
    b_type=PROJECTING
    x1=e.x-1
    y1=e.y-1    
    x2=e.x+1
    y2=e.y+1    
    c.create_line(x1,y1,x2,y2,fill="white",width=b_width,capstyle=b_type,smooth=True)
    
#Canvas parameters
w=900
h=400
c=Canvas(root,width=w,height=h,bg="white")
c.pack(pady=20,padx=20)
c.bind('<B1-Motion>',paint)

#Brush Options Frame
b_options_frame=Frame(root)
b_options_frame.pack(pady=20)

#Brush size Frame
b_size_frame=LabelFrame(b_options_frame,text="Brush Size")
b_size_frame.grid(row=0,column=0,padx=20)
#Brush Slider
slider=ttk.Scale(b_size_frame,from_=1,to=100,orient=VERTICAL,command=change_width,value=10)
slider.pack(pady=10,padx=10)
#Brush Slider Label
s_label=Label(b_size_frame,text=slider.get())
s_label.pack(pady=5)

#Eraser frame
eraser_frame=LabelFrame(b_options_frame,text="Eraser Size")
eraser_frame.grid(row=0,column=1,padx=20)
#Eraser slider
e_slider=ttk.Scale(eraser_frame,from_=1,to=100,orient=VERTICAL,command=change_eraser,value=2)
e_slider.pack(pady=10,padx=10)
#Eraser Slider Label
e_label=Label(eraser_frame,text=e_slider.get())
e_label.pack(pady=5)

#Brush type Frame
b_type_frame=LabelFrame(b_options_frame,text="Brush Type")
b_type_frame.grid(row=0,column=2,padx=20)
brush_type=StringVar()
brush_type.set("round")
#Radio buttons for brush type
b1=Radiobutton(b_type_frame,text="Round",value="round",variable=brush_type).pack(anchor=W)
b2=Radiobutton(b_type_frame,text="Slash",value="butt",variable=brush_type).pack(anchor=W)
b3=Radiobutton(b_type_frame,text="Diamond",value="projecting",variable=brush_type).pack(anchor=W)

#Text and eraser frames
text_eraser_frame=LabelFrame(b_options_frame,text="Text and Eraser")
text_eraser_frame.grid(row=0,column=3,padx=20)
#text button 
text_button=Button(text_eraser_frame,text="Add text",command=add_text)
text_button.pack(pady=10,padx=10)
text_color_button=Button(text_eraser_frame,text="Add text color",command=add_text_color)
text_color_button.pack(pady=10,padx=10)
#Erase button
erase_button=Button(text_eraser_frame,text="Eraser",command=erase)
erase_button.pack(pady=10,padx=10)


#Change color frame
color_frame=LabelFrame(b_options_frame,text="Change colors")
color_frame.grid(row=0,column=4,padx=20)
#Adding buttons
b_color_button=Button(color_frame,text="Brush Color",command=change_brush_color)
b_color_button.pack(pady=10,padx=10)
c_color_button=Button(color_frame,text="Canvas Color",command=change_canvas_color)
c_color_button.pack(pady=10,padx=10)


#Options frame
options_frame=LabelFrame(b_options_frame,text="Program Options")
options_frame.grid(row=0,column=5,padx=20)
#Clear button
clear_button=Button(options_frame,text="Clear screen",command=clear_screen)
clear_button.pack(pady=10,padx=10)
#Save as button
save_button=Button(options_frame,text="Save As PNG",command=save)
save_button.pack(pady=10,padx=10)
#Exit button
exit_button=Button(options_frame,text="Exit",command=root.quit)
exit_button.pack(pady=10,padx=10)


root.mainloop()