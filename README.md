
## Program Description:
This script checks the Seattle ferry website and sends a text alert if ferry tickets at the selected times/weeks are available.  
It is intended to be scheduled on the crontab to run every 10min or so, and will keep a log of any errors which occur automatically. It will also shut off automatically if a text alert is sent, so that the recipient does not receive text alerts every 10min for an open position.  
 (See **Instructions for Program Use** or **Background Info** sections for more information.)


## Background Info:
My father commutes by ferry every day to and from Seattle. The ferry tickets for the entire month release on the 1st of each month, and are visible on a week by week basis. Since tickets are typically sold out within two minutes, he has a difficult time getting tickets for his commute. Typically he is able to secure only certain weeks' tickets, so the flexibility of this program to be able to check only specified weeks and be easily updated was a core part of the design. This program allows him to get text alerts whenever a set of ferry tickets becomes available -- typically when someone cancels their online reservation.

## Instructions for Program Use:
- First off, for the script to run and send text alerts properly, a Twilio account must be set up, and the appropriate fields for phone number and account information must be filled out in the 'send_sms()' function.
- Run **reset.py** to ensure that the **run_or_not.txt** file contains the correct contents to allow program execution.
- In main(), if you want the program to run headless (ie. without opening a browser) then ensure that the 'headless' value is set to True on line 107. Otherwise if you want the program to open a physical browser so you can see it interact with the webpage, set this value to False.
- In main(), the program will only check the weeks specified on lines 115-119. Set any sections which need to be checked to True, all weeks marked as False will be skipped. Note that the program will begin checking on whichever week of the month it currently is. Additionally, the length of the array is flexible, so if one month only 5 weeks instead of 4, simply put a 5th True/False value in the array. (Example: if it is currently the 2nd week of the month, and I want to check for ferry tickets for all of the remaining weeks except the last one. I can fill the array with [True, False, True, True, False] and it will begin with the current week and check each following week that marked as true.)
- Once these values are set, the program is ready to execute. This can be done from the command line using 'python ferryBot.py' or 'python3 ferryBot.py'



## Program Components: 
- **ferryBot.py** -- Main python script which contains contains all elements of program execution. Running this python script (using either 'python ferryBot.py' or 'python3 ferryBot.py' will execute the program.)  
- **run_or_not.txt** -- Contents will either be 'run\n' or 'don't run\n' indicating the current status of the script. ferryBot.py will check this file before executing, and will only run if this file contains 'run\n'. This is to ensure that the user receiving the text alerts does not receive multiple text alerts for the same position.  
- **reset.py** -- A short script which resets 'run_or_not.txt' back to the 'run\n' state. It is included for user convenience.  
- **error_log.txt** -- Whenever the program executes, the current date/time as well as a brief record of whether or not the program ran successfully is added to 'error_log.txt'. If 'error_log.txt' does not exist when the program executes, then 'ferryBot.py' will generate this text document automatically.  
- **ferryBot.out** -- A file used to store the print statements used in ferryBot.py when running the script from the crontab. It is primarily used for debugging.  
- **a.out** -- A file used by the crontab to run the program automatically.  
- **geckodriver.log** -- This particular file is automatically generated whenever the program executes, and is part of the geckodriver dependency. (See **Required Dependencies** section.)  


## Required Dependencies for Program Execution: 
- python3 installed
- selenium python library
- Twilio python library
- Firefox web browser
- Geckodriver (A firefox driver allowing interaction w/ selenium)  
	(This should typically be installed in /usr/local/bin)



