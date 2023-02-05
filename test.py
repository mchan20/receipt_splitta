import requests
import json
import pprint
import pandas as pd


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='K83145254888957', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


# Use examples:
# test_file = ocr_space_file(filename='example_image.png', language='pol')
# test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')

# test_url = ocr_space_url(url='https://i.imgur.com/HXQtfqIm.png')
# test_url = ocr_space_url(url='https://i.imgur.com/tO6btZG.jpg')
test_url = ocr_space_url(url='https://i.imgur.com/KyKONQc.png')

#the most buggy ass thing in the world this is what happens when you use the free version ig

# print(test_url)

jdata = json.loads(test_url)
entries = jdata["ParsedResults"][0]
df = pd.DataFrame(entries)

pprint.pprint(df)

print(df.iat[0,3])

