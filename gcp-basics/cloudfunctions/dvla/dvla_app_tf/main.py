# Copyright 2018, Google, LLC.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START functions_ocr_setup]
import base64
import json
import os
import requests
import re

from google.cloud import pubsub_v1
from google.cloud import storage
from google.cloud import translate
from google.cloud import vision
from flask import escape

vision_client = vision.ImageAnnotatorClient()
translate_client = translate.Client()
publisher = pubsub_v1.PublisherClient()
storage_client = storage.Client()

project_id = os.environ['GCP_PROJECT']
print("Project Id is : {}".format(project_id))

with open('config.json') as f:
    data = f.read()
config = json.loads(data)
# [END functions_ocr_setup]

# [START functions_dvla_verify_vehicle_reg]
def verify_vehicle_reg(request):
    print('Entered verify_vehicle_reg function')

    request_json = request.get_json(silent=True)
    request_args = request.args
    request_files = request.files
    request_form = request.form
    request_data = request.data

    print("Request content")
    print(request_json)
    print(request_args)
    # curl -F option
    print(request_files)
    print(request_form)
    print(request_data)
    print("Request content End")

    if request_json and 'name' in request_json:
        num_plate_image = request_json['name']
    elif request_args and 'name' in request_args:
        num_plate_image = request_args['name']
    else:
        num_plate_image = 'gs://regulatory-ai-pocs-devbe85-10xcc-gcf-ocr-images/IMG_6647.HEIC'

    #Extract Vehicle Registration Number from the Image
    print("Name param is : {}".format(num_plate_image))
    regNumTokens = extractRegistrationNum(num_plate_image)

    #Get the DVLA API Key from Secrets Manager
    print('Getting API Key from Secrets Manager')
    api_key = access_secret_version(project_id, config['DVLA_API_KEY_NAME'], "latest")

    #url = 'https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
    url = config['DVLA_API_URL']
    head_dict = {"Content-Type": "application/json", "Accept": "application/json", "x-api-key": api_key}

    for token in regNumTokens:
        print("Registration Num is : {}".format(token))
        pload = {"registrationNumber": str(token)}
        response = requests.post(url, headers = head_dict, json=pload)
        print(response.text)
        print(response.json())
        print(response.status_code)
        if (response.status_code == 200):
            print("Vehicle found")
            return response.text
        else:
            print("Iterating")
    return response.text

    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))
    """


# [END functions_dvla_verify_vehicle_reg]

def access_secret_version(project_id, secret_id, version_id):
#def access_secret_version("regulatory-ai-pocs-devbe85", "10xcc-dvla-api-key", "latest"):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = client.secret_version_path(project_id, secret_id, version_id)

    # Access the secret version.
    response = client.access_secret_version(name)

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode('UTF-8')
    return payload
    #print('Plaintext: {}'.format(payload))

def extractRegistrationNum(image):
    print("In Extract Registration Number local function")

    #Call Vision API and obtain the Text Tokens
    regNumTokens = detect_text(image)

    #regNumToken = "KV16MYL"
    return regNumTokens

# [START functions_ocr_detect]
def detect_text(image_uri):
    print('Looking for text in image {}'.format(image_uri))

    text_detection_response = vision_client.text_detection({
        'source': {'image_uri': image_uri}
    })

    """
    If image is passed as stream in the Http Request us the below. Pass the image content object to text_detection method

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    """

    annotations = text_detection_response.text_annotations
    if len(annotations) > 0:
        text = annotations[0].description
    else:
        text = ''
    print('Extracted text {} from image ({} chars).'.format(text, len(text)))
    print(text.split('\n'))
    token_list = text.split('\n')
    pattern = re.compile("([A-Z])([A-Z]).. *([A-Z])([A-Z])([A-Z])")
    potential_veh_reg = []
    for i in token_list:
        print(i)
        print(len(i.strip()))
        if pattern.match(i.strip()):
            print('Potential Vehicle Reg')
            potential_veh_reg.append(i.strip())

    print(potential_veh_reg)
    return potential_veh_reg
