# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Config
login_time = 30                 # Time for login (in seconds)
new_msg_time = 5                # TTime for a new message (in seconds)
send_msg_time = 5               # Time for sending a message (in seconds)
country_code = 91               # Set your country code
action_time = 2                 # Set time for button click action

image_path = '/home/baishali/Filee/whatsapp-bulk-messenger/Image/hello.png'
 # Absolute path to you image
# driver.get("chrome://settings/clearBrowserData");


options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

# Create driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
path = "chromedriver_linux64 (2)/chromedriver"
service = Service(executable_path=path)

driver = webdriver.Chrome(service = service,options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


# Encode Message Text
with open('message.txt', 'r') as file:
    msg = file.read()

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)
        wait = WebDriverWait(driver, 10)
        attach_btn = driver.find_element(By.CSS_SELECTOR, '._1OT67')
        # Click on button to load the input DOM
        attach_btn = driver.find_element(By.CSS_SELECTOR, '._1OT67')
        attach_btn.click()
        time.sleep(action_time)
        # Find and send image path to input
        msg_input = driver.find_element(By.CSS_SELECTOR, '._1CGek input')
        msg_input.send_keys(image_path)
        time.sleep(action_time)
        # Start the action chain to write the message
        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            # SHIFT + ENTER to create next line
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.get("chrome://settings/clearBrowserData");
driver.quit()
