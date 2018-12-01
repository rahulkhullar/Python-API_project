Steps followed in the python script are as follows:
Requirements
requests==2.20.1 module is required for running this script and used python 3.6

Step1: Created a python script and define functions for each case.

Step2: I have used random, deque and string in-built function in function generate_password() to generate
random password as per the scenario given in the problem.

Step3: I have used regular expression library in python to match the string in function check_password_level()
 to determine the complexity level for the password generated in the 'generate_password()' function.

Step4: I have used assert function in 'test_check_password_level()' to return True or False based on
complexity_level which is determined by function 'check_password_level()'.

Step5: In this, I have used 'SQLite3' and 'requests' libraries and created a function 'create_user()'
which establishes the SQlite connection and calls the 'retrieve_user()' function which returns the full_name
and email_id of a random user from the given api of users and finally insert record in SQlite database file.

Steps6: In this, I have created a separate function 'main()' which retrieves 10 users using the Step5 method
'create_user()'. Once 10 users are created, for each one it creates a new password using the 'user_password()'
function with random length (between 6 and 12) and random complexity level and finally calls the function
'update_db_user()' which updates the password into the SQLite database associated with the correspondent user.
'show_data()' will display the required records.


