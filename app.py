import requests
from termcolor import colored

print("Welcome to the Value Changer and Viewer app for the client counter api, this app will allow you to change the value of clients and view it. \nMy Goal for this project is for buisness to be able to show how many clients when they dont have automatic updates, this program is a sort of a work around for that issue")
print("\n")
print(colored("This program was created By Indigo on Github 'https://github.com/IndigoCoke390' If anyone is distributing or selling this program immediatly request a refund, this is a free program!", 'red'))

print("\n")

print("What would you like to do?")
print(colored("Change Value of Clients (1)" , 'blue'))
print(colored("View Value of Clients (2)" , 'blue'))

what_user_wants_to_do = int(input("type here: "))

if what_user_wants_to_do == 1:
    print("you would like to change the value of clients!")

    new_value = int(input("What do you want to set the new number as? : "))
    password = input("What is the password you have set? : ")
    url = input("What is the url to your api? : ")

    url_full = "http://" + url + "/clients/update"

    # Send the request to update the clients value
    response = requests.post(url_full, json={"password_entr": password, "new_value": new_value})

    # Print the response from the server
    print(response.json())

    print(colored("Success!", "green"))

    print(colored("Exiting program", "red"))

elif what_user_wants_to_do == 2:
    print("you would like to view the value of clients!")

    url_2 = input("What is the url to your api? : ")

    url_full_2 = url_full = "http://" + url_2 + "/clients/view"

    # Send the GET request
    response = requests.get(url_full_2)

    # Print the response from the server
    print(response.json())

    print(colored("Success!", "green"))

    print(colored("Exiting program", "red"))

else:
    print(colored("Error, please enter either the number '1' or '2'", 'green'))
    
    print(colored("Exiting program", "red"))