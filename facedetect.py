from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib import pyplot

# draw an image with detected objects
def draw_image_with_boxes(filename, result_list):
    # load the image
    data = pyplot.imread(filename)

    # plot the image
    pyplot.imshow(data)

    # get the context for drawing boxes
    ax = pyplot.gca()

    # plot each box
    for result in result_list:
        # get coordinates
        x, y, width, height = result['box']
        # create the shape
        rect = Rectangle((x, y), width, height, fill = False, color = 'red')
        #draw the box
        ax.add_patch(rect)
    #show the plot
    pyplot.show()

def crop_face(filename, result_list):
    # load the image
    data = pyplot.imread(filename)
    # plot each face as a subplot
        # get coordinates
    for i in range(len(result_list)):
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
		# define subplot
        pyplot.subplot(1, len(result_list), i+1)
        pyplot.axis('off')
		# plot face
        pyplot.imshow(data[y1:y2, x1:x2])
	# show the plot
    # pyplot.savefig('new' + filename, bbox_inches='tight', pad_inches = 0., transparent = True)

filename = '154145805_781249495816213_637559880100306218_n.jpg'
# load image from file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
# display faces on the original image
draw_image_with_boxes(filename, faces)