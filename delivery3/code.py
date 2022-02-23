import re

def exercise1():

    """
    Point 1: Compute the ranking of usernames according to number of
    login attempts
    
    """

    # Create a pattern to find the name of the user

    """
    Example for valid session:
     - Check if the match is for the first component of the pattern (group 1)
    Example of invalid attempt:
     - Invalid user yoyo from 106.52.116.101 port 53873
     - Failed password for invalid user yoyo from 106.52.116.101 port 53873 ssh2

    """
    pattern = re.compile("session opened for user (\w+\d*) by|Invalid user (\w+\d*) from|Failed password for invalid user (\w+\d*) from")
    # Create a dictionary to find easier the name of the users
    attempts = dict([])
    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # If the user exits we plus one to the number of attemps

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1) is not 'None':
                    attempts[match.group(1)] += 1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2) is not 'None':
                    attempts[match.group(2)] += 1
                # Check if the match is for the third component of the pattern (group 3)
                if match.group(3) is not 'None':
                    attempts[match.group(3)] += 1
            except:
                # If the user doesn't exits we stored the new user

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1) is not 'None':
                    attempts[match.group(1)] =  1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2) is not 'None':
                    attempts[match.group(2)] =  1
                # Check if the match is for the third component of the pattern (group 3)
                if match.group(3) is not 'None':
                    attempts[match.group(3)] =  1

    # We transform the dictionary into a sorted list of tuples
    attempts_sorted=sorted(attempts.items(), key=lambda item: item[1], reverse=True)

    print(attempts_sorted)
    
if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()