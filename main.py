import cv2
import numpy as np

drawing = False
prev_point = (0,0)
color = (0,255,0)
mode = "pen"

def draw (event,x,y,flags, param):

    global drawing,color,mode
    global prev_point

    if event == cv2.EVENT_LBUTTONDOWN and (y>45 and y<467) and mode=="pen":

        drawing = True
        print("left button down")

        cv2.circle(img,(x,y),1,color,-1)

        prev_point = (x,y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing == True and (y>45 and y<467) and mode=="pen":

        #cv2.circle(img,(x,y),1,(0,255,0),-1)

        cv2.line(img,prev_point,(x,y),color,1)

        prev_point = (x,y)

        print("mouse move")

    elif event == cv2.EVENT_LBUTTONUP:

        print("mouse up")
        drawing = False

    elif event == cv2.EVENT_LBUTTONDBLCLK:

        if (y>=5 and y<=35):

            if(x>=22 and x<=98):
                color = (255,255,255)
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(22,5),(98,35),(255,255,255),1)
            if(x>=120 and x<=196):
                color = (255,0,0)
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(255,255,255),1)
            if(x>=218 and x<=294):
                color = (0,255,0)
                cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
                cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(0,0,0),1)
                cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
                cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)
                cv2.rectangle(img,(218,5),(294,35),(255,255,255),1)
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
                mode = "erase"


img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

img[0:45,:] = [60,60,60]

cv2.rectangle(img,(22,5),(98,35),(0,0,0),1)
cv2.rectangle(img,(120,5),(196,35),(0,0,0),1)
cv2.rectangle(img,(218,5),(294,35),(255,255,255),1)
cv2.rectangle(img,(316,5),(392,35),(0,0,0),1)
cv2.rectangle(img,(414,5),(490,35),(0,0,0),1)

img[10:30,27:93] = [255,255,255]
img[10:30,125:191] = [255,0,0]
img[10:30,223:289] = [0,255,0]
img[10:30,321:387] = [0,0,255]
img[10:30,419:485] = [0,255,255]

img[467:,:] = [60,60,60]

cv2.circle(img,(25,492),15,(0,0,0),-1)
cv2.rectangle(img,(472,477),(502,507),(0,0,0),1)
cv2.putText(img,'X',(477,503),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)

while(True):

    cv2.imshow('image',img)

    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()