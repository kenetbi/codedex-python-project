import imageio.v3 as iio

filenames = ['cat1.png', 'cat2.png', 'cat3.png', 'cat4.png']  # List of image filenames
images = []

for filename in filenames: # Read each image and append to the list
    images.append(iio.imread(filename))  #.imread reads the image based on the filepath

iio.imwrite("running_cat.gif", images, duration = .5, loop = 0)  # duration in milliseconds, loop=0 for infinite loop