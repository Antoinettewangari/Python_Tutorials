maths = int(input("Enter Maths score: \n"))
eng = int(input("Enter English score: \n"))
swa = int(input("Enter Swahili score: \n"))
physics = int(input("Enter Physics score: \n"))
history = int(input("Enter History score: \n"))


def get_scores():
    total = maths + eng + swa + physics + history
    return total
