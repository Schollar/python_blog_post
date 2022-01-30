import dbcreds
import mariadb as db


class dbInteraction:

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

    def user_login(username, password):
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
            return False
        else:
            for i in user:
                print(f'Welcome ', i[1])
