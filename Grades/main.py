from Grades import names
from Grades import scores
from Grades import mean
from Grades import grades


def run_program():
    print("Student Name: ", names.get_names(), "Total Score: ", scores.get_scores(),
          "Mean Score: ", mean.get_mean(), "Mean Grade: ", grades.get_grades())


run_program()
