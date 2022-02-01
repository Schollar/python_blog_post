import dbhandler as dbh
from colorama import init, Fore, Back, Style
# Printing welcome message, taking in username and password inputs from user and saving to a variable
print('Welcome to the Blog Site')
print('Please login to continue')
username = input("Enter a username: ")
password = input("Enter your password: ")
db = dbh.dbInteraction()
# Initilize colorama to make our program pretty!
init(autoreset=True)
# If our user login function returns false, we exit the program, else the user has logged in and we run the loop.
if(db.user_login(username, password) == False):
    exit()
else:
    # Infinite loop that runs once user is logged in, user can make a selection and based on user selection a function gets
    # called from the dbhandler module
    # One exception is there to catch if the user presses ctrl + c to exit by habit, it will do the thing and exit
    # Other check is done with our if statement, if input is not number 1 or 2 it will print the last else statement
    while(True):
        try:
            print('Please select an option: ')
            print(Fore.RED + '1. Write a new post')
            print(Fore.GREEN + '2. See all posts')
            print('Type', Fore.RED + "exit", 'to exit the app')
            selection = input("Select an option: ")
            if(selection == 'exit'):
                print('Thank you come again!')
                exit()
            elif(float(selection) == 1):
                db.write_post(username)
            elif(float(selection) == 2):
                db.show_posts()
            else:
                print('You must select a valid option')
        except KeyboardInterrupt:
            print('You have quit the app!')
            exit()
