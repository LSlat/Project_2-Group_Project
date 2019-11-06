import sqlite3
import csv
import codecs
import pandas as pd
import numpy as np

conn = sqlite3.connect("names_data.sqlite")

cur = conn.cursor()


cur.execute("CREATE TABLE femalenames(ID VARCHAR PRIMARY KEY, Name VARCHAR, Year NUMERIC, Gender VARCHAR, Count NUMERIC, Rank NUMERIC)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Female_Names.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:

    myData = [row[0], row[3], row[4], row[5], row[6], row[7]]
    cur.execute("INSERT INTO femalenames (ID, Name, Year, Gender, Count, Rank) VALUES (?, ?, ?, ?, ?, ?);", myData)
conn.commit()

cur.execute("CREATE TABLE malenames(ID VARCHAR PRIMARY KEY, Name VARCHAR, Year NUMERIC, Gender VARCHAR, Count NUMERIC, Rank NUMERIC)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Male_Names.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:
    if row[0] == str():
        pass
    else:
        myData = [row[0], row[3], row[4], row[5], row[6], row[7]]
        cur.execute("INSERT INTO malenames (ID, Name, Year, Gender, Count, Rank) VALUES (?, ?, ?, ?, ?, ?);", myData)
conn.commit()

cur.execute("CREATE TABLE movies(ID INT PRIMARY KEY, Characters VARCHAR, Actors VARCHAR, Director VARCHAR, Genre VARCHAR, Metascore INT, Poster VARCHAR, Title VARCHAR, Writer VARCHAR, Year INT, imdbID VARCHAR, imdbRating INT, imdbVotes INT)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Movies.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:

    myData = [row[0], row[14], row[1], row[3], row[4], row[5], row[6], row[8], row[9], row[10], row[11], row[12], row[13]]
    cur.execute("INSERT INTO movies (ID, Characters, Actors, Director, Genre, Metascore, Poster, Title, Writer, Year, imdbID, imdbRating, imdbVotes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", myData)
conn.commit()

conn.close()