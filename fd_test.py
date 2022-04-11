from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib import pyplot
import os
import shutil

# # draw an image with detected objects
# def draw_image_with_boxes(filename, result_list):
#     # load the image
#     data = pyplot.imread(filename)

#     # plot the image
#     pyplot.imshow(data)

#     # get the context for drawing boxes
#     ax = pyplot.gca()

#     # plot each box
#     for result in result_list:
#         # get coordinates
#         x, y, width, height = result['box']
#         # create the shape
#         rect = Rectangle((x, y), width, height, fill = False, color = 'red')
#         #draw the box
#         ax.add_patch(rect)
#     #show the plot
#     pyplot.show()

def face_detection(file):
    # load image from file
    pixels = pyplot.imread(file)
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    if faces:
        return True
    else:
        return False

dir = 'tw\\nayeon'
newdir = '\\tw\\newnayeon'
cwd = os.getcwd()
# create the detector, using default weights
detector = MTCNN()
counter = 1
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f) and face_detection(f) == True:
        shutil.move(f, cwd + newdir)
        print(f'{counter}. Image {f} has been moved successfully')
        counter += 1

# # display faces on the original image
# draw_image_with_boxes(filename, faces)