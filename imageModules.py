from tkinter import *
from PIL import *
from scipy import misc 
import numpy
import os
from tkinter import colorchooser
from PIL import ImageGrab
from PIL import ImageEnhance
from skimage import exposure,data
from transforms import RGBTransform
from tkinter import ttk

canvas_width=1300
canvas_height=600
def RotateByAngle(root,rotate_image,canvas,event=NONE):
 top=Toplevel(root)
 a=StringVar()
 b=BooleanVar()
 c=BooleanVar()
 d=BooleanVar() 
 e=BooleanVar()
 f=BooleanVar()
 g=StringVar()
 def getColor():
  color = colorchooser.askcolor()[1] 
  l1.config(bg=color)
  canvas1.config(bg=color)
  canvas2.config(bg=color)
 
 def Ok():
  img=Image.open("rotate.jpg").resize((250,350),Image.ANTIALIAS)
  top.img2=ImageTk.PhotoImage(img)
  canvas.delete("all")
  canvas.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=top.img2)
  top.destroy()
 
 def stateChange(event=NONE):
  if b.get()==True:
   check2.config(state=ACTIVE)
  else:
    check2.config(state=DISABLED)
 
 def sharpen(i):
  img=Image.open(i)
  top.img_sharp=img.filter(ImageFilter.SHARPEN)
  canvas2.create_image(20,20,anchor='nw',image=top.img_sharp)
 
 def rotate(i):
  canvas2.delete("all")
  img=Image.open(i)
  if(d.get()==True):
   img2=img.rotate(int(a.get()),expand=b.get(),resample=Image.NEAREST)
  else:
   img2=img.rotate(int(a.get()),expand=b.get(),resample=Image.BICUBIC)
  img3=img.rotate(0)
  top.img2=ImageTk.PhotoImage(img2)
  top.img3=ImageTk.PhotoImage(img3)
  if c.get()==True:
   canvas2.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=top.img3)
  canvas1.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=top.img3)
  canvas2.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=top.img2)
  misc.imsave("rotate.jpg",img2)
 
 top.title("Rotate By Angle")
 frame1=Frame(top,bd=2)
 frame1.pack(side=TOP)
 Label(frame1,text="Original image").grid(row=0,column=0)
 Label(frame1,text="New image").grid(row=0,column=2)
 canvas_height=120
 canvas_width=180
 canvas1=Canvas(frame1,bg='white',width=canvas_width,height=canvas_height)
 canvas1.grid(row=1,column=0)
 img1=Image.open(rotate_image).resize((50,70),Image.ANTIALIAS)
 img2=ImageTk.PhotoImage(img1)
 canvas1.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=img2)
 canvas2=Canvas(frame1,bg='white',width=180,height=120)
 canvas2.grid(row=1,column=2)
 canvas2.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=img2)
 misc.imsave("haha.jpg",img1)
 
 label1=LabelFrame(top,text="Options",bd=2,relief=GROOVE)
 label1.pack(anchor=W)
 Label(label1,text="Angle:").grid(row=0,column=0)
 a.set("0")
 image="haha.jpg"
 s=Spinbox(label1,from_=-360,to=360,textvariable=a,increment=1,command=lambda :rotate(image))
 s.grid(row=1,column=0)
 F2=Frame(label1,bd=2)
 F2.grid(row=2,column=0)
 check1=Checkbutton(F2,text="Keep original image/canvas size",variable=b).grid(row=2,column=0,sticky='w')
 label1.bind_all("<Button-1>",stateChange)
 b.set(False)
 check2=Checkbutton(F2,text="Keep original image as background",variable=c,state=DISABLED)
 check2.grid(row=3,column=0,sticky='w')
 c.set(False)
 Checkbutton(F2,text="Use new rotation method (faster for larger images without antialiasing)",variable=d).grid(row=4,column=0,sticky='w')
 d.set(False)
 Checkbutton(F2,text="Enabel antialiasing (better quality but slower)",variable=e).grid(row=5,column=0,sticky='w')
 e.set(True)
 Checkbutton(F2,text="Select 'best' old image in the result image (angle: -90 - 90 deg)").grid(row=6,column=0,sticky='w')
 
 F1=Frame(label1,bd=2)
 F1.grid(row=7,column=0)
 check5=Checkbutton(F1,text="Apply Sharpen after rotation:",variable=f).grid(row=0,column=0,sticky='w')
 f.set(False)
 if(f.get()==True):
  check5.conf(command=lambda :sharpen(image))
 Entry(F1,width=5,textvariable=g).grid(row=0,column=1)
 g.set(0)
 #F1.bind_all("<Button-1>",stateChange)
 Label(F1,text="(1 - 99)").grid(row=0,column=2)
 Label(F1,text="Set background color:\n(4,8,24 BPP images)").grid(row=1,column=0)
 l1=Label(F1,width=10)
 l1.grid(row=1,column=1,columnspan=1)
 Button(F1,text="Choose",command=getColor).grid(row=1,column=3)
 Label(F1,text="Hint: click into the image (main window) to set a special color.").grid(row=2,column=0,columnspan=3)
 
 F2=Frame(top)
 F2.pack(side=BOTTOM)
 Button(F2,text="Ok",padx=25,command=Ok).grid(row=0,column=1,padx=5,pady=5)
 Button(F2,text="Cancel",padx=15,command=top.destroy).grid(row=0,column=2,padx=5,pady=5)
 
 top.mainloop()

def CreateTitleImage(image,canvas,master,event=NONE):
 a=IntVar()
 b=IntVar()
 c=IntVar()
 d=IntVar()
 e=IntVar()
 f=IntVar()
 master.color="white"
 
 def ok():
  if(int(a.get())!=0 and int(b.get())!=0):
   x=int(a.get())
   y=int(b.get())
   img=Image.open(image)
   height,width=img.size
   vh=int(height/x)
   vw=int(width/y)
   new_im=Image.new('RGB',(height,width),color=master.color)
   for i in range(int(e.get()),height,vh):
    for j in range(int(f.get()),width,vw):
     im=Image.open(image).resize((vh-2*int(e.get()),vw-2*int(f.get())),Image.ANTIALIAS)
     new_im.paste(im,(i,j))
    new_im.save('tile.jpg')
   img=Image.open("tile.jpg")
   root.img2=ImageTk.PhotoImage(img)
   canvas.delete("all")
   canvas.create_image(canvas_width/2,(canvas_height/2)+10,anchor="center",image=root.img2)
  if(int(c.get())!=0 and int(d.get())!=0):
   x=int(c.get())
   y=int(d.get())
   img=Image.open(image)
   height,width=img.size
   nh=int(height/x)
   nw=int(width/x)
   vh=int(height/nh)
   vw=int(width/nw)
   new_im=Image.new('RGB',(height,width),color=master.color)
   for i in range(int(e.get()),height,vh):
    for j in range(int(f.get()),width,vw):
     im=Image.open(image).resize((vh-2*int(e.get()),vw-2*int(f.get())),Image.ANTIALIAS)
     new_im.paste(im,(i,j))
    new_im.save('tile.jpg')
   img=Image.open("tile.jpg")
   root.img2=ImageTk.PhotoImage(img)
   canvas.delete("all")
   canvas.create_image(canvas_width/2,(canvas_height/2)+10,anchor="center",image=root.img2)
  
 def getColor():
  master.color = colorchooser.askcolor()[1] 
  l1.config(bg=master.color)
 
 def cancel():
  root.img2=ImageTk.PhotoImage(Image.open(image))
  canvas.create_image(canvas_width/2,(canvas_height/2)+10,anchor="center",image=root.img2)
  root.destroy()
 
 def okAndSave():
  ok()
  img=Image.open("tile.jpg")
  misc.imsave("1.jpg",img)
  root.destroy()
 
 root=Toplevel(master)
 root.title("Create Title image")
 frame1=Frame(root,bd=2,relief=GROOVE)
 frame1.pack(side=TOP)
 label1=LabelFrame(frame1,text="Method 1:Set number of tiles",padx=10,pady=10)
 label1.pack(padx=10,pady=10)
 Label(label1,text="Width").grid(row=0,column=0)
 Entry(label1,textvariable=a).grid(row=0,column=1)
 a.set(0)
 Label(label1,text="Height").grid(row=0,column=2)
 Entry(label1,textvariable=b).grid(row=0,column=3)
 b.set(0)
 
 label2=LabelFrame(frame1,text="Method 2:Set Final image dimension in pixel",padx=10,pady=10)
 label2.pack(padx=10,pady=10)
 Label(label2,text="Width").grid(row=1,column=0)
 Entry(label2,width=10,textvariable=c).grid(row=1,column=1)
 c.set(0)
 Label(label2,text="Height").grid(row=1,column=3)
 Entry(label2,width=10,textvariable=d).grid(row=1,column=4)
 d.set(0)
 Radiobutton(label2,text="pixels",value=1,variable='e').grid(row=0,column=5)
 Radiobutton(label2,text="cm",value=2,variable='e').grid(row=1,column=5)
 Radiobutton(label2,text="inches",value=3,variable='e').grid(row=2,column=5)
 Label(label2,text="Some standard dimensions :").grid(row=2,column=0,columnspan=2)
 Button(label2,text="A3",width=10).grid(row=3,column=0,columnspan=2)
 Button(label2,text="A4",width=10).grid(row=4,column=0,columnspan=2)
 Button(label2,text="Letter",width=10).grid(row=5,column=0,columnspan=2)
 Label(label2,text="DPI :").grid(row=3,column=3)
 Entry(label2,width=10,text="75").grid(row=3,column=4)
 Radiobutton(label2,text="Portrait",value=1,variable='f').grid(row=4,column=3)
 Radiobutton(label2,text="Landscape",value=2,variable='f').grid(row=5,column=3)
  
 label3=LabelFrame(frame1,text="Set spaces between images (pixels):",padx=10,pady=10)
 label3.pack(padx=10,pady=10)
 Label(label3,text="Horizontal:").grid(row=0,column=0)
 Entry(label3,text="1",width=10,textvariable=e).grid(row=0,column=1)
 e.set(0)
 Label(label3,text="Vertical:").grid(row=0,column=2)
 Entry(label3,text="1",width=10,textvariable=f).grid(row=0,column=3)
 f.set(0)
 Label(label3,text="(pixel)").grid(row=0,column=4)
 Label(label3,text="Space color:").grid(row=1,column=0)
 l1=Label(label3,bg="white",width=20)
 l1.grid(row=1,column=1,columnspan=2)
 Button(label3,text="Choose",width=10,command=getColor).grid(row=1,column=3)
 Label(label3,text="Hint : click into the image (main window) to set a special color.").grid(row=2,column=0,columnspan=5)
 
 label4=Frame(frame1,bd=2)
 label4.pack()
 Button(label4,text="Apply to current image",width=10,command=ok,padx=30).grid(row=0,column=0)
 Button(label4,text="Ok",width=10,command=okAndSave).grid(row=0,column=1)
 Button(label4,text="Cancel",width=10,command=cancel).grid(row=0,column=2)
 root.mainloop()


def CreateNewImage(canvas,master,event=NONE):
 root=Toplevel(master)
 a=StringVar()
 b=StringVar()
 c=StringVar()
 d=StringVar()
 
 def ok():
  height=int(a.get())
  width=int(b.get())
  canvas.create_rectangle(10,10,height,width,fill=master.color)
 
 def getColor():
  master.color = colorchooser.askcolor()[1] 
  l1.config(bg=master.color)
 
 root.title("Create new image")
 frame3=Frame(root)
 frame3.pack(side=TOP)
 frame1=LabelFrame(frame3,text="Define new image",bd=2,relief=GROOVE)
 frame1.pack(side=LEFT)
 Label(frame1,text="Image width:").grid(row=0,column=0)
 Entry(frame1,width=10,textvariable=a).grid(row=0,column=1)
 a.set(0)
 Label(frame1,text="pixel").grid(row=0,column=2)
 Label(frame1,text="Image height:").grid(row=1,column=0)
 Entry(frame1,width=10,textvariable=b).grid(row=1,column=1)
 b.set(0)
 Label(frame1,text="pixel").grid(row=1,column=2)
 Label(frame1,text="Image X-DPI:").grid(row=2,column=0)
 Entry(frame1,width=10,textvariable=c).grid(row=2,column=1)
 c.set(0)
 Label(frame1,text="Image Y-DPI:").grid(row=3,column=0)
 Entry(frame1,width=10,textvariable=d).grid(row=3,column=1)
 d.set(0)
 master.color="black"
 l1=Label(frame1,width=25,bg=root.color)
 l1.grid(row=4,column=0,columnspan=3)
 Button(frame1,text="          Background color        ",command=getColor).grid(row=5,column=0,columnspan=3,padx=5,pady=5)
 
 frame2=LabelFrame(frame3,text="Colors:",bd=2,relief=GROOVE)
 frame2.pack(side=RIGHT)
 Radiobutton(frame2,text="Black/White (1 BPP)",value=1,underline=0,padx=5,pady=8).pack(anchor=W)
 Radiobutton(frame2,text="16 Colors (4 BPP)",value=2,underline=0).pack(anchor=W)
 Radiobutton(frame2,text="256 Colors (8 BPP)",value=3,underline=0).pack(anchor=W)
 Radiobutton(frame2,text="16.7 Million colors (24 BPP)",value=4,underline=0).pack(anchor=W)
 Checkbutton(frame2,text="Greyscale image").pack(anchor=W)
 
 frame3=Frame(root)
 frame3.pack(side=BOTTOM)
 Label(frame3,text="").grid(row=0,column=0)
 Button(frame3,text="      Ok      ",command=ok).grid(row=0,column=1,padx=5,pady=5)
 Button(frame3,text="   Cancel   ").grid(row=0,column=2,padx=5,pady=5)
 Label(frame3,text="").grid(row=0,column=3)
 root.mainloop()


def CreatePanoramaImage(event=NONE):
 root=Tk()
 root.title("Create panorama image")
 frame1=LabelFrame(root,text="Direction:",bd=2,relief=GROOVE)
 frame1.pack(side=TOP,anchor=W,fill=X)
 Radiobutton(frame1,text="Horizontal - add images at the right side of previous ones",value=1).pack(anchor=W)
 Radiobutton(frame1,text="Vertical - add images below previous ones",value=1).pack(anchor=W)
 Label(root,text='Hint: you can create multi-row panorama images in the Thumbnails window using the "Create Contact Sheet" feature.',bd=2,relief=GROOVE).pack()
 frame2=Frame(root,bd=2,relief=GROOVE)
 frame2.pack()
 Label(frame2,text="Input images:").grid(row=0,column=0)
 Label(frame2,text="").grid(row=0,column=1)
 Label(frame2,text="").grid(row=0,column=2)
 Button(frame2,text="   Add current file   ").grid(row=0,column=2)
 Label(frame2,text="").grid(row=0,column=4)
 Label(frame2,text="").grid(row=0,column=5)
 text=Text(frame2,height=10,width=60)
 text.grid(row=1,column=0,rowspan=5,columnspan=3)
 scroll=Scrollbar(frame2,orient=HORIZONTAL,command=text.xview)
 scroll.grid(row=5,column=0,columnspan=3,sticky='nsew')
 text['xscrollcommand']=scroll.set
 Button(frame2,text="     Add images    ").grid(row=1,column=3)
 Button(frame2,text=" Remove images  ").grid(row=2,column=3)
 Button(frame2,text="    Sort images     ").grid(row=3,column=3)
 Button(frame2,text=" Move images up ").grid(row=4,column=3)
 Button(frame2,text="Move images down").grid(row=5,column=3)
 Checkbutton(frame2,text='Insert filename into images (top left corner,options from the "Insert-Text" diaog)')
 
 frame3=LabelFrame(root,text="Add space between images:",bd=2,relief=GROOVE)
 frame3.pack(fill=X)
 Label(frame3,text="Spacing").grid(row=0,column=0)
 Entry(frame3,text="0",width=5).grid(row=0,column=1)
 Label(frame3,text="pixels (can be negative)").grid(row=0,column=2)
 Label(frame3,text="Space color:").grid(row=1,column=0)
 Entry(frame3,width=50).grid(row=1,column=1,columnspan=5)
 Button(frame3,text="   Choose   ").grid(row=1,column=6)
 
 frame4=Frame(root)
 frame4.pack()
 Label(frame4,text="").grid(row=0,column=0)
 Button(frame4,text="   Create image   ",underline=3).grid(row=0,column=1)
 Button(frame4,text="       Cancel        ",underline=8).grid(row=0,column=2)
 Label(frame4,text="").grid(row=0,column=3)
 root.mainloop()


def ChangeCanvasSize(event=NONE):
 root=Tk()
 root.title("Add image border (Canvas size)")
 frame1=LabelFrame(root,text="Method 1 :Set border dimensions in pixel:",bd=2,relief=GROOVE)
 frame1.pack(fill=X)
 Label(frame1,text="Left side:").grid(row=0,column=0)
 Entry(frame1,width=5).grid(row=0,column=1)
 Label(frame1,text="Right side:").grid(row=0,column=2)
 Entry(frame1,width=5).grid(row=0,column=3)
 Label(frame1,text="Top side:").grid(row=1,column=0)
 Entry(frame1,width=5).grid(row=1,column=1)
 Label(frame1,text="Bottom side:").grid(row=1,column=2)
 Entry(frame1,width=5).grid(row=1,column=3)
 Label(frame1,text="Note: border values can be negative numbers").grid(row=2,column=0,columnspan=3)
 Checkbutton(frame1,text="if negative values used: put the border on the inside").grid(row=3,column=0,columnspan=4)
 
 frame2=LabelFrame(root,text="Method 2: Set total canvas dimensions in pixels:",bd=2,relief=GROOVE)
 frame2.pack(anchor=W,fill=X)
 frame3=Frame(frame2)
 frame3.pack(anchor=W)
 Label(frame3,text="Width").grid(row=0,column=0)
 Entry(frame3,width=5).grid(row=0,column=1)
 Label(frame3,text="Height").grid(row=0,column=2)
 Entry(frame3,width=5).grid(row=0,column=3)
 Label(frame3,text="Anchor (start corner):").grid(row=1,column=0)
 
 frame4=Frame(frame2)
 frame4.pack()
 r1=Frame(frame4)
 r1.grid(row=0,column=0)
 Radiobutton(r1,text="Left top",value=1,variable="e").pack(anchor=W)
 Radiobutton(r1,text="Left middle",value=2,variable="e").pack(anchor=W)
 Radiobutton(r1,text="Left bottom",value=3,variable="e").pack(anchor=W)
 r2=Frame(frame4)
 r2.grid(row=0,column=1)
 Radiobutton(r2,text="Middle top",value=4,variable="e").pack(anchor=W)
 Radiobutton(r2,text="Center",value=5,variable="e").pack(anchor=W)
 Radiobutton(r2,text="Middle bottom",value=6,variable="e").pack(anchor=W)
 r3=Frame(frame4)
 r3.grid(row=0,column=2)
 Radiobutton(r3,text="Rigth top",value=7,variable="e").pack(anchor=W)
 Radiobutton(r3,text="Right middle",value=8,variable="e").pack(anchor=W)
 Radiobutton(r3,text="Right bottom",value=9,variable="e").pack(anchor=W)
 
 frame5=Frame(root,bd=2,relief=GROOVE)
 frame5.pack(anchor=W)
 Label(frame5,text="Canvas color:").grid(row=0,column=0)
 Label(frame5,bg="black",width=20).grid(row=0,column=1,columnspan=2)
 Button(frame5,text="        Choose          ").grid(row=0,column=3,padx=5,pady=5)
 Label(frame5,text="Hint: click into the image (main window) to set a specific color").grid(row=1,column=0,columnspan=4)
 
 frame6=Frame(root)
 frame6.pack(fill=X)
 Button(frame6,text="Apply to current image",padx=0).grid(row=0,column=0,padx=20,pady=5)
 Button(frame6,text="Ok",padx=50).grid(row=0,column=2,padx=20,pady=5)
 Button(frame6,text="Undo",padx=45).grid(row=1,column=0,padx=20,pady=5)
 Button(frame6,text="Cancel",padx=43).grid(row=1,column=2,padx=20,pady=5)
 root.mainloop()


def DecreaseColorDepth(event=NONE):
 root=Tk()
 root.title("Decrease color depth")
 frame1=LabelFrame(root,text="Colors:",bd=2,relief=GROOVE)
 frame1.pack(fill=X)
 Radiobutton(frame1,text="65536 Colors (24 BPP,simple RGB-565)",value=1,variable="e").pack(anchor=W)
 Radiobutton(frame1,text="256 Colors (8 BPP)",value=2,variable="e").pack(anchor=W)
 Radiobutton(frame1,text="16 Colors (4 BPP)",value=3,variable="e").pack(anchor=W)
 Radiobutton(frame1,text="2 Colors (black/white) (1 BPP)",value=4,variable="e").pack(anchor=W)
 Radiobutton(frame1,text="Custom:",value=5,variable="e").pack(anchor=W)
 Entry(frame1,width=5).pack(anchor=W)
 Label(frame1,text="(2-256 colors)").pack(anchor=W)
 Checkbutton(frame1,text="Use Floyd-Steinberg dithering (for max: 256 colors)").pack(anchor=W)
 Checkbutton(frame1,text="Use best color quality (slower for large image)").pack(anchor=W)
 Checkbutton(frame1,text="Make grayscale image").pack(anchor=W)
 
 frame2=Frame(root)
 frame2.pack()
 Button(frame2,text="Ok",padx=40).grid(row=0,column=1,padx=10,pady=5)
 Button(frame2,text="Cancel",padx=30).grid(row=0,column=2,padx=10,pady=5)
 root.mainloop()
 

def ColorCorrection(c1,image,root,event=None):
 master=Toplevel(root)
 a=StringVar()
 b=StringVar()
 c=StringVar()
 d=StringVar()
 e=StringVar()
 f=StringVar()
 g=StringVar()
 master.image=image 
 canvas_width=250
 canvas_height=150 
 def calcBrightness(image):
  greyscale_image = image.convert('L')
  histogram = greyscale_image.histogram()
  pixels = sum(histogram)
  brightness = scale = len(histogram)
  for index in range(0, scale):
    ratio = histogram[index] / pixels
    brightness += ratio * (-scale + index) 
  return 1 if brightness == 255 else brightness / scale
 
 
 def Ok():
  c1.delete("all")
  img=Image.open(image).resize((250,350).Image.ANTIALIAS)
  master.img2=ImageTk.PhotoImage(img)
  c1.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=master.img2)
  master.destroy()
 
 def getSeta(val):
  val1=int(val)
  a.set(str(val1))
  i=int(str(int(a.get())+255))
  im=Image.open(master.image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  enhancer=ImageEnhance.Brightness(im)
  img=enhancer.enhance(i*0.019)
  master.img2=ImageTk.PhotoImage(img)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 def getSetb(val):
  b.set(val)
  i=int(str(b.get()))
  im=Image.open(master.image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  img2=im.convert('RGB')
  red=RGBTransform().mix_with((255,0,0),factor=(i*0.0039)).applied_to(img2)
  master.img2=ImageTk.PhotoImage(red)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 def getSetc(val):
  c.set(val)
  i=int(str(c.get()))
  im=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  img2=im.convert('RGB')
  blue=RGBTransform().mix_with((0,255,0),factor=(i*0.0039)).applied_to(img2)
  master.img2=ImageTk.PhotoImage(blue)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 def getSetd(val):
  d.set(val)
  i=int(str(d.get()))
  im=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  img2=im.convert('RGB')
  green=RGBTransform().mix_with((0,0,255),factor=(i*0.0039)).applied_to(img2)
  master.img2=ImageTk.PhotoImage(green)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 
 def getSete(val):
  e.set(val)
  i=int(str(e.get()))
  im=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  enhancer=ImageEnhance.Contrast(im)
  img=enhancer.enhance(i*0.039)
  master.img2=ImageTk.PhotoImage(img)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 def getSetf(val):
  f.set(val)
  i=int(str(f.get()))
  im=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im)
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  img=data.imread(image)
  gamma_image=exposure.adjust_gamma(img,i)
  misc.imsave("gamma.jpg",gamma_image)
  gamma_image1=Image.open("gamma.jpg").resize((new_width,new_height),Image.ANTIALIAS)
  master.img2=ImageTk.PhotoImage(gamma_image1)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
  
 def getSetg(val):
  g.set(val)
  i=int(str(g.get()))
  im=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
  master.img1=ImageTk.PhotoImage(im);
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img1)
  enhancer=ImageEnhance.Color(im)
  img=enhancer.enhance(i*0.019)
  master.img2=ImageTk.PhotoImage(img)
  canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 
 master.title("Color corrections")
 frame1=Frame(master)
 frame1.grid(row=0,column=0)
 
 F1=Frame(frame1)
 F1.pack(side=TOP,fill=X)
 Label(F1,text="Original image").pack();
 canvas1=Canvas(F1,bg='white',width=250,height=150,bd=2)
 canvas1.pack()
 
 new_width=100
 new_height=150
 img=Image.open(image).resize((new_width,new_height),Image.ANTIALIAS)
 master.img2=ImageTk.PhotoImage(img)
 canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 misc.imsave("abc.jpg",img)
 
 F2=LabelFrame(frame1,text="Brightness:",bd=1,relief=GROOVE)
 F2.pack(fill=X)
 Sa=Scale(F2,length=200,from_=-255.0,to=255,orient=HORIZONTAL,sliderlength=15,tickinterval=1,command=getSeta)
 Sa.grid(row=0,column=0)
 #Sa.set(-255+(calcBrightness(Image.open(image))*150))
 Sa.set(-201)
 Entry(F2,width=4,textvariable=a).grid(row=0,column=1)
 a.set(str(Sa.get()-255))
 
 F3=LabelFrame(frame1,text="Color balance:",bd=1,relief=GROOVE)
 F3.pack(fill=X)
 Scale(F3,length=200,from_=-255.0,to=255,orient=HORIZONTAL,command=getSetb,sliderlength=15,tickinterval=1).grid(row=0,column=0)
 Entry(F3,width=4,textvariable=b).grid(row=0,column=1)
 b.set(0)
 Scale(F3,length=200,from_=-255.0,to=255,orient=HORIZONTAL,command=getSetc,sliderlength=15,tickinterval=1).grid(row=1,column=0)
 Entry(F3,width=4,textvariable=c).grid(row=1,column=1)
 Scale(F3,length=200,from_=-255.0,to=255,orient=HORIZONTAL,command=getSetd,sliderlength=15,tickinterval=1).grid(row=2,column=0)
 Entry(F3,width=4,textvariable=d).grid(row=2,column=1)
 
 F4=LabelFrame(frame1,text="Profiles:",bd=1,relief=GROOVE)
 F4.pack(fill=X)
 v1=StringVar()
 v1.set("            ")
 OptionMenu(F4,v1,"","","","","","","","","","").grid(row=0,column=0,columnspan=3,padx=50)
 Button(F4,text="Load",padx=10).grid(row=1,column=0,padx=5,pady=5)
 Button(F4,text="delete",padx=10).grid(row=1,column=1,padx=5,pady=5)
 Button(F4,text="Save",padx=10).grid(row=1,column=2,padx=5,pady=5)
 
 F5=Frame(frame1)
 F5.pack(fill=X)
 Label(F5,text="Hint: click into original image (bright areas) to").pack(anchor=W)
 Label(F5,text="change the White Balance (RGB values)").pack(anchor=W)
 
 frame2=Frame(master)
 frame2.grid(row=0,column=1)
 F6=Frame(frame2)
 F6.pack(side=TOP,fill=X)
 Label(F6,text="New image").pack()
 canvas=Canvas(F6,bg="white",width=250,height=150,bd=2)
 canvas.pack()
 canvas.create_image(canvas_width/2,canvas_height/2,anchor="center",image=master.img2)
 
 F7=LabelFrame(frame2,text="Contrast:",bd=1,relief=GROOVE,pady=5)
 F7.pack(fill=X)
 Scontrast=Scale(F7,from_=-127.0,to=127,length=200,orient=HORIZONTAL,command=getSete,sliderlength=15,tickinterval=1)
 Scontrast.grid(row=0,column=0,pady=5)
 Entry(F7,width=4,textvariable=e).grid(row=0,column=1)
 Scontrast.set(25)
 e.set(25)
 
 F8=LabelFrame(frame2,text="Gamma correction:",bd=1,relief=GROOVE,pady=5)
 F8.pack(fill=X)
 Sf=Scale(F8,from_=0.01,to=6.99,length=200,orient=HORIZONTAL,command=getSetf,sliderlength=15,tickinterval=0.01)
 Sf.grid(row=0,column=0,pady=10)
 Sf.set(1)
 Entry(F8,width=4,textvariable=f).grid(row=0,column=1)
 f.set("1")
 
 F9=LabelFrame(frame2,text="Saturation:",bd=1,relief=GROOVE,pady=5)
 F9.pack(fill=X)
 Sg=Scale(F9,length=200,from_=-255.0,to=255,orient=HORIZONTAL,command=getSetg,sliderlength=15,tickinterval=1)
 Sg.grid(row=0,column=0,pady=5)
 Sg.set(71)
 Entry(F9,width=4,textvariable=g).grid(row=0,column=1)
 
 F10=Frame(frame2,bd=2,relief=GROOVE)
 F10.pack(fill=X)
 Button(F10,text="Apply to original").grid(row=0,column=0,padx=10,pady=10)
 Button(F10,text="Set default values").grid(row=0,column=1)
 Checkbutton(F10,text="Save values on exit").grid(row=1,column=0)
 
 F11=Frame(frame2)
 F11.pack()
 Button(F11,text="OK",padx=50,command=Ok).grid(row=0,column=0,padx=5,pady=10)
 Button(F11,text="Cancel",padx=40,command=master.destroy).grid(row=0,column=1,padx=5,pady=10)
 master.mainloop()


def ReplaceColor(master,image1,canvas,event=NONE):
 def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

 def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

 def getColor1():
  root.color1 = colorchooser.askcolor()[1] 
  l1.config(bg=color1)
 
 def getColor2():
   root.color2=colorchooser.askcolor()[1]
   l2.config(bg=root.color2) 
 
 def click(event):
    im = Image.open("replace_color_image.jpg")
    rgbIm = im.convert("RGB")
    r,g,b = rgbIm.getpixel((event.x, event.y))
    color=rgb2hex(r,g,b)
    root.color1=color
    l1.config(bg=color)
 
 def replace():
  o=root.color1
  mr,og,ob=hex2rgb(o)
  rr=hex2rgb(root.color2)
  t=int(str(a.get()))
  photo=Image.open("replace_color_image.jpg").resize((200,300),Image.ANTIALIAS)
  photo=photo.convert('RGB')
  width=photo.size[0]
  height=photo.size[1]
  for x in range(0,width):
   for y in range(0,height):
    r,g,b=photo.getpixel((x,y))
    if(r in range(mr-t,mr+t) and g in range(og-t,og+t) and b in range(ob-t,ob+t)):
     photo.putpixel((x,y),rr)
  misc.imsave("replace_color_image.jpg",photo)
  root.img2=ImageTk.PhotoImage(photo)
  canvas1.delete("all")
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=root.img2)
 
 def ok():
  master.img2=ImageTk.PhotoImage(Image.open("replace_color_image.jpg"))
  canvas.delete("all")
  canvas.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=master.img2)
  root.destroy()

 def undo():
  img=Image.open(image1)
  root.img2=ImageTk.PhotoImage(img)
  canvas1.delete("all")
  canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=root.img2)
  misc.imsave("replace_color_image.jpg",img)
 
 def cancel():
  root.destroy()
 
 root=Toplevel(master)
 root.title("Replace Color")
 root.geometry("400x600+900+100")
 F1=Frame(root,bd=2,relief=GROOVE)
 F1.pack(fill=X)
 canvas1=Canvas(F1,bg="white",width=100,height=300,bd=2)
 canvas1.pack(fill=X)
 img=Image.open(image1).resize((200,300),Image.ANTIALIAS)
 root.img2=ImageTk.PhotoImage(img)
 canvas1.create_image(canvas_width/2,canvas_height/2,anchor="center",image=root.img2)
 canvas1.bind('<Button-1>',click)
 misc.imsave("replace_color_image.jpg",img)
  
 frame1=Frame(root,bd=2,relief=GROOVE)
 frame1.pack(fill=X)
 Label(frame1,text="Replace source color:").grid(row=0,column=0)
 l1=Label(frame1,bg="brown",padx=100)
 l1.grid(row=1,column=0,columnspan=2)
 Button(frame1,text="Choose",padx=40,command=getColor1).grid(row=1,column=2,padx=5,pady=5)
 Label(frame1,text="").grid(row=2,column=0)
 Label(frame1,text="with new color:").grid(row=4,column=0)
 l2=Label(frame1,bg="black",padx=100)
 l2.grid(row=5,column=0,columnspan=2)
 Button(frame1,text="Choose",padx=40,command=getColor2).grid(row=5,column=2)
 Label(frame1,text="").grid(row=6,column=0)
 
 frame2=Frame(root,bd=2,relief=GROOVE)
 frame2.pack(fill=X)
 Label(frame2,text="Tolerance value:").grid(row=0,column=0)
 a=StringVar()
 Entry(frame2,width=5,textvariable=a).grid(row=0,column=1)
 a.set(0)
 Label(frame2,text="(0-128)").grid(row=0,column=2)
 
 
 frame4=Frame(root)
 frame4.pack(fill=X)
 Button(frame4,text="Apply to current image",command=replace).grid(row=0,column=0,padx=20,pady=5)
 Button(frame4,text="Ok",padx=50,command=ok).grid(row=0,column=2,padx=20,pady=5)
 Button(frame4,text="Undo",padx=46,command=undo).grid(row=1,column=0,padx=20,pady=5)
 Button(frame4,text="Cancel",padx=40,command=cancel).grid(row=1,column=2,padx=20,pady=5)
 root.mainloop()


def CreateFrame(master,oldImage,canvas,event=NONE):
 def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)
 def getColor1(l):
  master.color1 = colorchooser.askcolor()[1] 
  l.config(bg=master.color1)
 def getColor2(l):
  master.color2 = colorchooser.askcolor()[1] 
  l.config(bg=master.color2)
 def getColor3(l):
  master.color3 = colorchooser.askcolor()[1] 
  l.config(bg=master.color3)
 def getColor4(l):
  master.color4 = colorchooser.askcolor()[1] 
  l.config(bg=master.color4)

 def selectItem(event=NONE):
  L=M1.focus()
  index=(M1.index(L))
  changeValues(index)

 def changeValues(index):
  if(index==0):
   a.set(0)
   b.set(0)
   c.set(0)
   d.set(40)
   master.color1="white"
   master.color2="white"
   master.color3="white"
   master.color4="white"
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==1):
   a.set(5)
   b.set(5)
   c.set(5)
   d.set(5)
   color1=rgb2hex(32,32,32)
   color2=rgb2hex(45,45,45)
   color3=rgb2hex(60,60,60)
   color4=rgb2hex(80,80,80)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==2):
   a.set(2)
   b.set(3)
   c.set(3)
   d.set(2)
   color1=rgb2hex(127,0,0)
   color2=rgb2hex(160,0,0)
   color3=rgb2hex(200,0,0)
   color4=rgb2hex(255,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==3):
   a.set(2)
   b.set(3)
   c.set(3)
   d.set(2)
   color1=rgb2hex(0,127,0)
   color2=rgb2hex(0,160,0)
   color3=rgb2hex(0,200,0)
   color4=rgb2hex(0,255,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==4):
   a.set(2)
   b.set(3)
   c.set(3)
   d.set(2)
   color1=rgb2hex(0,0,127)
   color2=rgb2hex(0,0,160)
   color3=rgb2hex(0,0,200)
   color4=rgb2hex(0,0,255)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==5):
   a.set(1)
   b.set(10)
   c.set(1)
   d.set(5)
   color1=rgb2hex(32,32,32)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(255,255,255)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==6):
   a.set(1)
   b.set(10)
   c.set(1)
   d.set(5)
   color1=rgb2hex(32,32,32)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(127,127,127)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==7):
   a.set(1)
   b.set(15)
   c.set(0)
   d.set(5)
   color1=rgb2hex(112,112,112)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(255,255,255)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==8):
   a.set(15)
   b.set(0)
   c.set(0)
   d.set(0)
   color1=rgb2hex(0,0,0)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(0,0,0)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==9):
   a.set(0)
   b.set(0)
   c.set(16)
   d.set(3)
   color1=rgb2hex(255,255,255)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(255,255,255)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==10):
   a.set(15)
   b.set(0)
   c.set(0)
   d.set(0)
   color1=rgb2hex(255,255,255)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(0,0,0)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==11):
   a.set(2)
   b.set(2)
   c.set(2)
   d.set(2)
   color1=rgb2hex(96,96,96)
   color2=rgb2hex(80,80,80)
   color3=rgb2hex(64,64,64)
   color4=rgb2hex(48,48,48)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==12):
   a.set(5)
   b.set(1)
   c.set(20)
   d.set(0)
   color1=rgb2hex(112,112,112)
   color2=rgb2hex(174,174,174)
   color3=rgb2hex(112,112,112)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==13):
   a.set(1)
   b.set(0)
   c.set(20)
   d.set(1)
   color1=rgb2hex(0,0,0)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(112,112,112)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==14):
   a.set(0)
   b.set(0)
   c.set(20)
   d.set(0)
   color1=rgb2hex(0,0,0)
   color2=rgb2hex(0,0,0)
   color3=rgb2hex(112,112,112)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==15):
   a.set(3)
   b.set(10)
   c.set(1)
   d.set(0)
   color1=rgb2hex(149,129,110)
   color2=rgb2hex(196,181,154)
   color3=rgb2hex(0,0,0)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
  if(index==16):
   a.set(3)
   b.set(10)
   c.set(1)
   d.set(0)
   color1=rgb2hex(98,119,174)
   color2=rgb2hex(140,169,248)
   color3=rgb2hex(0,0,0)
   color4=rgb2hex(0,0,0)
   master.color1=color1
   master.color2=color2
   master.color3=color3
   master.color4=color4
   l1.config(bg=master.color1)
   l2.config(bg=master.color2)
   l3.config(bg=master.color3)
   l4.config(bg=master.color4)
 
 def okAndSave():
  ok()
  img=Image.open("frame.jpg")
  width,height=img.size
  new_width,new_height=1300,600
  while width>1300:
   factor=width/height
   width=int(factor*new_height)
   height=new_height
  
  if height>600:
   height=600
  
  img2=img.resize((width,height),Image.ANTIALIAS)
  master.img2=ImageTk.PhotoImage(img2)
  canvas.delete("all")
  canvas.create_image(canvas_width/2,(canvas_height/2)+10,anchor="center",image=master.img2)
  misc.imsave("1.jpg",img)
  root.destroy()
 
 def cancel():
  master.img2=ImageTk.PhotoImage(Image.open(oldImage).resize((250,350),Image.ANTIALIAS))
  canvas.create_image(canvas_width/2,canvas_height/2+10,anchor="center",image=master.img2)
  root.destroy()
 
 def ok():
  img=Image.open(oldImage)
  img2=ImageOps.expand(img,border=a.get(),fill=master.color1)
  img3=ImageOps.expand(img2,border=b.get(),fill=master.color2)
  img4=ImageOps.expand(img3,border=c.get(),fill=master.color3)
  img5=ImageOps.expand(img4,border=d.get(),fill=master.color4)
  misc.imsave("frame.jpg",img5)
  h,w=img5.size
  img6=img5.resize((100,190),Image.ANTIALIAS)
  root.img5=ImageTk.PhotoImage(img6)
  c1.create_image((250-width)/2,10,anchor="nw",image=root.img5)
  
 
 a=IntVar()
 b=IntVar()
 c=IntVar()
 d=IntVar()
 master.color1="black"
 master.color2="black"
 master.color3="black"
 master.color4="black"
 root=Toplevel(master)
 root.title("Create picture frame")
 frame1=LabelFrame(root,text="Frame style (default names):",bd=2,relief=GROOVE)
 frame1.pack(side=TOP)
 M1=ttk.Treeview(frame1,height=10,columns=1)
 M1.grid(row=0,column=0)
 M1.column("1",width=0)
 M1.insert('',0,text="Inside fading frame")
 M1.insert('',1,text="Grey gradient")
 M1.insert('',2,text="Red gradient")
 M1.insert('',3,text="Green gradient")
 M1.insert('',4,text="Blue gradient")
 M1.insert('',5,text="Black with a white line and dark gray border")
 M1.insert('',6,text="Black with a gray line and dark gray border")
 M1.insert('',7,text="Black with gray border")
 M1.insert('',8,text="Plain black")
 M1.insert('',9,text="White with black inner edge")
 M1.insert('',10,text="Plain white")
 M1.insert('',11,text="Dark gradient")
 M1.insert('',12,text="Mono gray with inlay")
 M1.insert('',13,text="Gray with black inner and outer border")
 M1.insert('',14,text="Plain gray")
 M1.insert('',15,text="Warm")
 M1.insert('',16,text="Cold")
 M1.bind('<ButtonRelease-1>',selectItem)
 scroll=Scrollbar(frame1,orient=VERTICAL,command=M1.yview)
 scroll.grid(row=0,column=1,sticky='nsew')
 c1=Canvas(frame1,width=250,height=200,bg="white")
 c1.grid(row=0,column=2)
 img=Image.open(oldImage).resize((100,190),Image.ANTIALIAS)
 width,height=img.size
 root.img2=ImageTk.PhotoImage(img)
 c1.create_image((250-width)/2,10,anchor="nw",image=root.img2)
 
 frame2=Frame(root)
 frame2.pack(fill=X)
 T1=Frame(frame2)
 T1.grid(row=0,column=0)
 
 F1=LabelFrame(T1,text="Frame size:",bd=2,relief=GROOVE)
 F1.pack(side=TOP,fill=X)
 Label(F1,text="Border-1 (outer) size:",pady=5).grid(row=0,column=0,padx=5,pady=5)
 Entry(F1,width=6,textvariable=a).grid(row=0,column=1)
 a.set(0)
 Label(F1,text="pixels").grid(row=0,column=2)
 Label(F1,text="Border-2 size:            ",pady=5).grid(row=1,column=0,padx=5)
 Entry(F1,width=6,textvariable=b).grid(row=1,column=1)
 b.set(0)
 Label(F1,text="pixels").grid(row=1,column=2)
 Label(F1,text="Border-3 size:            ",pady=5).grid(row=2,column=0,padx=5)
 Entry(F1,width=6,textvariable=c).grid(row=2,column=1)
 c.set(0)
 Label(F1,text="pixels").grid(row=2,column=2)
 Label(F1,text="Border-4 (inner) size:",pady=7).grid(row=3,column=0,padx=5,pady=5)
 Entry(F1,width=6,textvariable=d).grid(row=3,column=1)
 d.set(0)
 Label(F1,text="pixels").grid(row=3,column=2)
 
 F2=Frame(T1,bd=2,relief=GROOVE)
 F2.pack(fill=X)
 Checkbutton(F2,text="Auto-load default sizes on style change",pady=20).pack()
 
 T2=Frame(frame2)
 T2.grid(row=0,column=1)
 F3=LabelFrame(T2,text="Frame colors:",bd=2,relief=GROOVE)
 F3.pack(fill=X)
 Label(F3,text="Border-1 (outer) color:").grid(row=0,column=0)
 l1=Label(F3,bd=3,relief=SUNKEN,padx=30)
 l1.grid(row=0,column=1)
 Button(F3,text="Choose",padx=10,command=lambda :getColor1(l1)).grid(row=0,column=2,padx=10,pady=5)
 Label(F3,text="Border-2 color:            ").grid(row=1,column=0)
 l2=Label(F3,bd=3,relief=SUNKEN,padx=30)
 l2.grid(row=1,column=1)
 Button(F3,text="Choose",padx=10,command=lambda :getColor2(l2)).grid(row=1,column=2,padx=10,pady=5)
 Label(F3,text="Border-3 color:            ").grid(row=2,column=0)
 l3=Label(F3,bd=3,relief=SUNKEN,padx=30)
 l3.grid(row=2,column=1)
 Button(F3,text="Choose",padx=10,command=lambda :getColor3(l3)).grid(row=2,column=2,padx=10,pady=5)
 Label(F3,text="Border-4 (inner) color:").grid(row=3,column=0)
 l4=Label(F3,bd=3,relief=SUNKEN,padx=30)
 l4.grid(row=3,column=1)
 Button(F3,text="Choose",padx=10,command=lambda :getColor4(l4)).grid(row=3,column=2,padx=10,pady=5)
 
 F4=Frame(T2,bd=2,relief=GROOVE)
 F4.pack(fill=X)
 Checkbutton(F4,text="Auto-load default colors on style change              ").grid(row=0,column=0)
 Label(F4,text="Hint: click into image (main window) to set a special").grid(row=1,column=0)
 Label(F4,text="color for the focused 'Choose' button.                       ").grid(row=2,column=0)
 
 frame3=Frame(root)
 frame3.pack()
 Button(frame3,text="Apply to current image",padx=50,command=ok).grid(row=0,column=0,padx=5,pady=5)
 Button(frame3,text="Ok",padx=50,command=okAndSave).grid(row=0,column=1,padx=5,pady=5)
 Button(frame3,text="Cancel",padx=46,command=cancel).grid(row=0,column=2,padx=5,pady=5)
 root.mainloop()


def ResizeImage(master,image,canvas,event=NONE):
 root=Toplevel(master)
 root.title("Resize/Resample image")
 a=StringVar()
 b=StringVar()
 c=StringVar()
 d=StringVar()
 e=StringVar()

 def one(height,width):
   a.set(height)
   b.set(width)
   l2.config(text=str(height)+"x"+str(width))   

 def two():
  hPer=int(c.get())
  wPer=int(d.get())
  h=int(a.get())
  w=int(b.get())
  height=h+(h/hPer)
  width=w+(w/wPer)
  a.set(int(height))
  b.set(int(width))
  l2.config(text=str(height)+"x"+str(width))   

 def resize1():
   width=int(a.get())
   height=int(b.get())
   img2=img.resize((width,height),Image.ANTIALIAS)
   root.img2=ImageTk.PhotoImage(img2)
   l2.config(text=str(img2.size[0])+"x"+str(img2.size[1]))
   canvas.delete('all')
   canvas.create_image(10,10,anchor='nw',image=root.img2)
 
 
 frame1=Frame(root)
 frame1.pack(side=LEFT)
 
 T1=Frame(frame1,bd=2,relief=GROOVE)
 T1.pack(fill=X)
 Label(T1,text="Current size:",pady=10).grid(row=0,column=0)
 l1=Label(T1,text="",padx=10)
 img=Image.open(image)
 old_height=img.size[0]
 old_width=img.size[1]
 l1.config(text=str(old_width)+"x"+str(old_height))
 l1.grid(row=0,column=1)
 Label(T1,text="Pixels").grid(row=0,column=2)
 Label(T1,text="New size:     ",pady=5).grid(row=1,column=0)
 l2=Label(T1,text="",padx=10)
 l2.config(text=str(old_width)+"x"+str(old_height))
 l2.grid(row=1,column=1)
 Label(T1,text="Pixels").grid(row=1,column=2)
 
 T2=LabelFrame(frame1,text="Set new size:",bd=2,relief=GROOVE)
 T2.pack(fill=X)
 Label(T2,text="Width:",pady=10).grid(row=0,column=0)
 Entry(T2,width=10,textvariable=a).grid(row=0,column=1)
 a.set(0)
 Label(T2,text="    Height:",pady=10).grid(row=0,column=2)
 Entry(T2,width=10,textvariable=b).grid(row=0,column=3)
 b.set(0)
 Label(T2,text="",pady=10).grid(row=1,column=0)
 #Radiobutton(T2,text="Pixels",value=1,variable="e").grid(row=1,column=1)
 #Radiobutton(T2,text="cm     ",value=2,variable="e").grid(row=1,column=2)
 #Radiobutton(T2,text="inches",value=3,variable="e").grid(row=1,column=3)

 T3=LabelFrame(frame1,text="Set new size as percentage of original:",bd=2,relief=GROOVE)
 T3.pack(fill=X)
 Label(T3,text="Width:",pady=15).grid(row=0,column=0)
 Entry(T3,width=10,textvariable=c).grid(row=0,column=1)
 c.set(0)
 Label(T3,text="%",padx=15).grid(row=0,column=2)
 Label(T3,text="Width:",pady=15).grid(row=0,column=3)
 Entry(T3,width=10,textvariable=d).grid(row=0,column=3)
 d.set(0)
 Label(T3,text="%",padx=15).grid(row=0,column=4)
 Button(T3,text="change dimensions",command=two).grid(row=1,column=2)
 
 T4=Frame(frame1,bd=2,relief=GROOVE)
 T4.pack(fill=X)
 Checkbutton(T4,text="Preserve aspect ratio (proportional)          ",pady=5).pack(anchor=W)
 Checkbutton(T4,text="Apply sharpen after Resample                  ",pady=5).pack(anchor=W)
 Checkbutton(T4,text="Adjust DPI based on new sizes (asp. ratio)",pady=5).pack(anchor=W)
 
 T4a=Frame(T4)
 T4a.pack(anchor=W,pady=3)
 Label(T4a,text="DPI:",padx=5,pady=15).grid(row=0,column=0)
 Entry(T4a,width=10).grid(row=0,column=1)
 Label(T4a,text="(auto calc. for cm/inches)").grid(row=0,column=2)
 
 TOK=Frame(frame1)
 TOK.pack()
 Button(TOK,text="Ok",padx=50,underline=0,command=resize1).grid(row=0,column=1,padx=5,pady=5)
 
 frame2=Frame(root)
 frame2.pack(side=RIGHT)
 T5=LabelFrame(frame2,text="Some standard dimensions (pixels):",bd=2,relief=GROOVE)
 T5.pack(fill=X)
 option=OptionMenu(T5,"New size","1280x720","1280x800","1280x960","1440x900","1600x1200","1680x1050","1920x1080","2560x1080","2560x1440","2560x1600",".......")
 option.grid(row=0,column=0)
 Label(T5,text="(ratio option used)").grid(row=0,column=1)
 Radiobutton(T5,text="640x480               ",underline=0,value=1,variable="m",command=lambda :one(640,480)).grid(row=1,column=0)
 Radiobutton(T5,text="800x600                ",underline=0,value=2,variable="m",command=lambda :one(800,600)).grid(row=2,column=0)
 Radiobutton(T5,text="1024x768              ",underline=0,value=3,variable="m",command=lambda :one(1024,768)).grid(row=3,column=0)
 Radiobutton(T5,text="Best fit to desktop",underline=5,value=4,variable="m").grid(row=4,column=0)
 Radiobutton(T5,text="1280x720 (HD)    ",underline=1,value=5,variable="m",command=lambda :one(1280,720)).grid(row=1,column=1)
 Radiobutton(T5,text="1920x1080 (FHD)",underline=1,value=6,variable="m",command=lambda :one(1920,1080)).grid(row=2,column=1)
 Radiobutton(T5,text="3840x2160 (4k)   ",underline=2,value=7,variable="m",command=lambda :one(3480,2160)).grid(row=3,column=1)
 Radiobutton(T5,text="7680x4320 (8k)   ",underline=0,value=8,variable="m",command=lambda :one(7680,4320)).grid(row=4,column=1)
 Radiobutton(T5,text="Desktop size (noo aspect ratio)               ",underline=4,value=9,variable="m").grid(row=5,column=0,columnspan=2)
 Button(T5,text="Half",underline=0,padx=40).grid(row=6,column=0,padx=5,pady=5)
 Button(T5,text="Double",underline=0,padx=35).grid(row=6,column=1,padx=5,pady=5)
 Button(T5,text="Swap sides",underline=1,padx=20).grid(row=7,column=0,padx=5,pady=5)
 Button(T5,text="Add to standard box",underline=17).grid(row=7,column=1,padx=5,pady=5)
 
 T6=LabelFrame(frame2,text="Size method",bd=2,relief=GROOVE)
 T6.pack(fill=X)
 Radiobutton(T6,text="Resample (better quality), use Filter:",underline=0,value=1,variable="s").pack(anchor=W)
 option1=OptionMenu(T6,"Hemite (faster)","Triangle","Bell","Mitcell","B-spline","Lanzos (slowest)")
 option1.pack()
 Radiobutton(T6,text="Resize (faster, lower quality)",underline=1,value=2,variable="s").pack(anchor=W)
 
 T7=Frame(frame2,bd=2,relief=GROOVE)
 T7.pack(fill=X)
 Checkbutton(T7,text="Use fast Resample filter for image shirinking").pack(anchor=W)
 Checkbutton(T7,text="Try to improve gamma for Resample").pack(anchor=W)
 
 TCan=Frame(frame2)
 TCan.pack()
 Button(TCan,text="Cancel",underline=0,padx=40).pack(padx=5,pady=5)
 root.mainloop()


def sharpen(i,canvas,root,event=NONE):
  img=Image.open(i)
  img_sharp=img.filter(ImageFilter.SHARPEN)
  root.img2=ImageTk.PhotoImage(img_sharp)
  canvas.create_image(20,20,anchor='nw',image=root.img2)

def ChangeCanvasColor(canvas):
 color=colorchooser.askcolor()[1]
 canvas.config(bg=color)
