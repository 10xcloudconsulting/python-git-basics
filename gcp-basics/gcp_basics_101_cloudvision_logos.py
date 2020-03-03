#!/usr/bin/env python3

#This file explores some basics for using GCP Cloud Vision

# Imports the Google Cloud client library
from google.cloud import vision
import io

def detect_text(path):
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print(type(texts))
    i = 0
    for text in texts:
        print("i is : " + str(i))
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: ''https://cloud.google.com/apis/design/errors'.format(response.error.message))

#Call the above custom function using a local image file
#detect_text("/Users/laks/Downloads/MeetingSMagora1.jpg")


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision

    #client = vision.ImageAnnotatorClient()

    # The Vision API client libraries accesses the global API endpoint (vision.googleapis.com) by default. To store and process your data in the European Union only, you need to explicitly set the endpoint (eu-vision.googleapis.com).
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#Call the above custom function using a image object stored in Cloud Storage bucket - https://storage.googleapis.com/[BUCKET_NAME]/[OBJECT_NAME]
#uri_str = "https://storage.googleapis.com/" + "cloudvisionapitut-268410-10xcc-python-basics-121/" + "MeetingSMagora1.jpg"
#uri_str = "https://cloudvisionapitut-268410-10xcc-python-basics-121/MeetingSMagora1.jpg"
#uri_str = "gs://cloudvisionapitut-268410-10xcc-python-basics-121/MeetingSMagora1.jpg"
uri_str = "gs://cloud-samples-data/vision/ocr/sign.jpg"
print("URI String for text_detection is : " + uri_str)
#detect_text_uri(uri_str)

def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#Call the above function
uri_str_doc = "gs://vision-api-handwriting-ocr-bucket/handwriting_image.png"
print("URI String for document_text_detection is : " + uri_str_doc)
detect_document_uri(uri_str_doc)
