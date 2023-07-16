import cv2

def findhist(img):

    hist_base = cv2.calcHist([img], [0,1,2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

    hist_base = cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    hist_base = cv2.compareHist(hist_base, hist_base, method=cv2.HISTCMP_CORREL)
    return hist_base
