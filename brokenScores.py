def score_check(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")


def error_loop(score):
    print("Invalid score")
    score = float(input("Enter score: "))
    return score


def get_score():
    score = float(input("Enter score: "))
    return score


def main():
    score = get_score()
    while score < 0 or score > 100:
        score = error_loop(score)
    else:
        score_check(score)


main()