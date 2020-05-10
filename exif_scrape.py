from geopy.geocoders import Here
from googletrans import Translator
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import requests, pprint

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val
    return labeled

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")
    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
    return geotagging

def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0
    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds
    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    return (lat,lon)

def get_location(geotags):
    coords = get_coordinates(geotags)
    uri = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json'
    headers = {}
    params = {
        'app_id': 'OG9RuhSv9sPPp5vva726',
        'app_code': 'ueVEcwt9dH9LH0y2MHLOVQ',
        'prox': "%s,%s" % coords,
        'gen': 9,
        'mode': 'retrieveAddresses',
        'maxresults': 1,
    }
    response = requests.get(uri, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(str(e))
        return {}

def make_thumbnail(filename):
    img = Image.open(filename)
    (width, height) = img.size
    if width > height:
        ratio = 50.0 / width
    else:
        ratio = 50.0 / height
    img.thumbnail((round(width * ratio), round(height * ratio)), Image.LANCZOS)

    thumbnail_var = 'thumb_' + filename
    img.save(thumbnail_var)
    return(thumbnail_var)

def print_output(photo):
    exif = get_exif(photo)
    labeled = get_labeled_exif(exif)
    geotags = get_geotagging(exif)
    coords = get_coordinates(geotags)
    geocoder = Here(apikey = 'jqd95MUaWzULxJk8ci0uHrSQ9kn2L8dDdg1kz0xjvcI')
    full_address = str((geocoder.reverse("%s,%s" % coords)))
    make = labeled.get('Make')
    model = labeled.get('Model')
    device = str(make + " " + model)
    software = labeled.get('Software')
    datetime = labeled.get('DateTime')
    width = labeled.get('ExifImageWidth')
    height = labeled.get('ExifImageHeight')
    offset = labeled.get('ExifOffset')
    flash = labeled.get('Flash')
    shutter = labeled.get('ShutterSpeedValue')
    zoom = labeled.get('DigitalZoomRatio')
    aperture = labeled.get('ApertureValue')
    focus = labeled.get('FocalLength')
    subsectime = labeled.get('SubsecTime')
    exposure = labeled.get('ExposureTime')
    fnumber = labeled.get('FNumber')
    isospeed = labeled.get('ISOSpeedRatings')
    dict = {'Address': full_address, 'Device': device, 'Software': software,
    'Timestamp': datetime, 'Height': height, 'Width': width, 'Offset': offset,
    'Flash': flash, 'Shutter': shutter, 'DigitalZoom': zoom, 'Aperture':  aperture,
    'Focus': focus, 'SubSecondTime': subsectime, 'Exposure': exposure, 'FNumber': fnumber,
    'ISOSpeedRating': isospeed}
    return dict

if __name__ == '__main__':
    metadata = print_output('stove.jpg')
    foreign_address = metadata.get('Address')
    translator = Translator()
    translated = translator.translate(foreign_address)
    english_address = translated.text
    metadata['Address'] = english_address
    pp = pprint.PrettyPrinter(indent = 4, width = 41)
    pp.pprint(metadata)
    print(type(metadata))
    download_choice = input("\nWould you like to download the image metadata as a .json file? [yes (y) | no (n)]\n")
    if (download_choice == "yes" or download_choice == "y"):
        filename = ""
        while (filename == ""):
            filename = input("\nWhat would you like to name the file? (e.g. stove_metadata.json):\n")
            if(filename == ""):
                print("\nFilename cannot be a blank string! \nPlease enter a filename...\n")
        with open('person.txt', 'w') as json_file:
            json.dump(person_dict, json_file)
