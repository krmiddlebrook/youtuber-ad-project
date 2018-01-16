"""User inputs a youtube video url and the script returns the video thumbnail
    and then analysis the objects in the thumbnail"""

# [START import_libraries]
import argparse
import io
import base64
from google.cloud import vision
from google.cloud.vision import types
import pafy
# [END import_libraries]

def get_thumb(youtube_url):
    """Process the user input youtube url and return url path to
    the video thumbnail"""
    url     = str(youtube_url)
    video   = pafy.new(url)
    tmp_thumb_url = ""
    tmp_thumb_url = str(video.bigthumbhd)
    if tmp_thumb_url != "":
        thumb_url = tmp_thumb_url
    else:
        thumb_url = str(video.thumb)
    print("Thumbnail url: " + thumb_url)
    print()
    print('Video description: ' + video.description)
    print()
    return thumb_url


# [START def_detect_labels_uri]
def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client  = vision.ImageAnnotatorClient()
    image   = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels, Scores, and Topicality:')

    for label in labels:
        print("Label: " + label.description + "\n" +
              "Score: " + str(label.score) + "\n" +
              "Topicality: " + str(label.topicality) + "\n")
# [END def_detect_labels_uri]




# [START run_application]
if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args    = parser.parse_args()
    thumb_uri = get_thumb(args.image_file)
    detect_labels_uri(thumb_uri)
# [END run_application]
