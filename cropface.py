from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib import pyplot
import os

def face_detection(file):
    # load image from file
    pixels = pyplot.imread(file)
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    if faces:
        return True
    else:
        return False

def crop_face(filename, name):
    # load image from file
    pixels = pyplot.imread(filename)
    # detect faces in the image
    result_list = detector.detect_faces(pixels)
    # plot each face as a subplot
        # get coordinates
    if len(result_list) == 1:
        for i in range(len(result_list)):
            x1, y1, width, height = result_list[i]['box']
            x2, y2 = x1 + width, y1 + height
            # define subplot
            pyplot.subplot(1, len(result_list), i+1)
            pyplot.axis('off')
            # plot face
            pyplot.imshow(pixels[y1:y2, x1:x2])
        # show the plot
        pyplot.savefig(cwd + newdir + '\\' + name, bbox_inches='tight', pad_inches = 0.)
    else:
        pass

dir = 'tw\\newnayeon'
newdir = '\\tw\\cropnayeon'
cwd = os.getcwd()
# create the detector, using default weights
detector = MTCNN()
counter = 1
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    crop_face(f, filename)
    print(f'{counter}. Image {f} has been cropped successfully')
    counter += 1