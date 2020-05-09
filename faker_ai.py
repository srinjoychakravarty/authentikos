from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import inquirer

def label_article(url_choice, label_definitions):
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
        output_definition = label_definitions.get(label)
        walt_ai_msg = (driver.find_element_by_xpath("//div[contains(@class, 'h1 mb-4')]")).text
        print(f"\nAI Conclusion: {walt_ai_msg}")
        print(f"\nArticle Label: {label}\n\nConfidence Score: {confidence}\n\nLabel Defintion: {output_definition}")
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
                url_choice = input("\nEnter url of the news article you would like to classify\n(e.g. https://www.bbc.com/news/live/world-52539905):\n> ") or "https://www.huzlers.com/teen-sues-juul-claims-vaping-made-him-homosexual/"
                print(f"url: {url_choice}")
                if(url_choice == ""):
                    print("\nNews article url can't be a blank string!\n")
            label_definitions = {'Journalism': 'Journalism focuses on sharing information. These articles do not attempt to persuade or influence the reader by means other than presentation of facts. Journalistic articles avoid opinionated, sensational or suspect commentary. Good journalism does not draw conclusions for the reader unless manifestly supported by the presented evidence. Journalistic articles can make mistakes, including reporting statements that are later discovered to be false, however the mark of good journalism is responsiveness to new information (via a follow up articles or a retraction) especially if it coutermands previously reported claims.', 'Wiki': 'Like Journalism, the primary purpose of Wiki articles is to inform the reader. Wiki articles do not attempt to persuade or influence reader by means other than presentation of the facts. Wiki articles tend to be pedagogical or encyclopedic in nature, focusing on scientific evidence and known or well studied content, and will highlight when a claim or an interpretation is controversial or under dispute.  Like Journalism, Wiki articles are responsive to new information and will correct or retract prior claims when new evidence is available.', 'Satire': 'Satirical articles are characteristically humorous, leveraging exaggeration, absurdity, or irony often intending to critique or ridicule a target. Claims in works of satire may be intentionally false or misleading, tacitly presupposing the use of exaggeration or absurdity as a rhetorical technique. Satirical articles can often be written in a journalistic voice or style for humorous intent.', 'Sensational': 'Sensational articles provoke public interest or excitement in a given subject matter. Sensational articles tend to leveraging emotionally charged language, imagery, or characterizations to achieve this goal. While sensational articles do not necessarily make false claims, informing the reader is not the primary goal, and the presentation of claims made in sensational articles can often be at the expense of accuracy.', 'Opinion': 'Opinion pieces present the author’s judgments about a particular subject matter that are not necessarily based on facts or evidence. Opinion pieces can be written in a journalistic style (as in “Op-Ed” sections of news publications). Claims made in opinion pieces may not be verifiable by evidence or may draw conclusions that are not materially supported by the available facts. Opinion pieces may or may not be political in nature, but often advocate for a particular position on a controversial topic or polarized debate.', 'Agenda-driven': 'Agenda-driven articles are primarily written with the intent to persuade, influence, or manipulate the reader to adopt certain conclusions. Agenda-driven articles may or may not be malicious in nature, but characteristically do not convince the reader by means of fact based argumentation or a neutral presentation of evidence. Agenda-driven articles tend to be less reliable or more suspect than fact based journalism, and an author of agenda-driven material may be less responsive to making corrections or drawing different conclusions when presented with new information.'}
            label_article(url_choice, label_definitions)
            continue_question = [inquirer.List('action', message = "\n\nWould you like to classify other articles?", choices = ['Yes', 'No'])]
            continue_answer = inquirer.prompt(continue_question)
            chosen_function = continue_answer['action']
            if (chosen_function == 'No'):
                classify_continue = False
                print("Thank you for using Authentikos! Bye now...")
    else:
        print("Thank you for using Authentikos! Bye now...")
