import cv2
import numpy as np
from datetime import datetime as dt

now = dt.now()  
#dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
#print("date and time =", dt_string)
drawing = False
colorfill = False
prev_point = (0,0)
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
yellow = (0,255,255)
pink = (255,0,255)
black = (0,0,0)
white = (255,255,255)
skyblue = (255,255,0)
color = green
mode = "pen"
font = cv2.FONT_HERSHEY_COMPLEX

def draw (event,x,y,flags, param):

    global drawing,color,mode,colorfill
    global prev_point

    if event == cv2.EVENT_LBUTTONDOWN and (y>45 and y<467) and mode=="pen":

        drawing = True
        print("left button down")

        cv2.circle(img,(x,y),1,color,-1)

        prev_point = (x,y)
    
    elif event == cv2.EVENT_LBUTTONDOWN and (y>45 and y<467) and mode=="color fill":

        colorfill = True
        print("left button down")

        cv2.circle(img,(x,y),10,color,-1)

        prev_point = (x,y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing == True and (y>45 and y<467) and mode=="pen":

        #cv2.circle(img,(x,y),1,(0,255,0),-1)

        cv2.line(img,prev_point,(x,y),color,1)

        prev_point = (x,y)

        print("mouse move")

    elif event == cv2.EVENT_MOUSEMOVE and colorfill == True and (y>45 and y<467) and mode=="color fill":

        #cv2.circle(img,(x,y),5,(0,0,0),-1)

        cv2.line(img,prev_point,(x,y),color,10)

        prev_point = (x,y)

        print("mouse move")

    elif event == cv2.EVENT_LBUTTONUP:

        print("mouse up")
        drawing = False
        colorfill = False

    elif event == cv2.EVENT_LBUTTONDBLCLK:

        if (y>=5 and y<=35):

            if(x>=22 and x<=98):
                mode = "pen"
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(22,5),(98,35),(255,255,255),1)
            if(x>=120 and x<=196):
                mode = "color fill"
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(255,255,255),1)
            if(x>=218 and x<=294):
                mode = "save"
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(255,255,255),1)
                cv2.waitKey(500)
                dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
                dt_string = dt_string + ".png"
                cv2.imwrite(dt_string,img)
                dt_string = "saved as "+dt_string
                cv2.imshow(dt_string,img)
                
            if(x>=316 and x<=392):
                color = (0,0,255)
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(255,255,255),1)
            if(x>=414 and x<=490):
                color = (0,255,255)
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(255,255,255),1)

        if y>=467 and y<=512:

            if x>=472 and x<=502 and y>=477 and y<=507:
                img[45:467,:] = (0,0,0)

            if x>=10 and x<=40 and y>=477 and y<=507:
                color = black
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(25,492),15,blue,-1)
                cv2.circle(img,(25,492),12,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=45 and x<=75 and y>=477 and y<=507:
                color = white
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(60,492),15,blue,-1)
                cv2.circle(img,(60,492),12,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=80 and x<=110 and y>=477 and y<=507:
                color = red
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(95,492),15,blue,-1)
                cv2.circle(img,(95,492),12,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=115 and x<=145 and y>=477 and y<=507:
                color = green
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(130,492),15,blue,-1)
                cv2.circle(img,(130,492),12,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=150 and x<=180 and y>=477 and y<=507:
                color = yellow
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(165,492),15,blue,-1)
                cv2.circle(img,(165,492),12,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=185 and x<=215 and y>=477 and y<=507:
                color = skyblue
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(200,492),15,blue,-1)
                cv2.circle(img,(200,492),12,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)

            if x>=220 and x<=250 and y>=477 and y<=507:
                color = pink
                cv2.circle(img,(25,492),15,black,-1)
                cv2.circle(img,(60,492),15,white,-1)
                cv2.circle(img,(95,492),15,red,-1)
                cv2.circle(img,(130,492),15,green,-1)
                cv2.circle(img,(165,492),15,yellow,-1)
                cv2.circle(img,(200,492),15,skyblue,-1)
                cv2.circle(img,(235,492),15,pink,-1)
                cv2.circle(img,(235,492),15,blue,-1)
                cv2.circle(img,(235,492),12,pink,-1)

img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

img[0:45,:] = [60,60,60]

cv2.rectangle(img,(22,5),(98,35),white,1)
cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
cv2.rectangle(img,(218,5),(294,35),black,1)
cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)

cv2.putText(img,'pen',(45,25),font,0.5,white,1,cv2.LINE_AA)
cv2.putText(img,'color fill',(130,25),font,0.4,white,1,cv2.LINE_AA)
cv2.putText(img,'save',(240,25),font,0.45,white,1,cv2.LINE_AA)

img[467:,:] = [60,60,60]

cv2.circle(img,(25,492),15,black,-1)
cv2.circle(img,(60,492),15,white,-1)
cv2.circle(img,(95,492),15,red,-1)
cv2.circle(img,(130,492),15,green,-1)
cv2.circle(img,(130,492),15,blue,-1)
cv2.circle(img,(130,492),12,green,-1)
cv2.circle(img,(165,492),15,yellow,-1)
cv2.circle(img,(200,492),15,skyblue,-1)
cv2.circle(img,(235,492),15,pink,-1)
cv2.rectangle(img,(472,477),(502,507),(0,0,0),1)
cv2.putText(img,'X',(477,503),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)

while(True):

    cv2.imshow('image',img)

    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()