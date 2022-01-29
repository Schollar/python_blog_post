import dbcreds
import dbhandler as dbh

print('Welcome to the Blog Site')
print('Please login to continue')
dbh.dbInteraction.user_login()
print('Welcome', {dbh.dbInteraction.username},
      ' please select an option: ')

# while True:
#     try:
#         print('1. Write a new post')
#         print('2. See all posts')
#         print('Type "exit" to exit the app')
#         selection = input("Select an option: ")
#         if(selection == 'exit'):
#             print('Thank you come again!')
#             exit()
#         elif(float(selection) == 1):
#             dbh.dbInteraction.write_post(username)
#         elif(float(selection) == 2):
#             dbh.dbInteraction.show_posts()
#         else:
#             print('You must select a valid option')
#     except KeyboardInterrupt:
#         print('You have quit the app!')
#         exit()
