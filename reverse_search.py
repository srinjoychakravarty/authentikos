from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def yandex_gen(img_to_upload):
    '''Uses Yandex Computer Vision to Reverse Search and Correlate Images'''
    CHROME_PATH = '/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH, chrome_options = chrome_options)
    driver.get("https://yandex.com/images")
    # generic2 = driver.find_element_by_xpath("//div[contains(@class, 'input__button')]");
    generic3 = driver.find_element_by_xpath("//div[contains(@class, 'input__button')]/button[contains(@class, 'button2_theme_clear')]");
    # print(generic.get_attribute('innerHTML'))
    generic3.click();
    input_button = driver.find_element_by_xpath("//input[contains(@class, 'cbir-panel__file-input')]");
    full_directory = os.getcwd() + '/' + img_to_upload
    print(full_directory)
    input_button.send_keys(full_directory);
    driver.implicitly_wait(3); # seconds
    tags = driver.find_element_by_xpath("//div[contains(@class, 'Tags_type_simple')]");
    attribution_array = tags.text.splitlines()
    translated_tags = []
    translator = Translator()
    for attr_tag in attribution_array:
        translated_tags.append(translator.translate(attr_tag).text)
    return (translated_tags)

if __name__ == '__main__':
    img_to_upload = 'rem.jpg'
    translated_tags = yandex_gen(img_to_upload)
    print(translated_tags)
