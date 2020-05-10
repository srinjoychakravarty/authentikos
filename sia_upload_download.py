from siaskynet import Skynet
from PIL import Image
import inquirer, webbrowser
from colorama import Fore, Style

def browser_open(url):
    browser_choice = input("\nWould you like to open in browser? [yes (y) | no (n)]\n")
    if (browser_choice == "yes" or browser_choice == "y"):
        open_type = ""
        while (open_type != "1" or open_type != "2"):
            open_type = input("\nNew window (1) or New tab (2)? \n")
            if (open_type == "1" or open_type == "2"):
                webbrowser.open(url, new = int(open_type))
            else:
                break
    elif (browser_choice == "no" or browser_choice == "n"):
        print(Fore.MAGENTA + "\nNot opened in browser! Thanks for using Authentikos!\n" + Fore.RESET)
    else:
        print(Fore.MAGENTA + "\nNo browser decision! Thanks for using Authentikos!\n" + Fore.RESET)

def upload_skynet(filename):
    print(Fore.YELLOW + "\nUploading to skynet...\n" + Fore.RESET)
    skylink = Skynet.upload_file(filename)
    sia_url = 'https://siasky.net/' + skylink[6:]
    print(f"Upload successful!\n\nSkylink url: {sia_url}")
    browser_open(sia_url)
    return sia_url

def write_data():
    same_dir_choice = input("\nIs your media file in the same directory as this script? [yes (y) | no (n)]\n")
    if (same_dir_choice == "yes" or same_dir_choice == "y"):
        filename = ""
        while (filename == ""):
            filename = input("\nName of file:\n")
            if(filename == ""):
                print(Fore.MAGENTA + "\nFilename cannot be a blank string! \nPlease enter a filename...\n" + Fore.RESET)
        try:
            im = Image.open(filename)
            sia_url = upload_skynet(filename)
        except IOError:
            print(Fore.MAGENTA + f"{filename} is not a valid image file" + Fore.RESET)
            sia_url = ""
        return sia_url

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
        sia_url = upload_skynet(full_filename)
        return sia_url
    else:
        print(Fore.MAGENTA + f"\nNo directory information! Thanks for using Authentikos...bye now!" + Fore.RESET)

def read_data():
    skylink_url = ""
    while (skylink_url == ""):
        skylink_url = input("\nEnter the Skylink url to download from: \n") or "https://siasky.net/fAMK9kP1ylIWICslP6TMvXmGMCMn6sTfWLc56oAmeSgxRg"
        print(Fore.BLUE + f"\nEntered url: {skylink_url}" + Fore.RESET)
        if(skylink_url == ""):
            print(Fore.MAGENTA + "\nSkylink url cannot be a blank string! \nPlease enter a Skylink url...\n" + Fore.RESET)
    sia_id = skylink_url[19:]
    filename = ""
    while (filename == ""):
        filename = input("\nEnter filename to save download as (e.g. img1): \n") or "img1"
        print(Fore.BLUE + f"\nEntered filename: {filename}" + Fore.RESET)
        if(filename == ""):
            print(Fore.MAGENTA + "\nFilename cannot be a blank string! \nPlease enter a filename (e.g. img1)...\n" + Fore.RESET)
    print(Fore.YELLOW + "\nDownloading from skynet...\n" + Fore.RESET)
    Skynet.download_file(filename, sia_id)
    print(f"Download successful and file saved as {filename}")
    image_open = input("\nWould you like to open the downloaded image? [yes (y) | no (n)] \n")
    if (image_open == "yes" or upload_choice == "y"):
        im = Image.open(r"./" + filename)
        im.show()
    elif (image_open == "no" or upload_choice == "n"):
        print(Fore.MAGENTA + f"\nNot displaying image right now? Thanks for using Authentikos...bye now!\n" + Fore.RESET)
    else:
        print(Fore.MAGENTA + f"\nNo image open decision! Thanks for using Authentikos...bye now!\n" + Fore.RESET)

if __name__ == '__main__':
    question = [inquirer.List('action', message = "Welcome to Authentikos! What skynet action do you need?", choices = ['Upload', 'Download'])]
    answer = inquirer.prompt(question)
    chosen_function = answer['action']
    if (chosen_function == 'Upload'):
        upload_continue = True
        while (upload_continue == True):
            upload_choice = input("\nWould you like to upload media to Skynet? [yes (y) | no (n)] \n")
            if (upload_choice == "yes" or upload_choice == "y"):
                write_data()
            elif (upload_choice == "no" or upload_choice == "n"):
                upload_continue = False
                print(Fore.MAGENTA + f"\nNot uploading right now? Thanks for using Authentikos...bye now!\n" + Fore.RESET)
            else:
                upload_continue = False
                print(Fore.MAGENTA + f"\nNo upload decision! Thanks for using Authentikos...bye now!\n" + Fore.RESET)
    elif (chosen_function == 'Download'):
        download_continue = True
        while (download_continue == True):
            upload_choice = input("\nWould you like to download media from Skynet? [yes (y) | no (n)] \n")
            if (upload_choice == "yes" or upload_choice == "y"):
                read_data()
            elif (upload_choice == "no" or upload_choice == "n"):
                download_continue = False
                print(Fore.MAGENTA + f"\nNot downloading right now? Thanks for using Authentikos...bye now!\n" + Fore.RESET)
            else:
                download_continue = False
                print(Fore.MAGENTA + f"\nNo download decision! Thanks for using Authentikos...bye now!\n" + Fore.RESET)
