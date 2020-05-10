from colorama import Fore
from geopy.geocoders import Here
from googletrans import Translator
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
from skynet import read_data
import inquirer, json, pprint, requests

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

def read_exif(filename):
    try:
        im = Image.open(filename)
        metadata = print_output('img1')
        foreign_address = metadata.get('Address')
        translator = Translator()
        translated = translator.translate(foreign_address)
        english_address = translated.text
        metadata['Address'] = english_address
        pp = pprint.PrettyPrinter(indent = 4, width = 41)
        pp.pprint(metadata)
    except IOError:
        print(Fore.MAGENTA + f"{filename} is not a valid image file" + Fore.RESET)
        metadata = {}
    return metadata

def scrape_metadata():
    question = [inquirer.List('action', message = "Where is your image stored", choices = ['Local', 'Skynet'])]
    answer = inquirer.prompt(question)
    chosen_function = answer['action']
    if (chosen_function == 'Local'):
        same_dir_choice = input("Is your image in the same directory as this script? [yes (y) | no (n)]\n")
        if (same_dir_choice == "yes" or same_dir_choice == "y"):
            filename = ""
            while (filename == ""):
                filename = input("\nName of file:\n")
                if(filename == ""):
                    print(Fore.MAGENTA + "\nFilename cannot be a blank string! \nPlease enter a filename...\n" + Fore.RESET)
            exif_metadata = read_exif(filename)

        elif (same_dir_choice == "no" or same_dir_choice == "n" + Fore.RESET):
            full_path = ""
            while (full_path == ""):
                full_path = input("\nEnter full path to file ending in / (e.g /home/eos/images/ \n")
                if(full_path == ""):
                    print(Fore.MAGENTA + "\nPath cannot be a blank string! \nPlease enter full path directory...\n" + Fore.RESET)
            filename = ""
            while (filename == ""):
                filename = input("\nName of file: (e.g. img1):\n")
                if(filename == ""):
                    print(Fore.MAGENTA + "\nFilename cannot be a blank string! \nPlease enter a filename...\n" + Fore.RESET)
            full_filename = full_path + filename
            exif_metadata = read_exif(full_filename)

        else:
            print(Fore.MAGENTA + f"\nNo directory information! Thanks for using Authentikos...bye now!" + Fore.RESET)

    elif (chosen_function == 'Skynet'):
        filename = read_data()
        print("\n")
        exif_metadata = read_exif(filename)
    return exif_metadata

if __name__ == '__main__':
    question = [inquirer.List('action', message = "Welcome to Authentikos! What skynet action do you need?", choices = ['Scrape Image Metadata', 'Download Metadata JSON'])]
    answer = inquirer.prompt(question)
    chosen_function = answer['action']
    if (chosen_function == 'Scrape Image Metadata'):
        scrape_continue = True
        while (scrape_continue == True):
            scrape_choice = input("\nWould you like to scrape exif metadata of an image? [yes (y) | no (n)]\n")
            if (scrape_choice == "yes" or scrape_choice == "y"):
                exif_metadata = scrape_metadata()
            elif (scrape_choice == "no" or scrape_choice == "n"):
                scrape_continue = False
                print(Fore.MAGENTA + f"\nNot scraping metadata right now? Thanks for using Authentikos...bye now!\n" + Fore.RESET)
            else:
                upload_continue = False
                print(Fore.MAGENTA + f"\nNo scrape decision! Thanks for using Authentikos...bye now!\n" + Fore.RESET)

    elif (chosen_function == 'Download Metadata JSON'):
        download_choice = input("\nWould you like to download the image metadata as a .json file? [yes (y) | no (n)]\n")
        if (download_choice == "yes" or download_choice == "y"):
            exif_metadata = scrape_metadata()
            filename = ""
            while (filename == ""):
                filename = input("\nWhat would you like to name the file? (e.g. metadata1):\n")
                if(filename == ""):
                    print(Fore.MAGENTA + "\nFilename cannot be a blank string! Please enter a filename..." + Fore.RESET)
            print(Fore.YELLOW + f"\nDownloading {filename} to disk...\n" + Fore.RESET)
            with open(filename, 'w') as json_file:
                json.dump(exif_metadata, json_file)

        elif (download_choice == "no" or download_choice == "n"):
            print(Fore.MAGENTA + f"\nNot downloading json right now? Thanks for using Authentikos...bye now!\n" + Fore.RESET)
        else:
            upload_continue = False
            print(Fore.MAGENTA + f"\nNo json decision! Thanks for using Authentikos...bye now!\n" + Fore.RESET)
