import dbcreds
import mariadb as db


class dbInteraction:

    def write_post(username):
        content = input('Write your post:')
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"INSERT INTO python_blog.blog_post(username, content) VALUES('{username}', '{content}')")
        conn.commit()
        cursor.close()
        conn.close()

    def show_posts():
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"select *  from blog_post")
        posts = cursor.fetchall()

        cursor.close()
        conn.close()
        for post in posts:
            print(post[0], ':', post[1])

    def user_login():
        username = input("Enter a username: ")
        password = input("Enter your password: ")
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'")
        user = cursor.fetchall()
        cursor.close()
        conn.close()
        if(user == []):
            print("Invalid username or password!")
        else:
            for i in user:
                print(f'Welcome ', i[1])


username = 'foo'
