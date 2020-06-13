from roipoly import RoiPoly
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from PIL import Image
import os

matplotlib.use('Qt5Agg')
points = np.empty((0,3))
for filename in os.listdir('train_images'):
    filename = 'train_images/' + filename
    image = plt.imread(filename)

    plt.imshow(image)
    my_roi = RoiPoly(color='r')  # draw new ROI in red colo
    mask = my_roi.get_mask(image[:, :, 0])
    img = plt.imread(filename)
    points = np.vstack((points,img[mask]))

np.savetxt('ball.csv',points,delimiter=',')


