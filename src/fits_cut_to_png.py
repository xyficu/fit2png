import f2n
import sys
import Image
import os

import pyfits
import time



"""
#author:  xyf
#email:   xyficu@nao.cas.cn
#Date:    20140829

update history
20141014    add time information on the top left corner
20140902    fix the float number error of inputing float coordinates
            if the -s is empty, the circle will not be painted
            change output file format to JPEG
"""


version = "0.1.2" 

def FitsCutToPng(inputfile, outputfile, x, y, a, s):
    """
        convert fits file to png/jpg with assigned size
        
        -inputfile     the input fits file name including path
        -outputfile    the output png file name including path
        -x             coordinate x
        -y             coordinate y
        -a             border of the square picture around (x, y)
        -s             the string under the circled star
        """
   
   
    if(x<0 or x>3056 or y<0 or y>3056 or a<0 or a>3056):
        print "x or y or a is out of border, please check!"
        return
 
#     if(x-a<0 or x+a>3056 or y-a<0 or y+a>3056):
#         print "x-a or x+a or y-a or y+a is out of border, please check!"
    if x-a<0:
        left=0
        p=a-x
    else:
        left=x-a
        p=0
 
    if x+a>3056:
        right=3056
    else:
        right=x+a
        
    if y-a<0:
        top=0
        q=y
    else:
        top=y-a
        q=a
        
    if y+a>3056:
        bottom=3056
        q=a-(3056-y)
    else:
        bottom=y+a
        q=0

#     print "-----"
#     print p
#     print q
#     print len(sys.argv)
#     print "-----"
    
#    open input file
    tmpImage = f2n.fromfits(inputfile)
    tmpImage.crop(left, right, top, bottom)
    tmpImage.setzscale("auto", "flat", 3, 100000, 300, 65000)
    
    tmpImage.makepilimage("lin", negative = False)
    if s!="":
        tmpImage.drawcircle(x, y, 5, (0,255,0), s)
    if x==1528 and y==1528 and a==1528:
        Info = inputfile
        tmpImage.writeinfo([Info], colour=(255,0,0))
    
    tmpImage.tonet("tmp.png")

#    convert png to jpg
    fgImg=Image.open("tmp.png")
    bgImg=Image.new("RGB", (2*a, 2*a), (100,100,100))
    bgImg.paste(fgImg,(p,q))
    bgImg.save(outputfile, "JPEG")
    os.system("rm tmp.png")
    
    
if __name__ == '__main__':    
    print "version: " + version
    
    if len(sys.argv)==7:
        FitsCutToPng(str(sys.argv[1]), str(sys.argv[2]), int(float(sys.argv[3])), int(float(sys.argv[4])), int(float(sys.argv[5])), str(sys.argv[6]))
    else:
        print "Arguments are not correct!"
        
    


# f=iraf.imaccess("20131203_m06-0848+50_1053.fit")


# fitsFile = pyfits.open("20131203_m06-0848+50_1053.fit");
# #b=fitsFile['primary'].data[0:3,0:3]
# b=pyfits.PrimaryHDU(fitsFile['primary'].data[0:300,0:300])
# head=fitsFile['primary'].header
# b.header=head
# b.header['12345678']=67
# b.writeto('out.fit')







