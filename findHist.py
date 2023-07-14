import cv2

def findhist(img):
    img = cv2.imread(img , cv2.COLOR_BGR2RGB)

    hist_base = cv2.calcHist([img], [0,1,2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    hist_base = cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist_base


img = cv2.imread('60.png')
h = findhist(img)
print(h)