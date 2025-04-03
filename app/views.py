from flask import Blueprint, request, render_template, current_app

# to help us find the structural similarity score between og image and tampered image
from skimage.metrics import structural_similarity
# to grab the  curves that join points of equal intensity value in an image (aka countours)
import imutils
# to use computer vision for all the image processing requirements
import cv2
# to download and visualize the image
from PIL import Image
# to fetch the data from the URLs
import requests
# creating two libraries to store our images using shell commands
import os

# Define blueprint
main = Blueprint('main', __name__)

# Adding path to config
# app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
# app.config['EXISTING_FILE'] = 'app/static/original'
# app.config['GENERATED_FILE'] = 'app/static/generated'

# Route to home page
@main.route('/', methods=['GET', 'POST'])
def index():

    # Execute if request is get
    if request.method == 'GET':
        return render_template('index.html')

    # Execute if request is post
    if request.method == 'POST':
        # Get uploaded image
        file_upload = request.files['file_upload']
        filename = file_upload.filename

        # Resize and save uploaded image
        uploaded_image = Image.open(file_upload).resize((250,160))
        uploaded_image.save(os.path.join(current_app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Read uploaded and original image as array
        original_image = cv2.imread(os.path.join(current_app.config['EXISTING_FILE'], 'image.jpg'))
        uploaded_image = cv2.imread(os.path.join(current_app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # convert to greyscale
        original_grey = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        uploaded_grey = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

        # Computing the Structural Similarity Index (SSIM) betweem both images and returning the diff image (full=)
        (score, diff) = structural_similarity(original_grey, uploaded_grey, full=True)
        diff = (diff * 255).astype("uint8")

        # Calculating threshold and contours
        # Here we transform the diff grayscale image into a binary image
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Here we compute the bounding box of the countour and then draw the bounding box on both input images to represent where they differ
        for c in cnts:
            # applying contours on image --> w= width | h= height
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Save all output images (if requested)
        cv2.imwrite(os.path.join(current_app.config['GENERATED_FILE'], 'image_original.jpg'), original_image)
        cv2.imwrite(os.path.join(current_app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_image)
        cv2.imwrite(os.path.join(current_app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
        cv2.imwrite(os.path.join(current_app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)
        return render_template('index.html', prod=str(round(score * 100, 2)) + '%' + 'correct')

# Main function
#if __name__ == '__main__':
#    app.run(debug=True)