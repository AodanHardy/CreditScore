"""
CreditScoreQuestion class stores the data for each question asked to the user
it takes the question, asks the user and then stores the answer as YES or NO
and the score relevant to the answer
"""


class CreditScoreQuestion:
    def __init__(self, question, yesScore, noScore):
        self.question = question
        self.answer, self.score = creditQuestion(question, yesScore, noScore)

    # toString method gets the string representation of the data stored in the object
    def __str__(self):
        return f"======================================================================================\n" \
               f"Question: {self.question}\n" \
               f"Answer: {self.answer}                              Affect on score: {self.score}\n"


# Credit question converts answers to consistent and presentable answers and
# returns with the answer. If answer is not yes or no it will loop until it is
def creditQuestion(question, yesScore, noScore):
    while True:
        answer = input(question)
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return 'YES', yesScore
        elif answer.lower() == 'no' or answer.lower() == 'n':
            return 'NO', noScore
        else:
            print("Error - answer should be yes or no \nPlease try again")
