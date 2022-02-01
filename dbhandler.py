import dbcreds
import mariadb as db


class dbInteraction:
    # Function That takes in a user post input saves it to a variable
    # Then we make a connection to the database, create a cursor
    # Execute an insert SQL query to insert the post content and user's username into the DB. Username was passed to function as argument
    # Commit our changes to the DB, close the cursor and then close the connection
    def write_post(username):
        content = input('Write your post:')
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(
            f"select id from users where username = '{username}'")
        user = cursor.fetchone()
        cursor.execute(
            f"INSERT INTO python_blog.blog_post(content, user_id) VALUES('{content}', '{user[0]}')")
        conn.commit()
        cursor.close()
        conn.close()
# Function that creates DB connection, creates cursor, runs a select SQL query to select all blog posts and
# usernames attached to post from our DB, fetch all the posts, close our cursor and DB connection, and then
# loop through the posts we saved to a variable from the SQL query and display the username and content using print

    def show_posts():
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"select content, users.username  from blog_post inner join users on users.id = blog_post.user_id")
        posts = cursor.fetchall()

        cursor.close()
        conn.close()
        for post in posts:
            print(post[1], ':', post[0])
# Function that takes in the username and password, creates connection to DB, creates cursor and runs a
# select query to grab username and password where the username and password matches that of the arguments given
# Check to see if our user variable is empty from select query, if it is we return false since no username and password from the DB matched
# If user varable is not empty we got a match from the DB and print a welcome message

    def user_login(username, password):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'")
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if(user == None):
            print("Invalid username or password!")
            return False
        else:
            print(f'Welcome ', user[1])
