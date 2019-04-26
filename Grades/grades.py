from Grades.mean import *


def get_grades():
    if get_mean() in range(80, 101):
        g = 'A'
        r = 'Excellent!'
        return g, r
    elif get_mean() in range(70, 80):
        g = 'B'
        r = 'Good!'
        return g, r
    elif get_mean() in range(60, 70):
        g = 'C'
        r = 'Average!'
        return g, r
    elif get_mean() in range(50, 60):
        g = 'D'
        r = 'Below Average!'
        return g, r
    else:
        g = 'F'
        r = 'Put more Effort!'
        return g, r
