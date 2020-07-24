import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from math import *

def poissonPreProcess(intervalLen, start):
    """
    sets up the random variable and support for the PMF
    :param intervalLen: length of the interval
    :param start: start point for the graph
    :return: returns xAxis for plot
    """
    span = np.arange(start,start+intervalLen+1)
    return span


def poissonDist(avg, k):
    """
    Calculates poisson distribution PMF for a random variable with avg parameter
    :param avg: lambda paramter for possion
    :param k: random variable number
    :return: pmf
    """
    PMF = ((avg**k)*(np.exp(-1*avg))/(factorial(k)))
    return(PMF)


def pmfPlotter(pmf, timeLine):
    """
    creates plots of the poisson PMF
    :param pmf: array of PMF values
    :param timeLine: xAxis and support
    :return: plotten poisson PMF
    """
    plt.plot(timeLine, pmf)
    plt.show()



def areaCalc(PMF):
    """
    This function calculates the area under the curve described by the PMF of the distribution.
    :param PMF: Probability mass function
    :return: Area under the curve using the trapezoid method
    """
    pmf = np.asarray(PMF)
    area = np.trapz(pmf, dx=e-4)
    area2 = simps(pmf, dx=0.0001)
    print("area trap: ", area)
    print("area simps: ", area2)


if __name__ == '__main__':
    intLen = int(input("enter length of interval: "))
    startPoint = int(input("enter start: "))
    lambdaVal = float(input("enter lambda parameter: "))
    xAxis = poissonPreProcess(intLen, startPoint)
    pmfList = []
    for i in xAxis:
        pmfVal = poissonDist(lambdaVal, i)
        pmfList.append(pmfVal)
    pmfPlotter(pmfList, xAxis)

