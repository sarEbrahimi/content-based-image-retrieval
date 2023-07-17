# content-based-image-retrieval

<h4>Goals:</h4>
  find histogram of images
  compare them with each other
  return the most similar picture

<h4>Histogram in opencv:</h4>
  cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
  . images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
  . channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
  . mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
  . histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
  . ranges : this is our RANGE. Normally, it is [0,256].

<h4>Compare histogram in opencv:</h4>

  cv2.compareHist(H1, H2, method)
  
  The cv2.compareHist function takes three arguments: 
  H1, which is the first histogram to be compared,
  H2, the second histogram to be compared,
  and method, which is a flag indicating which comparison method should be performed.
  
  The method flag can be any of the following:
  . cv2.HISTCMP_CORREL: Computes the correlation between the two histograms.
  . cv2.HISTCMP_CHISQR: Applies the Chi-Squared distance to the histograms.
  . cv2.HISTCMP_INTERSECT: Calculates the intersection between two histograms.
  . cv2.HISTCMP_BHATTACHARYYA: Bhattacharyya distance, used to measure the “overlap” between the two histograms.

<h4>What did we do?</h4>
  in #findHist implemented a function to capture the color histogram




  
