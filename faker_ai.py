from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import inquirer

def label_article(url_choice):
    CHROME_PATH = '/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH, options = chrome_options)
    driver.get("https://www.fakerfact.org/")
    driver.implicitly_wait(4) # delay ensures link loads from cnn
    inputElement = driver.find_element_by_name("url")
    inputElement.send_keys(url_choice)
    inputElement.send_keys(Keys.ENTER)
    try:
        walt_list = ((driver.find_element_by_xpath("//div[contains(@class, 'ff-flag-row form-row')]")).text).splitlines()
        label = walt_list[0]
        confidence = walt_list[1]
        print(f"\n\nArticle Label: {label}\nConfidence Score: {confidence}")                
        try:
            classifier_justification = ((driver.find_element_by_xpath("//div[contains(@class, 'border-bottom ml-2 mb-3')]")).text).splitlines()[0]
            print(f"\n{classifier_justification}\n")
            phrase_choice_question = [inquirer.List('action', message = "Would you like to see the phrases used by our AI to classify?", choices = ['Yes', 'No'])]
            phrase_choice_answer = inquirer.prompt(phrase_choice_question)
            chosen_function = phrase_choice_answer['action']
            if (chosen_function == 'Yes'):
                indicators = (driver.find_element_by_xpath("//ul[contains(@class, 'ff-copy')]")).text
                print(indicators)
        except:
            print("Article has no warning indicators!")
    except:
        too_short_alert = (driver.find_element_by_xpath("//ul[contains(@class, 'alert-danger')]")).text
        print(too_short_alert)

if __name__ == '__main__':
    question = [inquirer.List('action', message = "Welcome to Authentikos! Would you like to classify an article?", choices = ['Yes', 'No'])]
    answer = inquirer.prompt(question)
    chosen_function = answer['action']
    if (chosen_function == 'Yes'):
        classify_continue = True
        while (classify_continue == True):
            url_choice = ""
            while (url_choice == ""):
                url_choice = input("\nEnter url of the news article you would like to classify\n(e.g. https://www.bbc.com/news/live/world-52539905):\n\n> ") or "https://www.huzlers.com/teen-sues-juul-claims-vaping-made-him-homosexual/"
                if(url_choice == ""):
                    print("\nNews article url can't be a blank string!\n")
            label_article(url_choice)
            continue_question = [inquirer.List('action', message = "\n\nWould you like to classify other articles?", choices = ['Yes', 'No'])]
            continue_answer = inquirer.prompt(continue_question)
            chosen_function = continue_answer['action']
            if (chosen_function == 'No'):
                classify_continue = False
                print("Thank you for using Authentikos! Bye now...")
    else:
        print("Thank you for using Authentikos! Bye now...")
