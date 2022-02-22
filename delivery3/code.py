import re

def exercise1():

    pattern = re.compile("Hello")

    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            print(line)

if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()