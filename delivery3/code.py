import re

def exercise1():

    """
    Point 1: Compute the ranking of usernames according to number of
    login attempts
    """

    # Create a pattern to find the name of the user

    """
    Example for valid session:
     - Session opened for user root by (uid=0)
    Example of invalid attempt:
     - Invalid user yoyo from 106.52.116.101 port 53873
     - Failed password for invalid user yoyo from 106.52.116.101 port 53873 ssh2
    """
    pattern = re.compile("session opened for user (\w+\d*) by|Invalid user (\w+\d*) from|Failed password for invalid user (\w+\d*) from")

    # Create a dictionary to store the user names and login attempts
    attempts = dict([])
    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # If the user exists we add one to the number of attempts

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] += 1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] += 1
                # Check if the match is for the third component of the pattern (group 3)
                if match.group(3)!='None':
                    attempts[match.group(3)] += 1
            except:
                # If the user doesn't exist we store the new user

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] =  1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] =  1
                # Check if the match is for the third component of the pattern (group 3)
                if match.group(3)!='None':
                    attempts[match.group(3)] =  1

    # We transform the dictionary into a sorted list of tuples
    attempts_sorted=sorted(attempts.items(), key=lambda item: item[1], reverse=True)

    print(attempts_sorted)
    
def exercise2():

    """
    Compute the distribution of attacks and IP addresses. The distribution must be computed in quarters.
    """
    """
    Example for valid session:
     - Accepted password for aftoral from 79.150.140.15 port 57667 ssh2
    Example of invalid attempt:
     - Invalid user yoyo from 106.52.116.101 port 53873
     - Failed password for invalid user yoyo from 106.52.116.101 port 53873 ssh2
    """
    
    # Pattern to find the IP of each attempt
    pattern = re.compile("Invalid user \w* from (\d*.\d*.\d*.\d*) | Failed password for invalid user \w* from (\d*.\d*.\d*.\d*) | Accepted password for \w* from (\d*.\d*.\d*.\d*)")

    # Create a dictionary to store the user names and login attempts
    attempts = dict([])

    # Counter to sum all the login attempts
    count = 0

    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # If the user exists we add one to the number of attempts

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] += 1
                    count += 1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] += 1
                    count += 1
                # Check if the match is for the third component of the pattern (group 3)
                if match.group(3)!='None':
                    attempts[match.group(3)] += 1
                    count += 1

            except:
                # If the user doesn't exist we store the new user

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] =  1
                    count += 1

                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] =  1
                    count += 1

                # Check if the match is for the second component of the pattern (group 2)
                if match.group(3)!='None':
                    attempts[match.group(3)] =  1
                    count += 1

    # all_values = attempts.values()
    # max_value = max(all_values)

    # q1 = max_value/4
    # Calculate the quarters of the login attempts
    q1 = count/4
    print("Quarters: ", q1, q1*2, q1*3, q1*4)

    # Define the number of unics attempts for each quarter
    n_q1 = 0
    n_q2 = 0
    n_q3 = 0
    n_q4 = 0
    
    # Create a loop to extract the number of attempts of each IP
    for attempt in attempts:

        # Check if the IP belongs to the first quarter
        if (attempts[attempt] <= q1):
            # If it belongs to the first quarter add 1
            n_q1 += 1

        # Check if the IP belongs to the second quarter
        if (attempts[attempt] > q1 and attempts[attempt] <= q1*2):

            # If it belongs to the second quarter add 1
            n_q2 += 1

        # Check if the IP belongs to the third quarter
        if attempts[attempt] > q1*2 and attempts[attempt] <= q1*3:
            
            # If it belongs to the third quarter add 1
            n_q3 += 1

        # Check if the IP belongs to the fourth quarter
        if attempts[attempt] > q1*3 and attempts[attempt] <= q1*4:

            # If it belongs to the second fourth add 1
            n_q4 += 1

    # Print the distribution
    distribution = [("0<x<=q1",n_q1), ("q1<x<=q2",n_q2), ("q2<x<=q3",n_q4), ("q3<x<=q4",n_q4)]
    print(distribution)

def exercise3():

    """
    Point 3: Obtain a Ranking of failed login attempts by source IP
    """

    # Create a pattern to find the name of the user and the source IP

    """
    Example of invalid attempt:
     - Invalid user yoyo from 106.52.116.101 port 53873
     - Failed password for invalid user yoyo from 106.52.116.101 port 53873 ssh2
    """

    pattern = re.compile("Invalid user \w* from (\d*.\d*.\d*.\d*) | Failed password for invalid user \w* from (\d*.\d*.\d*.\d*)")

    # Create a dictionary to store the user names and login attempts
    attempts = dict([])

    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # If the user exists we add one to the number of attempts

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] += 1
                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] += 1
            except:
                # If the user doesn't exist we store the new user

                # Check if the match is for the first component of the pattern (group 1)
                if match.group(1)!='None':
                    attempts[match.group(1)] =  1

                # Check if the match is for the second component of the pattern (group 2)
                if match.group(2)!='None':
                    attempts[match.group(2)] =  1


    # We transform the dictionary into a sorted list of tuples
    failed_attempts_sorted=sorted(attempts.items(), key=lambda item: item[1], reverse=True)

    print(failed_attempts_sorted)
    
if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()
    
    # Call method for Exercise 2
    exercise2()


    # Call method for Exercise 3
    exercise3()
