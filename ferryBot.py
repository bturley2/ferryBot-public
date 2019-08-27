# ******************************************************************************
# *** REQUIRED DEPENDENCIES ***
# -- selenium python library
# -- Twilio python library
# -- Firefox web browser
# -- Geckodriver (allows interaction between selenium/firefox)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from twilio.rest import Client
from calendar import monthrange
import time
import datetime

# ******************************************************************************
# *** FUNCTION DEFINITIONS ***

# select next week
def select_next_week(driver):
    time.sleep(0.3)
    elem = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[3]/div')
    elem.click()

# checks if the list of available options contains 8:00am
def check_available_times(driver, file, ferry_time = '8:00 am'):
    time.sleep(0.3)
    item_list = []
    item_list = driver.find_elements_by_class_name('item-header')

    print("This week's available times: ")

    for item in item_list:
        print(item.text)
        if (str(item.text) == ferry_time):
            print('Found ' + ferry_time + '!')
            file.write('Located an available slot at ' + ferry_time + '! Sending automated message.')
            return True

# sends a sms to the specified phone number
def send_sms(message_text):
    account_sid = 'AC019bcf8e8c79af5f60533a93e3a602f1'
    auth_token = '3c96ad11e6c8572f8ff8a1be2ff59e4c'
    client = Client(account_sid, auth_token)

    client.messages \
                    .create(
                         body= message_text,
                         from_='+12537991173',
                         to='+12533151770'
                     )

# uses calendar to figure out how many weeks are left in the month
# and clicks the 'next week' button however many times are necessary
def num_weeks_left(driver):
    todays_date = int(time.strftime('%d'))
    current_year = int(time.strftime('%Y'))
    current_month = int(time.strftime('%m'))
    days_in_this_month = monthrange(current_year, current_month)[-1]

    while todays_date <= days_in_this_month:
        select_next_week(driver)
        todays_date += 7


# ******************************************************************************
# *** MAIN CONTROL FUNCTION ***

def main():
    # decide whether to run headless browser or not. 
    # 'successful' is used to determine whether or not to disable this script
    headless = True     #default is True
    successful = False  #default is False


    # append to error_log.txt file and print current time of this script running
    file = open('error_log.txt', 'a')
    file.write('\n\n' + str(datetime.datetime.now()) + '\n')


    # Create the Firefox() browser
    options = Options()

    # make the Firefox browser headless
    if headless:
        options.headless = True

    driver = webdriver.Firefox(options = options)

    if not headless:
        driver.maximize_window()

    try:

        # ******************************************************************
        # *** CHECKING MORNINGS ***

        print('** Checking Morning Times: **')

        driver.get("http://www.kitsaptransit.com/fast-ferry-reservations")

        # pause to allow loading of initial page
        time.sleep(1)

        # switch to desired frame to interact w/ page elements
        driver.switch_to.frame("iFrameWebEngine")

        # choose morning ferry (Bremerton -> Seattle)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[1]")
        elem.click()


        # choose 1 adult passenger
        elem = driver.find_element_by_xpath('//*[@id="ember601"]')
        elem.clear()
        elem.send_keys("1")

        # click "choose times"
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div[9]")
        elem.click()

        # iterate through the weeks remaining until we are in the next month
        num_weeks_left(driver)


        # 1st week
        if check_available_times(driver, file):
            send_sms("1st Week of September is available at 8:00 am!")
            successful = True

        # 2nd week
        select_next_week(driver)
        if check_available_times(driver, file):
            send_sms("2nd Week of September is available at 8:00 am!")
            successful = True

        # 3rd week
        select_next_week(driver)
        if check_available_times(driver, file):
            send_sms("3rd Week of September is available at 8:00 am!")
            successful = True

        # 4th week
        select_next_week(driver)
        if check_available_times(driver, file):
            send_sms("4th Week of September is available at 8:00 am!")
            successful = True

        file.write('Morning times successfully checked.\n')
        



        # ******************************************************************
        # *** CHECKING AFTERNOONS ***

        print('\n** Checking Afternoon Times: **')

        driver.get("http://www.kitsaptransit.com/fast-ferry-reservations")
        driver.set_window_size(1440, 900)

        # pause to allow loading of initial page
        time.sleep(1)

        # switch to desired frame to interact w/ page elements
        driver.switch_to.frame("iFrameWebEngine")


        # choose afternoon ferry (Seattle -> Bremerton)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div/div[2]/div") 
        elem.click()

        # choose 1 adult passenger
        elem = driver.find_element_by_xpath('//*[@id="ember601"]')
        elem.clear()
        elem.send_keys("1")

        # click "choose times"
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div[9]")
        elem.click()

        # iterate through the weeks remaining until we are in the next month
        num_weeks_left(driver)

        # 1st week
        if check_available_times(driver, file, '5:10 pm'):
            send_sms("1st Week of September is available at 5:10 pm!")
            successful = True

        # 2nd week
        select_next_week(driver)
        if check_available_times(driver, file, '5:10 pm'):
            send_sms("2nd Week of September is available at 5:10 pm!")
            successful = True

        # 3rd week
        select_next_week(driver)
        if check_available_times(driver, file, '5:10 pm'):
            send_sms("3rd Week of September is available at 5:10 pm!")
            successful = True

        # 4th week
        select_next_week(driver)
        if check_available_times(driver, file, '5:10 pm'):
            send_sms("4th Week of September is available at 5:10 pm!")
            successful = True

        file.write('Afternoon times successfully checked.\n')
        
    except:
        file.write('An error occurred. Closing browser instance.\n')
        print('An error occurred. Closing browser instance.')



    # pause before closing -- for use in debugging
    if not headless:
        input()

    
    file.close()
    driver.quit()

    # return whether or not the program should repeat
    return successful

# ******************************************************************************
# *** PROGRAM EXECUTION ***

# read in whether or not to execute the script
infile = open('run_or_not.txt', 'r')
instruction = infile.read()
infile.close()

# execute code if instructed in run_or_not.txt
# if main is successful disable the script 
# by overwriting instruction with 'no'
if instruction == 'run\n' or instruction == 'run':
    print('***RUNNING SCRIPT***')
    if main():
        outfile = open('run_or_not.txt', 'w')
        outfile.write("don't run")
        outfile.close()
else:
    print("Skipping script execution as per 'run_or_not.txt' instruction.")

    file = open('error_log.txt', 'a')
    file.write('\n\n' + str(datetime.datetime.now()) + '\n')
    file.write("Skipping script execution as per 'run_or_not.txt' instruction.")
    file.close()
