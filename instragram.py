import requests
from datetime import datetime
from requests.api import post
import config
import json
import pandas as pd
import photoNumber



def postInstagram(imageNumber):
    colors = pd.read_csv('ColorList.csv')
    name = colors['name'].iloc[imageNumber]
    hexa = colors['hex'].iloc[imageNumber]
    r = str(colors['red'].iloc[imageNumber])
    g = str(colors['green'].iloc[imageNumber])
    b = str(colors['blue'].iloc[imageNumber])
    caption = name + '  - ' + hexa + '\r\nRGB(' + r + ", " + g + ", " + b + ")\r\n\r\n#color #rainbow #chroma"
    
    imageLocation = 'https://raw.githubusercontent.com/jorgeroma/rainbowColor/main/images/{}.jpeg'.format(imageNumber)


    postUrl = 'https://graph.facebook.com/{}/media'.format(config.ig_user_id)
    payload = {
        'image_url': imageLocation,
        'caption': caption,
        'access_token': config.ig_token
    }

    r = requests.post(postUrl, data=payload)
    print(r.text)

    result = json.loads(r.text)
    if 'id' in result:
        creationId = result['id']

        secondUrl = 'https://graph.facebook.com/{}/media_publish'.format(config.ig_user_id)
        secondPayload = {
            'creation_id': creationId,
            'access_token': config.ig_token
        }

        r = requests.post(secondUrl, data=secondPayload)
        print('-------------------Imagen publicada en Instagram-------------------')
        print(r.text)
    
    else:
        print('Ha habido un problema')


def start():
    try:
        # nFoto = photoNumber.getPhotoNumber()
        postInstagram(0);
        # photoNumber.setPhotoNumber(nFoto+1)
    except:
        print('ERROR')

start()

