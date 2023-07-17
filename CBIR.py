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
print(f'we have {len(att)} pictures')

# we calculated the hist for base img
img = cv2.imread('60.png')
base = findHist.findhist(img)
base_hist = cv2.compareHist(base, base, method=cv2.HISTCMP_CORREL)
print(base_hist)
att_hist = []
# for every picure calculate the hist
for image in att:
    histogram = findHist.findhist(image)
    print('ok1')
    histogram = cv2.compareHist(base, histogram, method=cv2.HISTCMP_CORREL)
    print('ok2')
    print(histogram)
    att_hist.append(histogram)

flag = -2147483647
counter = 0
for i in att_hist:
    # now compare them with each other and store the largest amount
    if i >= flag:
        flag = i
        c = counter
    counter += 1

print('the picture has the most similarity is: ',c)
