##This program finds phone numbers and email addresses in a text
#NB: There must be some text compied to your clipboard

import pyperclip
import re

text = str(pyperclip.paste())  #Extracting text from the clipboard

matches = []

phoneNum = re.findall("[-0-9]+.{,14}", text)  #Up to 14 characters of phone number: 233-244870609
email = re.findall("[a-z.0-9]+@[a-z.]+", text, re.IGNORECASE)   #Email regex

#Storing the matched objects in a list for later reference
for eachMail, eachNum in zip(email, phoneNum):
    comb = eachMail+" "+eachNum
    matches.append(comb)
