import cv2 as cv
import numpy as np

IMAGES = {
  "normal": {
    "path": "./images/Normal.jpg",
    "window_name": "Normal",
  },
}

def show_image(image, window_name):
  image_h = image.shape[0]
  image_w = image.shape[1]

  def trackbar_change(pos):
    pos = pos / 100 # get a scaling factor from trackbar pos
    h = int(image.shape[0] * pos) # scale h
    w = int(image.shape[1] * pos) # scale w
    resized_image = cv.resize(image, (w, h)) # resize image

    cv.resizeWindow(window_name, w, h) # resize window
    cv.imshow(window_name, resized_image) # display resized image
    return


  def insert_trackbar():
    STARTING_TRACKBAR_VALUE = 10
    TRACKBAR_MAXIMUM_SIZE = 10

    cv.createTrackbar(
      'Image scale',
      window_name,
      STARTING_TRACKBAR_VALUE,
      TRACKBAR_MAXIMUM_SIZE,
      trackbar_change,
    )
    return

  cv.namedWindow(window_name, cv.WINDOW_NORMAL)
  cv.imshow(window_name, image)
  insert_trackbar()
  return


image_normal = cv.imread(IMAGES["normal"]["path"])
show_image(image_normal, IMAGES["normal"]["window_name"])

cv.waitKey(0)
cv.destroyAllWindows()
