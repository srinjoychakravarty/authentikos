from siaskynet import Skynet
import webbrowser


def browser_open(url):
    browser_choice = input("\nWould you like to open in browser? [yes (y) | no (n)]")
    if (browser_choice == "yes" or browser_choice == "y"):
        webbrowser.open(url, new=1)

def upload_skynet(filename):
    print("\nUploading to skynet...\n")
    skylink = Skynet.upload_file(filename)
    sia_url = 'https://siasky.net/' + skylink[6:]
    print(f"\nUpload successful! \nSkylink url: {sia_url}")
    browser_open(sia_url)
    return sia_url
    
def write_data():
    same_dir_choice = input("\nIs your media file in the same directory as this script?[yes (y) | no (n)]\n")
    if (same_dir_choice == "yes" or same_dir_choice == "y"):
        filename = ""
        while (filename == ""):
            filename = input("\nName of file including extenstion (e.g. razr.jpg):\n")
            if(filename == ""):
                print("\nFilename cannot be a blank string! \nPlease enter a filename...\n")
        sia_url = upload_skynet(filename)
            
    elif (same_dir_choice == "no" or same_dir_choice == "n"):
        full_path = ""
        while (full_path == ""):    
            full_path = input("\nEnter full path to file ending in / (e.g /home/eos/images/ \n")
            if(full_path == ""):
                print("\nPath cannot be a blank string! \nPlease enter full path directory...\n")
        filename = ""
        while (filename == ""):
            filename = input("\nName of file including extenstion (e.g. razr.jpg):\n")
            if(filename == ""):
                print("\nFilename cannot be a blank string! \nPlease enter a filename...\n")
        full_filename = full_path + filename
        sia_url = upload_skynet(full_filename)
        
    else:
        print(f"\nNo directory information! Thanks for using Authentikos...bye now!")       
    


if __name__ == '__main__':
    upload_continue = True
    while (upload_continue == True):
        upload_choice = input("\nWelcome to Authentikos! \nWould you like to upload media to Skynet? [yes (y) | no (n)] \n")
        if (upload_choice == "yes" or upload_choice == "y"):
            write_data()

        elif (upload_choice == "no" or upload_choice == "n"):
            upload_continue = False
            print(f"\nNot uploading right now? Thanks for using Authentikos...bye now!\n") 

        else:
            upload_continue = False
            print(f"\n No upload decision! Thanks for using Authentikos...bye now!\n") 

    