import csv

username = input("enter username: ")
password = input("enter password: ")

with open("users.csv") as data_file:
    data = csv.reader(data_file)
    users = [row for row in data if len(row) > 0]
    new_user = dict(users)

for user in new_user:
    if username in user and password in new_user[user]:
        print("Found")
        print(f"username = {user}, password= {new_user[user]}")