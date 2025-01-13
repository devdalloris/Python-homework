import sqlite3
#Database creation
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query="CREATE TABLE IF NOT EXISTS Books(Title text, Author text, Year_Published int, Genre text);"
    cursor.execute(query)
#Insert data
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query = """INSERT INTO Books VALUES
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');
    """
    cursor.executescript(query)
#Update data
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query = "UPDATE Books SET Year_Published=1950 WHERE Year_Published=1984;"
    cursor.execute(query)
#Query data
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query="SELECT Title, Author FROM Books WHERE Genre='Dystopian';"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
#Delete data
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query="DELETE FROM Books WHERE Year_Published<1950;"
    cursor.execute(query)
#Bonus task
with sqlite3.connect("library.db") as db:
    cursor=db.cursor()
    query="""
    ALTER TABLE Books ADD COLUMN Rating int;
    UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird';
    UPDATE Books SET Rating=4.7 WHERE Title='1984';
    UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby';
    """
    cursor.executescript(query)
#Advanced query
with sqlite3.connect("library.db") as db:
    cursor = db.cursor()
    query = """
    SELECT * FROM Books ORDER BY Year_Published ASC;
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
