#importing spy from spy details
from spy_details import spy, ally

from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored


STATUS_CHOICES = ['Google, i am coming', 'Finally, I am a pythonist']

print 'Let\'s get started'
#concatenate spy name with salutation
user_existence = raw_input('Do you want to continue as' + spy ['salutation'] + ' ' + spy['name'] + '(Y/N)')
#adding and  updating status
def add_status(current_status_msg):

    updated_status_msg = None

    if current_status_msg != None:
        print 'your current message is %s' % current_status_msg
    else:
        print "You do not have any status messages"

    choosing_user = raw_input("Do you want to choose from the per existing statuses? (Y/N)")
#user is choosing an option from list of choices(statuses)
    if choosing_user.upper() == "Y":

        for status in range(0, len(STATUS_CHOICES)):

            print '%s' % (STATUS_CHOICES[status])

        status_select= raw_input('Enter the serial number of status that you want to select')
        if len(status_select) > 0:
            status_select = int(status_select)
            updated_status_msg = STATUS_CHOICES[status_select-1]
#user choosed to enter a new status
    elif choosing_user.upper() == "N":
        new_status = raw_input("please enter your new status")

        if len(new_status) > 0:
            STATUS_CHOICES.append(new_status)
            updated_status_msg = new_status

    else:
        print 'Not valid! Press either y or n.'

    if updated_status_msg:
        print 'Your updated status message is: %s' % updated_status_msg
    else:
        print 'You did not update your status message'

    return updated_status_msg



#method for adding a new ally
def add_ally():

    new_ally = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats': []
    }

    new_ally['name'] = raw_input('please add your friends name')
    new_ally['salutation'] = raw_input('Choose Mr or Ms')
    new_ally['age'] = int(raw_input('Enter the age of your friend'))
    new_ally['rating'] = float(raw_input('Enter the rating of your friend'))

    if len(new_ally['name']) > 0 and new_ally['age'] > 12 and new_ally['rating'] >= spy['rating']:
        ally.append(new_ally)
        print 'Friend Added'

    else:
        print 'Your friend is not good enough.'
    return len(ally)


#method for choosing from existing allies
def choosing_an_ally():

    item_choice = 0

    for fri in ally:
        print '%d. %s' % (item_choice + 1, fri['name'])
        item_choice = item_choice + 1

    ally_selection = raw_input('Choose from your fellow spies')
    if len(ally_selection) > 0:
        ally_selection = int(ally_selection)
        return ally_selection



def send_message():

    ally_choice = choosing_an_ally()
    ally_choice_position = int(ally_choice) - 1

    original_image = raw_input("What is the name of the image?")
    output_path = "eifel.jpg"
    text = raw_input("What do you want to say? ")
    if len(text) > 50:

        del ally[ally_choice_position]
    elif len(text) == 0:
        print 'please enter some text'
    else:
        Steganography.encode(original_image, output_path, text)

        new_chat = {
            "message": text,
            "time": datetime.now(),
            "sent_by_me": True
            }
        ally[ally_choice]['chats'].append(new_chat)

        print "Your secret message image is ready!"

def read_message():

    sender = choosing_an_ally()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    ally[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():

    ally_name = choosing_an_ally()
    for chat in ally[ally_name]['chats']:
        if chat['sent_by_me']:
            print colored("[%s]:", "blue") %(chat['time'].strftime("%d.%B,%Y")), colored ("You said", "red")
            print chat ['message']
        else:
           print colored("[%s]:","blue") %(chat['time'].strftime("%d %B %Y")), \
               colored(ally[ally_name]['name'] +" said" ,"red")
           print chat['message']


def start_chat_app(spy):

    current_status_msg = None

    if spy['age'] > 12 and spy['age'] < 50:

        if spy['rating'] >= 0.0 and spy['rating'] < 2.5:
            print'. Welcome %s %s, age : %d.' \
                  ' You are a noobie' \
                   % (spy['salutation'], spy['name'], spy['age'])
        elif spy['rating'] >= 2.5 and spy['rating'] < 4.0 :
            print'Welcome %s %s, age : %d. ' \
                 'You are an intermediate' \
             % (spy['salutation'], spy['name'], spy['age'])
        elif spy['rating'] >= 4.0:
            print'Welcome %s %s, age : %d. ' \
                 'You are an expert' \
             % (spy['salutation'], spy['name'], spy['age'])

        show_menu = True

        while show_menu:

            menu_options = "What do you want to do?\n" \
                           "1. Add a status update\n" \
                           "2. Add a friend \n" \
                           "3. Send a secret message \n" \
                           "4. Read a secret message\n" \
                           "5. Read Chats from a user \n" \
                           "6. Close Application \n"

            menu_option = raw_input(menu_options)

            if len(menu_option) > 0:
                menu_option = int(menu_option)

                if menu_option == 1:
                    current_status_msg = add_status(current_status_msg)

                elif menu_option == 2:
                    number_of_friends = add_ally()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_option == 3:
                    send_message()
                elif menu_option == 4:
                    read_message()
                elif menu_option == 5:
                    read_chat_history()
                else:
                    show_menu = False
                    print'Enter a valid option'
    else:
       print'Sorry you are not of the correct age to be a spy'


if user_existence.upper() == "Y":
    start_chat_app(spy)
elif user_existence.upper() == "N":
    spy= {
        'name' : '',
        'salutation': '',
        'age' : 0,
        'rating' : 0.0,
        'is_online' : False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

        spy['age'] = raw_input("What is your age?")
        spy['age'] = int(spy['age'])

        spy['rating'] = raw_input("What is your spy rating?")
        spy['rating'] = float(spy['rating'])

        spy['is_online'] = True
        start_chat_app(spy)
    else:
        print 'Please add a valid spy name'
else:
    print 'Not a valid input'