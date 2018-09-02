from tkinter import *
from PIL import Image,ImageTk,ImageOps
from tkinter import filedialog
from scipy import misc
from skimage import feature
from skimage.io import imread
import numpy
import matplotlib.pyplot as plt
import matplotlib.widgets
import os
import imageModules
from imageModules import *
from scipy.ndimage import zoom
import time
import os.path
import threading

def zooming(image,event=NONE):
 def clipped_zoom(img, zoom_factor, **kwargs):
    h, w = img.shape[:2]
    zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)
    if zoom_factor < 1:
        zh = int(numpy.round(h * zoom_factor))
        zw = int(numpy.round(w * zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2
        out = numpy.zeros_like(img)
        out[top:top+zh, left:left+zw] = zoom(img, zoom_tuple, **kwargs)
    elif zoom_factor > 1:
        zh = int(numpy.round(h / zoom_factor))
        zw = int(numpy.round(w / zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2
        out = zoom(img[top:top+zh, left:left+zw], zoom_tuple, **kwargs)
        trim_top = ((out.shape[0] - h) // 2)
        trim_left = ((out.shape[1] - w) // 2)
        out = out[trim_top:trim_top+h, trim_left:trim_left+w]
    else:
        out = img
    return out
 img1=misc.imread("1.jpg")
 zm1=clipped_zoom(img1,2)
 misc.imsave("zoomed.jpg",zm1)
 img2=Image.open("zoomed.jpg")
 root.img2=ImageTk.PhotoImage(img2)
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)



def crop(image,event=NONE):
 def onselect(eclick,erelease):
   if eclick.ydata>erelease.ydata:
    eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
   if eclick.xdata>erelease.xdata:
    eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
   ax.set_ylim(erelease.ydata,eclick.ydata)
   ax.set_xlim(eclick.xdata,erelease.xdata)
   fig.canvas.draw()
 fig=plt.figure()
 ax=fig.add_subplot(111)
 photo=Image.open(image)
 photo.save("fhaltu.png")
 filename="fhaltu.png"
 im=Image.open(filename)
 arr=numpy.asarray(im)
 plt_image=plt.imshow(arr)
 plt_image.axes.get_xaxis().set_visible(False)
 plt_image.axes.get_yaxis().set_visible(False)
 rs=matplotlib.widgets.RectangleSelector(ax,onselect,drawtype='box',rectprops=dict(facecolor='red',edgecolor='black',alpha=0.5,fill=True))
 plt.show()
 plt.savefig("crop.jpg")

def ConvertToGreyscale(event=NONE):
 matA=misc.imread('1.jpg')
 h,w,b=matA.shape
 matB=numpy.zeros((h,w))
 r=0
 while r<h:
  c=0
  while c<w:
   factor=r/h
   progressBar.step(factor*100)
   matB[r][c]=matA[r][c][0]*0.21+matA[r][c][1]*0.72+matA[r][c][2]*0.07
   c=c+1
  r=r+1
 misc.imsave("1.jpg",matB)
 root.img=ImageTk.PhotoImage(Image.open("1.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def RGB2RBG(event=NONE):
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([r,b,g])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)

def RGB2BGR(event=NONE):
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([b,g,r])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)

def RGB2BRG(event=NONE):
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([b,r,g])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)

def RGB2GRB(event=NONE):
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([g,r,b])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)

def RGB2GBR(event=NONE):
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([g,b,r])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)



def edgeDetection():
 def edge(event):
  matA=misc.imread('1.jpg')
  h,w,b=matA.shape
  matB=numpy.zeros((h,w))
  r=0
  while r<h:
   c=0
   while c<w:
    matB[r][c]=matA[r][c][0]+matA[r][c][1]+matA[r][c][2]
    c=c+1
   r=r+1
  edges=feature.canny(matB,sigma=scale.get())
  misc.imsave("bb.jpg",edges)
  img=Image.open("bb.jpg")
  root.img2=ImageTk.PhotoImage(img)
  canvas.delete("all")
  canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 
 top=Toplevel(root)
 scale=Scale(top,from_=0,to=10,command=edge)
 scale.set(0)
 scale.pack()
 top.mainloop()

def sepia():
 def make_linear_ramp(white):
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((int(r*i/255), int(g*i/255), int(b*i/255)))
    return ramp 
 
 sepia=make_linear_ramp((255,240,192)) 
 im=Image.open("1.jpg")
 if im.mode!="L":
  im=im.convert("L")
 im.putpalette(sepia)
 im=im.convert("RGB")
 im.save("bb.jpg")
 img=Image.open("bb.jpg")
 root.img2=ImageTk.PhotoImage(img)
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave("1.jpg",img)

def autoAdjustColor():
 img=Image.open("1.jpg")
 img2=ImageOps.equalize(img)
 root.img2=ImageTk.PhotoImage(img2)
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave("1.jpg",img2)


def  redChannel():
 matA=misc.imread("1.jpg")
 h,w,b=matA.shape
 matB=numpy.zeros((h,w))
 r=0
 while r<h:
  c=0
  while c<w:
   matB[r][c]=matA[r][c][0]*0.21
   c+=1
  r+=1
 misc.imsave("1.jpg",matB)
 root.img=ImageTk.PhotoImage(Image.open("1.jpg"))
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def greenChannel():
 matA=misc.imread("1.jpg")
 h,w,b=matA.shape
 matB=numpy.zeros((h,w))
 r=0
 while r<h:
  c=0
  while c<w:
   matB[r][c]=matA[r][c][1]*0.72
   c+=1
  r+=1
 misc.imsave("1.jpg",matB)
 root.img=ImageTk.PhotoImage(Image.open("1.jpg"))
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def blueChannel():
 matA=misc.imread("1.jpg")
 h,w,b=matA.shape
 matB=numpy.zeros((h,w))
 r=0
 while r<h:
  c=0
  while c<w:
   matB[r][c]=matA[r][c][2]*0.07
   c+=1
  r+=1
 misc.imsave("1.jpg",matB)
 root.img=ImageTk.PhotoImage(Image.open("1.jpg"))
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def negative():
 img=Image.open("1.jpg")
 img=img.convert("RGB")
 data=numpy.array(img)
 r,g,b=data.T
 data=numpy.array([255-r,255-g,255-b])
 data=data.transpose()
 sub=Image.fromarray(data)
 misc.imsave("swap.jpg",sub)
 root.img2=ImageTk.PhotoImage(Image.open("swap.jpg"))
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 
def negativeRed():
 im=misc.imread("1.jpg")
 height=len(im)
 width=len(im[0])
 for row in range(height):
  for col in range(width):
   green=im[row][col][1]
   blue=im[row][col][2]
   red=255-im[row][col][0]
   im[row][col]=[red,green,blue]
 misc.imsave("1.jpg",im)
 img=Image.open("1.jpg")
 root.img=ImageTk.PhotoImage(img)
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def negativeBlue():
 im=misc.imread("1.jpg")
 height=len(im)
 width=len(im[0])
 for row in range(height):
  for col in range(width):
   red=im[row][col][0]
   green=im[row][col][1]
   blue=255-im[row][col][2]
   im[row][col]=[red,green,blue]
 misc.imsave("1.jpg",im)
 img=Image.open("1.jpg")
 root.img=ImageTk.PhotoImage(img)
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)

def negativeGreen():
 im=misc.imread("1.jpg")
 height=len(im)
 width=len(im[0])
 for row in range(height):
  for col in range(width):
   red=im[row][col][0]
   green=255-im[row][col][1]
   blue=im[row][col][2]
   im[row][col]=[red,green,blue]
 misc.imsave("1.jpg",im)
 img=Image.open("1.jpg")
 root.img=ImageTk.PhotoImage(img)
 canvas.delete('all')
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)


def RotateLeft(event=NONE):
 canvas.delete("all")
 img=Image.open('1.jpg')
 img2=img.rotate(90,expand=True)
 root.img2=ImageTk.PhotoImage(img2)
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave('1.jpg',img2)

def RotateRight(event=NONE):
 canvas.delete("all")
 img=Image.open('1.jpg')
 img2=img.rotate(-90,expand=True)
 width,height=checkDimension(img2)
 img3=img2.resize((width,height),Image.ANTIALIAS)
 root.img2=ImageTk.PhotoImage(img3)
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave('1.jpg',img2)

def VerticalFlip(event=NONE):
 canvas.delete("all")
 img=Image.open('1.jpg')
 img2=img.transpose(Image.FLIP_TOP_BOTTOM)
 root.img2=ImageTk.PhotoImage(img2)
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave('1.jpg',img2)

def HorizontalFlip(event=NONE):
 canvas.delete("all")
 img=Image.open('1.jpg')
 img2=img.transpose(Image.FLIP_LEFT_RIGHT)
 root.img2=ImageTk.PhotoImage(img2)
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img2)
 misc.imsave('1.jpg',img2)

def doNothing():
 w=Label(root,text="Not yet implemented")
 w.pack()

def checkDimension(image):
  width,height=image.size
  new_width,new_height=1300,600
  while width>1300:
   factor=width/height
   width=int(factor*new_height)
   height=new_height
  
  if height>600:
   height=600
  return width,height


def Open(event=NONE):
 t=threading.Thread()
 t.__init__(target=progressBar.start,args=())
 t.start()
 a=filedialog.askopenfilename(initialdir="/Pictures/college",title="select file",filetypes=(("jpeg files","*.jpg"),("alll files","*.*")))
 filename=Image.open(a)
 width,height=checkDimension(filename)
 img=filename.resize((width,height),Image.ANTIALIAS)
 root.photo=ImageTk.PhotoImage(img)
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.photo)
 AccessTime=time.ctime(os.path.getatime(a))
 Size=os.path.getsize(a)
 Size=int(Size/(1024))
 b="Size :  "+str(height)+"x"+str(width)+"          Image Creation Date And Time : "+str(AccessTime)+"           File Size : "+str(Size)+"KB"
 groundLabel.config(text=b)
 misc.imsave('1.jpg',img)
 misc.imsave("original.jpg",img)
 progressBar.stop()
 t.join()

def reOpen(event=NONE):
 img=Image.open("original.jpg")
 root.img=ImageTk.PhotoImage(img)
 canvas.delete("all")
 canvas.create_image(root.canvas_width/2,(root.canvas_height/2)+10,anchor="center",image=root.img)
 misc.imsave("1.jpg",img)

root=Tk()
root.title("Photoshop")
root.canvas_height=640
root.canvas_width=1350
canvas=Canvas(root,width=root.canvas_width,height=root.canvas_height,bg="#E6DECC")
canvas.pack()
root.geometry('1366x670+0+0')
menubar=Menu(root)
fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label='Open...',command=Open,accelerator="Ctrl+o")
menubar.bind_all("<Control-o>",Open)
fileMenu.add_command(label='Reopen',command=reOpen)
fileMenu.add_command(label='Open Recent Files',command=doNothing)
fileMenu.add_command(label='Open with external editor',command=doNothing)
OpenAsMenu=Menu(root)
OpenAsMenu=Menu(fileMenu,tearoff=0)
OpenAsMenu.add_command(label="HEX File",command=doNothing)
OpenAsMenu.add_command(label="ASCII File",command=doNothing)
OpenAsMenu.add_command(label="RAW File",command=doNothing)
fileMenu.add_cascade(label="Open as",menu=OpenAsMenu)
fileMenu.add_separator()
fileMenu.add_command(label='Thumbnails',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Slideshow...',command=doNothing)
fileMenu.add_command(label='Start slidedshow with current file list',command=doNothing)
fileMenu.add_command(label='Batch Conversion/Rename..',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Search files..',command=doNothing)
fileMenu.add_command(label='Rename File...',command=doNothing)
fileMenu.add_command(label='Move File...',command=doNothing)
fileMenu.add_command(label='Copy File...',command=doNothing)
fileMenu.add_command(label='Delete File..',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Save(original folder)',command=doNothing)
fileMenu.add_command(label='Save as...',command=doNothing)
fileMenu.add_command(label='Save for Web...(Plugin)',command=doNothing)
fileMenu.add_command(label='Save Selection as...',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Print',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Select Scan/TWAIN Source...',command=doNothing)
fileMenu.add_command(label='Acquire/Batch scanning...',command=doNothing)
fileMenu.add_command(label='Copy Shop..',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label="File",menu=fileMenu)

editMenu=Menu(menubar,tearoff=0)
editMenu.add_command(label='Undo',command=doNothing)
editMenu.add_command(label='Redo',command=doNothing)
'''
editMenu.add_separator()
editMenu.add_command(label='Show Paint dialog',command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Create custom crop selection',command=doNothing)
option1=Menu(root)
option1=Menu(editMenu,tearoff=0)
option1.add_command(label='1:1',command=doNothing)
option1.add_command(label='3:2',command=doNothing)
option1.add_command(label='4:3',command=doNothing)
option1.add_command(label='16:9',command=doNothing)
option1.add_command(label='16:10',command=doNothing)
option1.add_command(label='21:9 (2.370:1)',command=doNothing)
option1.add_separator()
option1.add_command(label='2:3',command=doNothing)
option1.add_command(label='3:4',command=doNothing)
option1.add_command(label='9:16',command=doNothing)
option1.add_command(label='10:16',command=doNothing)
option1.add_separator()
option1.add_command(label='Current custom selection',command=doNothing)
editMenu.add_cascade(label="Create maximized selection (ratio:)",menu=option1)

editMenu.add_command(label='Maximize and center selection',command=doNothing)
option2=Menu(root)
option2=Menu(editMenu,tearoff=0)
option2.add_command(label='None',command=doNothing)
option2.add_command(label='Golden ratio',command=doNothing)
option2.add_command(label='Thirds',command=doNothing)
option2.add_command(label='Fourths',command=doNothing)
editMenu.add_cascade(label='Show selection grid',menu=option2)

editMenu.add_command(label='Show fixed grid',command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Insert text...',command=doNothing)
editMenu.add_command(label='Insert overlay/watermark image...',command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Cut-selection',command=doNothing)
editMenu.add_command(label='Cut-area outside of the selection',command=doNothing)
option3=Menu(root)
option3=Menu(editMenu,tearoff=0)
option3.add_command(label='Remove Horizontal strip (sel. height)',command=doNothing)
option3.add_command(label='Remove Vertical strip (sel. width)',command=doNothing)
option3.add_separator()
option3.add_command(label='Insert Horizontal strip (sel. height)',command=doNothing)
option3.add_command(label='Insert Vertical strip (sel. width)',command=doNothing)
editMenu.add_cascade(label='Remove/Insert strip (uses selection)',menu=option3)

editMenu.add_separator()
editMenu.add_command(label='Crop selection (Cut out)',command=doNothing)
editMenu.add_command(label='Auto-crop borders',command=doNothing)
editMenu.add_command(label='Capture visible window area',command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Copy',command=doNothing)
editMenu.add_command(label='Paste',command=doNothing)
option4=Menu(root)
option4=Menu(editMenu,tearoff=0)
option4.add_command(label='To right',command=doNothing)
option4.add_command(label='To left',command=doNothing)
option4.add_separator()
option4.add_command(label='To Bottom',command=doNothing)
option4.add_command(label='To Top',command=doNothing)
editMenu.add_cascade(label="Paste Special (add on side)",menu=option4)

editMenu.add_command(label='Delete (Clear dispay)',command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Clear Clipboard',command=doNothing)
editMenu.add_separator()
'''
menubar.add_cascade(label="Edit",menu=editMenu)

imageMenu=Menu(menubar,tearoff=0)
imageMenu.add_command(label='Information...',command=doNothing)
imageMenu.add_separator()
imageMenu.add_command(label='Change canvas color',command=lambda :ChangeCanvasColor(canvas))
imageMenu.add_command(label='Create New (empty) image...',command=lambda :CreateNewImage(canvas,root),accelerator="shift+N")
menubar.bind_all("<N>",lambda :CreateNewImage(canvas,root))
#imageMenu.add_command(label='Create Panorama image...',command=CreatePanoramaImage)
imageMenu.add_separator()
imageMenu.add_command(label='Rotate Left(counter clockwise)',command=RotateLeft,accelerator="l")
menubar.bind_all("<l>",RotateLeft)
imageMenu.add_command(label='Rotate Right(clockwise)',command=RotateRight,accelerator="r")
menubar.bind_all("<r>",RotateRight)
image="1.jpg"
imageMenu.add_command(label='Custom/Fine rotation...',command=lambda :RotateByAngle(root,image,canvas),accelerator="Ctrl+u")
menubar.bind_all("<Control-u>",lambda :RotateByAngle(root,image,canvas))
imageMenu.add_command(label='Vertical Flip',command=VerticalFlip,accelerator="v")
menubar.bind_all("<v>",VerticalFlip)
imageMenu.add_command(label='Horizontal Flip',command=HorizontalFlip,accelerator="h")
menubar.bind_all("<h>",HorizontalFlip)
imageMenu.add_separator()
imageMenu.add_command(label='Resize/Resample...',command=lambda :ResizeImage(root,image,canvas),accelerator="Ctrl+r")
menubar.bind_all("<Control-r>",lambda :ResizeImage(root,image,canvas))
#imageMenu.add_command(label='Change canvas size...',command=ChangeCanvasSize,accelerator="Shift+v")
#menubar.bind_all("<V>",ChangeCanvasSize)
imageMenu.add_command(label='Add border/frame...',command=lambda :CreateFrame(root,image,canvas),accelerator="Ctrl+d")
menubar.bind_all("<Control-d>",lambda :CreateFrame(root,image,canvas))
imageMenu.add_separator()
#imageMenu.add_command(label='Increase Color Depth...',command=doNothing)
#imageMenu.add_command(label='Decrease Color Depth...',command=DecreaseColorDepth)
#imageMenu.add_separator()
imageMenu.add_command(label='Convert to Greyscale',command=ConvertToGreyscale,accelerator="Ctrl+g")
menubar.bind_all("<Control-g>",ConvertToGreyscale)
imageMenu.add_command(label="crop",command=lambda :crop(image))
imageMenu.add_command(label="zoom",command=lambda :zooming(image))
ImageOption1=Menu(root)
ImageOption1=Menu(imageMenu,tearoff=0)
ImageOption1.add_command(label='Red',command=redChannel)
ImageOption1.add_command(label='Green',command=greenChannel)
ImageOption1.add_command(label='Blue',command=blueChannel)
ImageOption1.add_command(label='Alpha',command=doNothing)
imageMenu.add_cascade(label='Show channel',menu=ImageOption1)

ImageOption2=Menu(root)
ImageOption2=Menu(imageMenu,tearoff=0)
ImageOption2.add_command(label='All channel',command=negative)
ImageOption2.add_separator()
ImageOption2.add_command(label='Red channel',command=negativeRed)
ImageOption2.add_command(label='Green channel',command=negativeGreen)
ImageOption2.add_command(label='Blue channel',command=negativeBlue)
imageMenu.add_cascade(label='Negative (invert image)',menu=ImageOption2)

imageMenu.add_command(label='Color correction...',command=lambda :ColorCorrection(canvas,image,root),accelerator="Shift+G")
menubar.bind_all("<G>",lambda :ColorCorrection(canvas,image,root))
imageMenu.add_command(label='Histogram...',command=doNothing)
imageMenu.add_command(label='Replace Color...',command=lambda :ReplaceColor(root,image,canvas))
imageMenu.add_command(label='Create Titled image...',command=lambda :CreateTitleImage(image,canvas,root))
imageMenu.add_separator()
imageMenu.add_command(label='Auto-adjust colors',command=autoAdjustColor)
imageMenu.add_command(label='Sharpen',command=lambda :sharpen(image,canvas,root),accelerator="Shift+S")
menubar.bind("<S>",lambda :sharpen(image,canvas,root))
#imageMenu.add_command(label='Red eye reduction (selection)',command=doNothing)
ImageOption3=Menu(root)
ImageOption3=Menu(imageMenu,tearoff=0)
ImageOption3.add_command(label='Effects browser...',command=doNothing)
ImageOption3.add_separator()
ImageOption3.add_command(label='3D Button',command=doNothing)
ImageOption3.add_command(label='Blur',command=doNothing)
ImageOption3.add_command(label='Emboss',command=doNothing)
ImageOption3.add_command(label='Oil Paint',command=doNothing)
ImageOption3.add_command(label='Edge Detection',command=edgeDetection)
ImageOption3.add_command(label='Median Filter',command=doNothing)
ImageOption3.add_command(label='Explosion',command=doNothing)
ImageOption3.add_command(label='Pixelize',command=doNothing)
ImageOption3.add_command(label='Sepia',command=sepia)
ImageOption3.add_command(label='Rain Drops',command=doNothing)
ImageOption3.add_separator()
ImageOption3.add_command(label='AltaLux effects...(Plugin)',command=doNothing)
ImageOption3.add_separator()
ImageOption3.add_command(label='Filter Sandbox... (Plugin)',command=doNothing)
ImageOption3.add_separator()
ImageOption3.add_command(label='Filter Simulation effect...(Plugin)',command=doNothing)
ImageOption3.add_separator()
ImageOption3.add_command(label='Filter Factory... (Plugin)',command=doNothing)
ImageOption3.add_command(label='Filters Unlimited... (Plugin)',command=doNothing)
imageMenu.add_cascade(label='Effects',menu=ImageOption3)

ImageOption4=Menu(root)
ImageOption4=Menu(imageMenu,tearoff=0)
ImageOption4.add_command(label='Filter dialog...',command=doNothing)
ImageOption4.add_separator()
ImageOption4.add_command(label='Perspective Transformations',command=doNothing)
ImageOption4.add_command(label='SmartCurve',command=doNothing)
ImageOption4.add_command(label='Wire Worm',command=doNothing)
ImageOption4.add_command(label="Harry's Filters",command=doNothing)
ImageOption4.add_command(label='PapArt',command=doNothing)
#imageMenu.add_cascade(label='Adobe 8BF Plugins',menu=ImageOption4)

imageMenu.add_separator()
ImageOption5=Menu(root)
ImageOption5=Menu(imageMenu,tearoff=0)
ImageOption5.add_command(label='RGB->RBG',command=RGB2RBG)
ImageOption5.add_command(label='RGB->BGR',command=RGB2BGR)
ImageOption5.add_command(label='RGB->BRG',command=RGB2BRG)
ImageOption5.add_command(label='RGB->GRB',command=RGB2GRB)
ImageOption5.add_command(label='RGB->GBR',command=RGB2GBR)
imageMenu.add_cascade(label='Swap Colors',menu=ImageOption5)

ImageOption6=Menu(root)
ImageOption6=Menu(imageMenu,tearoff=0)
ImageOption6.add_command(label='Edit palette...',command=doNothing)
ImageOption6.add_command(label='Export palette...',command=doNothing)
ImageOption6.add_command(label='Import palette...',command=doNothing)
#imageMenu.add_cascade(label='Palette',menu=ImageOption6)

menubar.add_cascade(label="Image",menu=imageMenu)
optionMenu=Menu(menubar,tearoff=0)
optionMenu.add_command(label='Properties/Settings...',command=doNothing)
optionMenu.add_command(label='Change language...',command=doNothing)
menubar.add_cascade(label='Option',menu=optionMenu)

viewMenu=Menu(menubar,tearoff=0)
viewMenu.add_command(label='Show/hide status bar',command=doNothing)
viewMenu.add_command(label='Show/hide toolbar',command=doNothing)
viewMenu.add_command(label='Show/hide menu bar',command=doNothing)
viewMenu.add_command(label='Show/hide caption',command=doNothing)
menubar.add_cascade(label='View',menu=viewMenu)

helpMenu=Menu(menubar,tearoff=0)
helpMenu.add_command(label='Photoshop Help',command=doNothing)
menubar.add_cascade(label='Help',menu=helpMenu)
root.config(menu=menubar)

groundLabel=Label(root,width=100,height=20,text="",relief="groove",anchor='w')
groundLabel.config(text="No File loaded ( Use -> Open)")
groundLabel.pack(side=LEFT)
root.progress=StringVar()
progressBar=ttk.Progressbar(root,length=100,maximum=100,mode='determinate',orient=HORIZONTAL)
progressBar.pack()
root.mainloop()