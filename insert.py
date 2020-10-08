import sqlite3
conn = sqlite3.connect('image.db')
cursor = conn.cursor()


def convert_pic():
    filename ='sun.jpg'
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo

if __name__ == "__main__":
    id = 23
    name = 'nawshin'
    photo = convert_pic()
    cursor.execute(" INSERT INTO new_employee (id, name, photo) VALUES (? ,?, ?)",(id, name, photo))
    conn.commit()
    cursor.close()
    conn.close()
