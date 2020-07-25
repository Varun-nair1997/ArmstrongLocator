"""
This program counts the number of armstrong number and generates a data set to be used to model the probability of 
finding an armstrong number.
"""

__Author__ = "Varun Nair"

def armCounter(p):
    """
    Counts number of armstrong numbers with p digits
    :param p: number of digits to search through
    :return: number of p digit armstrong numbers
    """
    stopR = 10**p
    startR = 10**(p-1)
    count = 0
    for i in range(startR, stopR):
        checker = armstrongCheck(i)
        if checker:
            count+=1
    return count


def armstrongCheck(n):
    """
    Checks if a given number is an armstrong number
    :param n: number to check
    :return: 'True' if armstrong 'False' if not
    """
    nStr = str(n)
    armCheck = 0
    for i in nStr:
        armCheck+=(int(i)**(len(nStr)))
    if armCheck == n:
        return True
    if armCheck != n:
        return False


if __name__ == '__main__':
    for i in range(1,20):
        NoOfArms = armCounter(i)
        print(i,' digit numbers: ' ,NoOfArms)

