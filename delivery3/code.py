import re

def exercise1():
    file = open("messages_syslog_class.txt")
    list_lines = file.readlines()
    print(list_lines[0])

if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()