import re
from datetime import datetime

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

    print("Exercise 1")
    print()
    print(attempts_sorted)
    print()

    
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

    # count to sum all the login attempts
    count = 0

    # Define the number of unics attempts for each quarter
    n_q1 = 0
    n_q2 = 0
    n_q3 = 0
    n_q4 = 0

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

 
    print()
    print("Exercise 2")
    print()

    # Calculate the quarters of the login attempts
    q1 = count/4
    print("Quarters: ", q1, q1*2, q1*3, q1*4)

    count = 0
    attempts = dict([])

    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # When the limit of the first quartile is passed, the dictionary is cleaned to store new unique IPs again
                if (count == q1):
                    attempts = dict([])
                # When the limit of the second quartile is passed, the dictionary is cleaned to store new unique IPs again
                if (count == q1*2):
                    attempts = dict([])
                # When the limit of the third quartile is passed, the dictionary is cleaned to store new unique IPs again
                if (count == q1*3):
                    attempts = dict([])
                
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

                # The count of unique IPs in the first quantile is increased if the count is in the first quartile
                if (count <= q1):
                    n_q1 += 1

                # The count of unique IPs in the second quantile is increased if the count is in the second quartile
                if (q1 < count <= 2*q1):
                    n_q2 += 1

                # The count of unique IPs in the third quantile is increased if the count is in the third quartile
                if (2*q1 < count <= 3*q1):
                    n_q3 += 1

                # The count of unique IPs in the fourth quantile is increased if the count is in the fourth quartile
                if (3*q1 < count <= count):
                    n_q4 += 1


    # Print the distribution
    distribution = [("0 < x <= q1",n_q1), (" q1 < x <= q2",n_q2), ("q2 < x <= q3",n_q4), ("q3 < x <= q4",n_q4)]
    print(distribution)
    print()

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

    print("Exercise 3")
    print()
    print(failed_attempts_sorted)
    print()


def exercise4():

    """
    Point 4: Compute the reverse ranking of average period between
    login attempts (seconds)
    """

    # Create a pattern to find the IP of the user 

    """
    Example for valid session:
     - Accepted password for aftoral from 79.150.140.15 port 57667 ssh2
    Example of invalid attempts with date
    - Dec 15 06:26:55 crowds-ml sshd[19538]: Invalid user slottan from 106.12.118.30 port 42486
    - Dec 15 06:25:05 crowds-ml sshd [19321]: Failed password for invalid user yoyo from 106.52.116.101 port 53873 ssh2
    """

    pattern = re.compile("\w{2,} \d{2} (\d{2}:\d{2}:\d{2}) crowds-ml sshd\W\d{5}\W: Invalid user \w* from (\d*.\d*.\d*.\d*)|\w{2,} \d{2} (\d{2}:\d{2}:\d{2}) crowds-ml sshd\W\d{5}\W: Failed password for invalid user \w* from (\d*.\d*.\d*.\d*)|\w{2,} \d{2} (\d{2}:\d{2}:\d{2}) crowds-ml sshd\W\d{5}\W: Accepted password for \w* from (\d*.\d*.\d*.\d*)")

    
    # Create a dictionary to store the IPs and times
    times = dict([])

    for line in open("messages_syslog_class.txt"):
        for match in re.finditer(pattern, line):
            try:
                # If the IP exits in the dictionary:

                # Check if the match is for the first component of the pattern, where the group 1 
                # is the time and the group 2 is the IP source
                if (match.group(1) is not None) and (match.group(2) is not None):

                    # First we take the time of the previous attemp for this IP that is 
                    # stored in the third position of the dictionary
                    a = datetime.strptime(times[match.group(2)][2], '%H:%M:%S')
                    # The second time is the time of the actual log found with the pattern
                    b = datetime.strptime(match.group(1), '%H:%M:%S')

                    # Calculate the difference in seconds between the actual attemp and the previous one
                    dif = (b-a).total_seconds()

                    # Store the difference of the time between attempts in the first position of the list
                    times[match.group(2)][0] +=  dif
                    # Add one to the counter of the second position of the list
                    times[match.group(2)][1] +=  1
                    # Store the time of this attemp in the third position of the list
                    times[match.group(2)][2] =  match.group(1)

                # Check if the match is for the second component of the pattern, where the group 3 
                # is the time and the group 4 is the IP source
                if (match.group(3) is not None) and (match.group(4) is not None):
                    
                    # First we take the time of the previous attemp for this IP that is 
                    # stored in the third position of the dictionary
                    a = datetime.strptime(times[match.group(4)][2], '%H:%M:%S')
                    # The second time is the time of the actual log found with the pattern
                    b = datetime.strptime(match.group(3), '%H:%M:%S')

                    # Calculate the difference in seconds between the actual attemp and the previous one
                    dif = (b-a).total_seconds()

                    # Store the difference of the time between attempts in the first position of the list
                    times[match.group(4)][0] +=  dif
                    # Add one to the counter of the second position of the list
                    times[match.group(4)][1] +=  1
                    times[match.group(4)][2] =  match.group(3)
                
                # Check if the match is for the second component of the pattern, where the group 5 
                # is the time and the group 6 is the IP source
                if (match.group(5) is not None) and (match.group(6) is not None):
                    # First we take the time of the previous attemp for this IP that is 
                    # stored in the third position of the dictionary
                    a = datetime.strptime(times[match.group(6)][2], '%H:%M:%S')
                    # The second time is the time of the actual log found with the pattern
                    b = datetime.strptime(match.group(5), '%H:%M:%S')

                    # Calculate the difference in seconds between the actual attemp and the previous one
                    dif = (b-a).total_seconds()

                    # Store the difference of the time between attempts in the first position of the list
                    times[match.group(6)][0] +=  dif
                    # Add one to the counter of the second position of the list
                    times[match.group(6)][1] +=  1
                    # Store the time of this attemp in the third position of the list
                    times[match.group(6)][2] =  match.group(5)

            except:
                # If the IP does't exists in the dictionary because is the first time it tries to loggin:


                # Check if the match is for the first component of the pattern, where the group 1 
                # is the time and the group 2 is the IP source
                if (match.group(1) is not None) and (match.group(2) is not None):
                    # We store the IP in the dictionary with a value of a list, where the first component
                    # of the list is the sum of differences between attempts, the second one is the number 
                    # of attempts and the third one is the time of attempt of the last time (Group 1)
                    times[match.group(2)] =  [0, 1, match.group(1)]

                # Check if the match is for the second component of the pattern, where the group 3 
                # is the time and the group 4 is the IP source
                if (match.group(3) is not None) and (match.group(4) is not None):
                    # We store the IP in the dictionary with a value of a list, where the first component
                    # of the list is the sum of differences between attempts, the second one is the number 
                    # of attempts and the third one is the time of attempt of the last time (Group 3)
                    times[match.group(4)] =  [0, 1, match.group(3)]

                # Check if the match is for the second component of the pattern, where the group 5 
                # is the time and the group 6 is the IP source
                if (match.group(5) is not None) and (match.group(6) is not None):
                    # We store the IP in the dictionary with a value of a list, where the first component
                    # of the list is the sum of differences between attempts, the second one is the number 
                    # of attempts and the third one is the time of attempt of the last time (Group 5)
                    times[match.group(6)] =  [0, 1, match.group(5)]
    # Create a new dictionary to store the average
    tuples = dict([])
    # Create a loop to calculate the average for each element
    for i in times:
        # the mean is the division between the total sum of the time between attempts (first position)
        # and the total number of attempts for that IP (second position)
        avg = round(times[i][0]/times[i][1], 2)
        tuples[i] = avg

    # We transform the dictionary into a sorted list of tuples
    times_sorted=sorted(tuples.items(), key=lambda item: item[1])

    print("Exercise 4")
    print()
    print(times_sorted)

    
if __name__ == '__main__':

    # Call method for Exercise 1
    exercise1()
    
    # Call method for Exercise 2
    exercise2()

    # Call method for Exercise 3
    exercise3()

    # Call method for Exercise 4
    exercise4()
