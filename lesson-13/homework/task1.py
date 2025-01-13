import sqlite3

# Database creation
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, Age INTEGER);
    """
    cursor.execute(query)

# Insert data
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    INSERT INTO Roster VALUES('Benjamin Sisko', 'Human', 40);
    INSERT INTO Roster VALUES('Jadzia Dax', 'Trill', 300);
    INSERT INTO Roster VALUES('Kira Nerys', 'Bajoran', 29);
    """
    cursor.executescript(query)

# Update data
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax';
    """
    cursor.execute(query)

# Query data
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    SELECT Name, Age FROM Roster WHERE Species='Bajoran';
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

# Delete data
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    DELETE FROM Roster WHERE Age > 100;
    """
    cursor.execute(query)

# Bonus task
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    ALTER TABLE Roster ADD Rank TEXT;
    UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko';
    UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax';
    UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys';
    """
    cursor.executescript(query)

# Advanced query
with sqlite3.connect("roster.db") as db:
    cursor = db.cursor()
    query = """
    SELECT * FROM Roster ORDER BY Age DESC;
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)