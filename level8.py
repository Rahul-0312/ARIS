import os
import pprint


def level8(name, xp, shopping_points, item_list):
    # print(name, xp, shopping_points)
    score = 0
    print("Good job for reaching the final stage!")
    print("To win your treasure and end the game, you must correctly answer 3 out 5 questions")

    print("QUESTION 1")
    print("Who is the dog?")
    question1 = {
        "A": "Bingo",
        "B": "Bruno",
        "C": "Ella"
    }
    print(*[str(option) + ': ' + str(answer) for option, answer in question1.items()], sep='\n')
    q1_count_chance = 2
    while q1_count_chance >= 1:
        answer1 = input("Choose A or B or C : ")
        if answer1.lower().strip() == "a" or answer1 == "A":
            print("You picked: " + question1["A"])
            print("Correct!")
            score += 1
            q1_count_chance -= 2
        elif answer1.lower().strip() == "b" or answer1 == "B" or answer1.lower().strip() == "c" or answer1 == "C":
            print("Option chosen is incorrect")
            q1_count_chance -= 2
        else:
            q1_count_chance -= 1
            if q1_count_chance >= 1:
                print("Please enter a letter between A and C")
            elif q1_count_chance == 0:
                print("You have entered two letters not in the options. Question missed!")

    q2_count_chance = 2
    print("QUESTION 2")
    print("Who is the dog?")

    question2 = {
        "A": "Bingo",
        "B": "Bruno",
        "C": "Ella"
    }
    print(*[str(option) + ': ' + str(answer) for option, answer in question2.items()], sep='\n')
    while q2_count_chance >= 1:
        answer2 = input("Choose A or B or C : ")
        if answer2.lower().strip() == "c" or answer2 == "C":
            print("You picked: " + question2["C"])
            print("Correct!")
            score += 1
            q2_count_chance -= 2
        elif answer2.lower().strip() == "b" or answer2 == "B" or answer2.lower().strip() == "a" or answer2 == "A":
            print("Option chosen is incorrect")
            q2_count_chance -= 2
        else:
            q2_count_chance -= 1
            if q2_count_chance >= 1:
                print("Please enter a letter between A and C")
            elif q2_count_chance == 0:
                print("You have entered two letters not in the options. Question missed!")

    q3_count_chance = 2
    print("QUESTION 3")
    print("Who is the dog?")
    question3 = {
        "A": "Bingo",
        "B": "Bruno",
        "C": "Ella"
    }
    print(*[str(option) + ': ' + str(answer) for option, answer in question3.items()], sep='\n')
    while q3_count_chance >= 1:
        answer3 = input("Choose A or B or C : ")
        if answer3.lower().strip() == "a" or answer3 == "A":
            print("You picked: " + question3["A"])
            print("Correct!")
            score += 1
            q3_count_chance -= 2
        elif answer3.lower().strip() == "b" or answer3 == "B" or answer3.lower().strip() == "c" or answer3 == "C":
            print("Option chosen is incorrect")
            q3_count_chance -= 2
        else:
            q3_count_chance -= 1
            if q3_count_chance >= 1:
                print("Please enter a letter between A and C")
            elif q3_count_chance == 0:
                print("You have entered two letters not in the options. Question missed!")
    # else statement is letter is not between a and c

    q4_count_chance = 2
    print("QUESTION 4")
    print("Who is the dog?")
    question4 = {
        "A": "Bingo",
        "B": "Bruno",
        "C": "Ella"
    }
    print(*[str(option) + ': ' + str(answer) for option, answer in question4.items()], sep='\n')
    while q4_count_chance >= 1:
        answer4 = input("Choose A or B or C : ")
        if answer4.lower().strip() == "b" or answer4 == "B":
            print("You picked: " + question4["B"])
            print("Correct!")
            score += 1
            q4_count_chance -= 2
        elif answer4.lower().strip() == "a" or answer4 == "A" or answer4.lower().strip() == "c" or answer4 == "C":
            print("Option chosen is incorrect")
            q4_count_chance -= 2
        else:
            q4_count_chance -= 1
            if q4_count_chance >= 1:
                print("Please enter a letter between A and C")
            elif q4_count_chance == 0:
                print("You have entered two letters not in the options. Question missed!")

    q5_count_chance = 2
    print("QUESTION 5")
    print("Who is the dog?")
    question5 = {
        "A": "Bingo",
        "B": "Bruno",
        "C": "Ella"
    }
    print(*[str(option) + ': ' + str(answer) for option, answer in question5.items()], sep='\n')
    while q5_count_chance >= 1:
        answer5 = input("Choose A or B or C : ")
        if answer5.lower().strip() == "b" or answer5 == "B":
            print("You picked: " + question5["B"])
            print("Correct!")
            score += 1
            q5_count_chance -= 2
        elif answer5.lower().strip() == "a" or answer5 == "A" or answer5.lower().strip() == "c" or answer5 == "C":
            print("Option chosen is incorrect")
            q5_count_chance -= 2
        else:
            q5_count_chance -= 1
            if q5_count_chance >= 1:
                print("Please enter a letter between A and C")
            elif q5_count_chance == 0:
                print("You have entered two letters not in the options. Question missed!")

    print("Your score is " + str(score) + " out of 5")

    if score >= 3:
        print("CONGRATULATIONS!")
        # celebration sound
        print("You have won the treasure. A SUM OF £10000!")

    elif score < 3:
        print("You have lost. Better luck next time")

    print("Thank you for playing the game. Goodbye!")
