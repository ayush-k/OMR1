import cv2#imports the open cv module 
import numpy as np #imports the numpy module 
#from matplotlib import pyplot as plt
def getting_x_coor(a,temp):# forms a list of the x coordinates of the a,b,c,d options by taking the input matrix from the match template function 
	index=0
	for x_co in temp:
		if(x_co[0]-a[index]>10):
			a.append(x_co[0])
			index=index+1	
def getting_xy(temp2,xy):
	index=0
	for i in temp2:
		if(i[1]-xy[index][1]>10 or i[0]-xy[index][0]>10):
			index=index+1
			xy[index][0]=i[0]
			xy[index][1]=i[1]

def right(i,x):
	for tin in range (0,12):
		if(abs(x[tin]-i[0])<60):
			if(tin+1==1 or tin+1==5 or tin+1==9):
				return 1
			elif(tin+1==2 or tin+1==6 or tin+1==10):
				return 2
			elif(tin+1==3 or tin+1==7 or tin+1==11):
				return 3
			elif(tin+1==4 or tin+1==8 or tin+1==12):
				return 4
def ans(xy,x,an):
	index=0
	for i in xy:
		an.append(right(i,x))
x=[]# alist that stores the refernce x coordinates 
xy=np.zeros((90,2))#stores the final x and y coordinates  
an=[]#stores the final answers 
img_rgb=cv2.imread("sheet.png")#reads the image for which we need to find the answers 
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)#converts the coloured image to gray scale 
template = cv2.imread('template_2.png',0)#this template is used to detect the refernce x coordinates 
template_2=cv2.imread("template_mark.png",0)#reads the black mark which will be later on used to detect the answers 
w, h = template.shape[::-1]#[::-1] inverts
w1,h1 = template_2.shape[::-1]#[::-1] inverts
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)# the template matching tool which is used to detect the refernce points 
res_2= cv2.matchTemplate(img_gray,template_2,cv2.TM_CCOEFF_NORMED)# the template matching tool which is used to detect the answer marks 
threshold = 0.55 #thresholding value(if the match % is greater the 55 then we will accept it as a valid point )
loc_2= np.where( res_2 >=0.85)  #np is the shortform of numpy
loc = np.where( res >= threshold) #np is the shortform of numpy
x.append(loc[1][0])
#print loc_2[1]
#x[0][0]=loc_2[1][0]
temp=zip(*loc[::-1])#inverts the refernce matrix to make it wxl type from lxw type 
temp2=zip(*loc_2[::-1])#inverts the answer point matrix to make it wxl type from lxw type 
#print temp2[0]
xy[0][0]=temp2[0][0]
xy[0][1]=temp2[0][1]
getting_x_coor(x,temp)
print x
getting_xy(temp2,xy)
ans(xy,x,an)
#print x
#print xy

print an
for pt in temp2:
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('final.png',img_rgb)
