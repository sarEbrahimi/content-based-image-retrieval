import cv2
import glob
import findHist

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

path = 'att/*'
files = glob.glob(path)
att = []
for file in files:
    ax = cv2.imread(file)
    att.append(cv2.cvtColor(ax,cv2.COLOR_BGR2RGB))

# we calculated the hist for base ima
img = cv2.imread('60.png')
base_hist = findHist.findhist(img)

att_hist = []
# for every picure calculate the hist
for i in range( len(att) ):
    image = cv2.imread(i)
    histogram = findHist.findhist(image)
    att_hist.append(histogram)

flag = 0
for i in range( len(att) ):
    # now compare them with each other and store the largest amount
    compared = cv2.compareHist(base_hist,att_hist[i], cv2.HISTCMP_CORREL)
    if compared <= 2147483647:
        flag = i
    else:
        continue
