import math

print(math.pi)            # Output: 3.141592653589793
print(math.sqrt(16))      # Output: 4.0
print(math.sin(math.pi))  # Output: 1.2246467991473532e-16

from math import pi, sqrt

print(pi)          # Output: 3.141592653589793
print(sqrt(16))    # Output: 4.0

import math as m

print(m.pi)            # Output: 3.141592653589793
print(m.sqrt(16))      # Output: 4.0
print(m.sin(m.pi))     # Output: 1.2246467991473532e-16

from math import *

# Example libs
# math: Provides mathematical functions like sin(), cos(), sqrt(), and constants like pi.
# random: Provides functions for generating random numbers and selecting random items from lists.
# datetime: Provides classes for working with dates and times.
# os: Provides a way to interact with the operating system, including functions for navigating file systems, creating and deleting directories, and running system commands.
# json: Provides functions for encoding and decoding JSON data.
# csv: Provides functions for reading and writing CSV files.
# re: Provides regular expression matching functionality.
# urllib: Provides functions for working with URLs.
# sqlite3: Provides a simple way to work with SQLite databases.
# socket: Provides a way to work with network sockets.

# random module examples
import random

print(random.random())    # Output: 0.12345678901234567

print(random.randint(1, 10))    # Output: 5

print(random.randrange(1, 10))    # Output: 5

print(random.choice(["apple", "banana", "cherry"]))    # Output: "banana"

print(random.sample(["apple", "banana", "cherry"], 2))    # Output: ["apple", "cherry"]

# datetime module examples

import datetime

print(datetime.date.today())    # Output: 2019-01-01

print(datetime.timedelta(days=5))    # Output: 5 days, 0:00:00

print(datetime.datetime.now())    # Output: 2019-01-01 00:00:00.000000

# os module examples

import os

print(os.getcwd())    # Output: /home/user

print(os.listdir())    # Output: ["file1.txt", "file2.txt", "file3.txt"]

print(os.path.exists("file1.txt"))    # Output: True

print(os.path.getsize("file1.txt"))    # Output: 1234

print(os.path.abspath("file1.txt"))    # Output: /home/user/file1.txt

# json module examples

import json

# JSON string

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string

parsed_json = json.loads(json_string)

# Print JSON string

print(parsed_json)    # Output: {"name": "John", "age": 30, "city": "New York"}

# Print JSON string

print(json.dumps(parsed_json))    # Output: {"name": "John", "age": 30, "city": "New York"}

# Print JSON string

print(json.dumps(parsed_json, indent=4))    # Output: {

#     "name": "John",

#     "age": 30,

#     "city": "New York"

# }

# Print JSON string

print(json.dumps(parsed_json, indent=4, sort_keys=True))    # Output: {

#     "age": 30,

#     "city": "New York",

#     "name": "John"

# }

# csv module examples

import csv

# CSV file

csv_file = "file.csv"

# Read CSV file

with open(csv_file, "r") as file:

    # Read CSV file

    reader = csv.reader(file)

    # Print CSV file

    for row in reader:

        print(row)

# Output:

# ["name", "age", "city"]

# ["John", "30", "New York"]

# ["Jane", "25", "Boston"]

# ["Bob", "22", "Miami"]

# Write CSV file

with open(csv_file, "w") as file:

    # Write CSV file

    writer = csv.writer(file)

    # Write row to CSV file

    writer.writerow(["name", "age", "city"])

    # Write row to CSV file

    writer.writerow(["John", "30", "New York"])

    # Write row to CSV file

    writer.writerow(["Jane", "25", "Boston"])

    # Write row to CSV file

    writer.writerow(["Bob", "22", "Miami"])

# Output:

# name,age,city

# John,30,New York

# Jane,25,Boston

# Bob,22,Miami

# urllib module examples

import urllib.request

# URL

url = "https://www.google.com"

# Post Data

data = {"name": "John", "age": 30, "city": "New York"}

# Encode data

data = urllib.parse.urlencode(data).encode("utf-8")

# Request

request = urllib.request.Request(url, data)

# Response

response = urllib.request.urlopen(request)

# Read response

html = response.read()

# Print response

print(html)

# sqlite3 module examples

import sqlite3

# Connect to database

connection = sqlite3.connect("database.db")

# Create cursor

cursor = connection.cursor()

# Create table

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT)")

# Insert data

cursor.execute("INSERT INTO users VALUES (1, 'John', 30, 'New York')")

# Update data

cursor.execute("UPDATE users SET age = 26 WHERE name = 'Jane'")

# Select data

cursor.execute("SELECT * FROM users")

# Fetch data

users = cursor.fetchall()

# Delete data

cursor.execute("DELETE FROM users WHERE name = 'Bob'")

# Commit changes

connection.commit()

# Close connection

connection.close()


# socket module examples

import socket

# Create socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server

s.connect(("www.google.com", 80))

# Send data

s.send(b"GET / HTTP/1.1\r

Host: www.google.com\r

\r

")

# Receive data

data = s.recv(1024)

# Close connection

s.close()

# Print data

print(data)

# Output:

# b'HTTP/1.1 200 OK\r

Date: Mon, 01 Jan 2019 00:00:00 GMT\r

Expires: -1\r

Cache-Control: private, max-age=0\r

Content-Type: text/html; charset=ISO-8859-1\r

P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r

Server: gws\r

X-XSS-Protection: 1; mode=block\r

X-Frame-Options: SAMEORIGIN\r

Set-Cookie: 1P_JAR=2019-01-01-00; expires=Wed, 31-Jan-2019 00:00:00 GMT; path=/; domain=.google.com\r

Set-Cookie: NID=123=456; expires=Tue, 31-Dec-2019 00:00:00 GMT; path=/; domain=.google.com; HttpOnly\r

Accept-Ranges: none\r

Vary: Accept-Encoding\r

Connection: close\r

\r




