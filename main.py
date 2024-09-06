from creditScoreQuestion import CreditScoreQuestion
from creditScore import CreditScore


def runCreditScoreCheck():
    # Adding questions to CreditScoreQuestion object, which will ask the question and store it
    question1 = CreditScoreQuestion("Do you have a mortgage? (yes/no):", -10, 5)
    question2 = CreditScoreQuestion("Are you currently in debt (excluding your mortgage)? (yes/no):", -15, 10)
    question3 = CreditScoreQuestion("Do you have any unpaid credit card balances? (yes/no): ", -10, 10)
    question4 = CreditScoreQuestion("Do you make your credit card payments on time? (yes/no): ", 15, -20)
    question5 = CreditScoreQuestion("Have you ever declared bankruptcy? (yes/no): ", -30, 20)
    question6 = CreditScoreQuestion("Do you have any outstanding loans (car loan, personal loan, etc.)? (yes/no): ",
                                    -10,
                                    10)
    question7 = CreditScoreQuestion("Do you regularly save a portion of your income? (yes/no): ", 10, -5)
    question8 = CreditScoreQuestion("Have you been employed at your current job for more than two years? (yes/no): ",
                                    10,
                                    -5)
    question9 = CreditScoreQuestion("Do you have multiple credit cards? (yes/no): ", -5, 5)
    question10 = CreditScoreQuestion("Have you ever missed a loan payment? (yes/no): ", -20, 15)

    # Adding questions to list
    listOfQuestions = [question1, question2, question3, question4, question5,
                       question6, question7, question8, question9, question10]

    # Creating CreditScore object with listOfQuestions
    creditScore = CreditScore(listOfQuestions)

    # Print out the receipt
    print(creditScore.presentScore())


def main():
    # Main Loop
    while True:
        runCreditScoreCheck()

        goAgain = input("Would you like to go again? (y, or any other key to exit)")

        if "yes" != goAgain.lower() != 'y':
            print("Exiting....")
            break


main()
