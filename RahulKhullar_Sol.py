#!/usr/bin/env python

import string
import random
import re
import sqlite3
import requests
from collections import deque


# get next char format
def get_next_char(char_queue):
    next = char_queue.popleft()
    char_queue.append(next)
    return next


# Returns the password depending on the complexity level
def generate_password(length, complexity):
    char_queue = deque()
    if complexity >= 1:
        char_queue.append(string.ascii_lowercase)
    if complexity >= 2:
        char_queue.append(string.digits)
    if complexity >= 3:
        char_queue.append(string.ascii_uppercase)
    if complexity >= 4:
        char_queue.append(string.punctuation)
    password = ''
    for i in range(0, length):
        password += random.choice(get_next_char(char_queue))
    return password


# Returns the complexity level for each password
def check_password_level(password):
    complexity_level = 0
    pattern1 = re.compile('[a-z]+')
    pattern2 = re.compile('[0-9]+')
    pattern3 = re.compile('[A-Z]+')
    pattern4 = re.compile('[!"#$%&\'()*+,-./:;<=>?^_`{|}~]+')

    if pattern1.search(password):
        complexity_level = 1
    if complexity_level == 1 and pattern2.search(password):
        complexity_level = 2
    if complexity_level == 1 and pattern2.search(password):
        complexity_level = 2
    if complexity_level == 2 and pattern3.search(password):
        complexity_level = 3
    if complexity_level == 3 and pattern4.search(password):
        complexity_level = 4
    if complexity_level == 1 and len(password) >= 8:
        complexity_level = 2
    elif complexity_level == 2 and len(password) >= 8:
        complexity_level = 3
    return complexity_level


# Checks using the assertion function the password level and return True or False
def test_check_password_level():
    password_1 = generate_password(4,1)
    complexity_level = check_password_level(password_1)
    assert complexity_level == 1, "Failed, Actual Complexity is not equal to the expected value of 1"

    password_2 = generate_password(4, 2)
    complexity_level = check_password_level(password_2)
    assert complexity_level == 2, "Failed, Actual Complexity is not equal to the expected value of 2"

    password_3 = generate_password(4, 3)
    complexity_level = check_password_level(password_3)
    assert complexity_level == 3, "Failed, Actual Complexity is not equal to the expected value of 3"

    password_4 = generate_password(4, 4)
    complexity_level = check_password_level(password_4)
    assert complexity_level == 4, "Failed, Actual Complexity is not equal to the expected value of 4"


# Retrieves a random user details from API, returns full name and email address
def retrieve_user():
    url = 'https://randomuser.me/api/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    # print(response_json)
    title = response_json["results"][0]["name"]["title"]
    first_name = response_json["results"][0]["name"]["first"]
    last_name = response_json["results"][0]["name"]["last"]
    full_name = "%s %s %s" % (title, first_name, last_name)
    email_id = response_json["results"][0]["email"]
    return full_name, email_id


# Create table, gets values to be inserted for name and email from table_insert_value, finally inserts it
def create_user(db_path):
    conn = sqlite3.connect(db_path)  # new_user4.db
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS USERS7 (full_name TEXT, email TEXT PRIMARY KEY, password TEXT);')
    table_insert_response = retrieve_user()
    user_name = table_insert_response[0]
    email_id = table_insert_response[1]
    c.execute('INSERT INTO USERS7(full_name,email) VALUES(?,?)', (user_name, email_id))
    conn.commit()
    conn.close()


# Update database users with password
def update_db_users(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM USERS7;')
    email_add_list =[]
    for row in cursor:
        email_add_list.append(row[1])
    conn.close()
    for email in email_add_list:
        # print("Email: ", email)
        update_user_password(db_path, email)


# Generates user password
def user_password():
    complexity = random.randint(1, 4)
    # print("Complexity :", complexity)
    password_length = random.randint(6, 12)
    # print("Password Length :", password_length)
    generated_password = generate_password(password_length, complexity)
    return generated_password


# Updates password for user using email in where clause
def update_user_password(db_path, user_email):
    conn = sqlite3.connect(db_path)  # 'new_user4.db'
    c = conn.cursor()
    pwd = user_password()
    c.execute('UPDATE USERS7 SET password = ? WHERE email = ?', (pwd, user_email))
    conn.commit()
    conn.close()


# Retrieve table rows
def show_data(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM USERS7;')
    for row in cursor:
        print(row[0], row[1], row[2])
    conn.close()


# Main method that test complexity test cases, create users in DB and then update
def main():
    # test_check_password_level()
    database_path = "new_user4.db"
    # Step 6, use method created in step 5 which is create_user
    for i in range(0, 10):
        create_user(database_path)
    '''
    Once 10 users are created, for each one: create a new password using the password
    generator function with random length (between 6 and 12) and random complexity level;
    persist this password into the SQLite database associated with the correspondent user
    using email as primary key.
    '''
    update_db_users(database_path)
    show_data(database_path)


main()
