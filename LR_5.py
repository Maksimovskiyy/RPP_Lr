import sqlite3
conn = sqlite3.connect('users')
cursor = conn.cursor()
cursor.execute("""create table if not exists users(
id integer primary key,
name text,
email text)""")
conn.commit()

def insert_value(id, name, email):
        conn = sqlite3.connect('users')
        cursor = conn.cursor()
        cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """,
                       {"id": id, "name": name, "email": email})
        conn.commit()

def select_func():
        cursor = conn.cursor()
        cursor.execute("""select * from users""")
        print(cursor.fetchall())

def select_user(id):
        cursor = conn.cursor()
        cursor.execute("""select * from users where id=:id""", {"id": id})
        print(cursor.fetchall())

def select_user2(id, name):
        cursor = conn.cursor()
        cursor.execute("""select * from users where id=:id and name=:name """, {"id": id, "name": name})
        print(cursor.fetchall())

def delete_user(id):
        cursor = conn.cursor()
        cursor.execute("""delete from users where id=:id""", {"id": id})
        print(cursor.fetchall())
        conn.commit()

def main():
        insert_value(1, 'Ибрагим', 'One@mail.ru')
        insert_value(2, 'Святослав', 'Punch@mail.ru')
        insert_value(3, 'Светлана', 'Assassin@mail.ru')
        insert_value(4, 'Святомир', 'Hahaha@mail.ru')
        insert_value(5, 'Никита', 'Nikitos@mail.ru')
        insert_value(7, 'Злата', 'Zlato@mail.ru')
        insert_value(8, 'Алеша', 'Popovich@mail.ru')

        # Поиск всех пользывателей
        select_func()
         #Поиск по id
        select_user(3)
        # Удаление по id
        delete_user(6)
        # Поиск по id и имени
        select_user2(2, 'Святослав')
        select_func()

main()
cursor.execute("drop table users")
conn.close()