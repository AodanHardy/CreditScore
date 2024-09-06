"""
CreditScore class will initiate the score and stores the list of CreditScoreQuestion objects
presentScore() will loop through each question, adding the string representation to a string
builder and totaling the score
analyseScore() will get 2d tuple from constants that determines the thresholds of each rating and
presents it at the end of the builder
"""
from constants import SCORE_DEFAULT, THRESHOLDS, DEFAULT_THRESHOLD


class CreditScore:
    def __init__(self, listOfQuestions):
        self.score = SCORE_DEFAULT
        self.listOfQuestions = listOfQuestions

    def presentScore(self):
        builder = "\n\n\n"
        for question in self.listOfQuestions:
            self.score += question.score
            builder += question.__str__()

        builder += f"======================================================================================\n" \
                   f"Total Score                                                            {self.score}\n"
        builder += f"Score Assessment                                                       {analyseScore(self.score)}"
        return builder


def analyseScore(score):
    for item in THRESHOLDS:
        if score >= item[1]:
            return item[0]
    return DEFAULT_THRESHOLD
