# Prankr
# version 0.0.2
#
# Use twilio to create and send prank sms and voice calls
# no with Python 3.

# import prank Class templates
from Templates import *
import Templates

# import list of pranks
from PranksList import *
import PranksList

# get users choice to send or save new prank
def user_start(prank_list):

    print("1: get list of pranks\n2: create a new prank")
    user_choice = raw_input("1 or 2: ")

    if user_choice == "1":
        send_prank_sms(prank_list)

    if user_choice == "2":
        create_new_prank()

    if user_choice != "1" and user_choice != "2":
        print("please try again with 1 or 2")

# function for sending the prank, called if user inputs 1
def send_prank_sms(prank_list):

    print(prank_list)

    text_body = input("choose a text to send, typing the exact name in quotes: ")
    number_to_send_to = input("what are the ten digits for the mobile number? ")

    if text_body not in prank_list:
        print("error: use correct name")

    for i in PranksList.pranks:
        if i.title == text_body:
            print("working..")
            i.send_sms(number_to_send_to)
            print("message sent. mwuaahahaha.")

    user_start(prank_list)

# function for creating new prank, called if user inputs 2
def create_new_prank():

    user_title = input("Name prank title without spaces, in quotes: ")
    user_body = input("What should the body of the prank be? ")

    if " " in user_title:
        print("don't use spaces")
        return

    # open prank python file that has templates
    prank_templates_read = open('templates.py', 'r')
    # save text of python templates file in variable
    prank_templates_save = prank_templates_read.read()

    # open prank python files again, but this time for writing
    new_prank_templates = open('templates.py', 'w')
    # create new file using old file text + new prank
    new_prank_templates.write(prank_templates_save+user_title+" = Base.Sms(" + "'"+ user_title + "'" +","+"'"+user_body+"'"+")\n\n")

    # same as above, but this updates the PranksList.py file
    prank_list = open("PranksList.py", "r")
    prank_list_read = prank_list.read()
    prank_list_save = open("PranksList.py", "w")
    prank_list_save.write(prank_list_read[0:len(prank_list_read)-2] + ', ' + user_title + "]")

    # confirm user has saved new prank
    print "New prank " + user_title + " saved."

    # TODO restart with new prank added
    # user_start()

# create list of pranks
pranks = []
for i in PranksList.pranks:
    print(i.title)
    pranks.append(i.title)

# initiate pranks
user_start(pranks)
