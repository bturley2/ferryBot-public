INSTRUCTIONS FOR USE:
-- to allow the script to run, 'run_or_not.txt' must contain the string "run"
-- program will overwrite this string with "don't run" if it sends a text
-- resetting 'run_or_not.txt' can be done automatically by executing the
  'reset.py' script
-- idea is to schedule this program to run periodically using the crontab,
  and it must be manually reset once it sends a text. This prevents the
  recipient of the texts from being inundated with texts as soon as a spot
  on the ferry becomes available
-- an error log is kept automatically which stores times at which the program
  ran as well as any issues that it came across.
  This is found in 'error_log.txt'
-- do NOT make this script publicly available without altering it in some way,
  as both the twilio product key and phone number of the recipient are hard-
  coded into the 'ferryBot.py' script


*** REQUIRED DEPENDENCIES FOR PROGRAM EXECUTION***
-- python3 installed
-- selenium python library
-- Twilio python library
-- Firefox web browser
-- Geckodriver (A firefox driver allowing interaction w/ selenium)
	(This must be installed in /usr/local/bin)
