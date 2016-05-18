import sqlite3

def migrate(database_path):
    print "migrating to db version 5"
    conn = sqlite3.connect(database_path)
    conn.text_factory = str
    cursor = conn.cursor()

    # update settings table to include smtp server settings
    cursor.execute('''ALTER TABLE sales ADD COLUMN "unread" INTEGER''')
    cursor.execute('''ALTER TABLE purchases ADD COLUMN "unread" INTEGER''')
    cursor.execute('''ALTER TABLE cases ADD COLUMN "unread" INTEGER''')

    # update version
    cursor.execute('''PRAGMA user_version = 5''')
    conn.commit()
    conn.close()
