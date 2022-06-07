from voice import speak
def level8(name, xp, shopping_points, item_list):
    # print(name, xp, shopping_points)
    score = 0
    print("========== LEVEL 8 ==========")
    speak("\nGood job for reaching the final stage!\n")
    print("===========================\n")
    speak("To win your treasure and end the game, you must correctly answer 3 out of 5 questions")
    print("\n===========================\n")
    speak("QUESTION 1\n")
    speak("What is a correct syntax to output 'Hello World' in Python?")
    question1 = {
        "A": "print('Hello  World')",
        "B": "echo('Hello World')",
        "C": "p('Hello World')"
    }
    speak("Your Options are as follows.\n"
            + "A: " + question1["A"] + ",\n"
            + "B: " + question1["B"] + ",\n"
            + "C: " + question1["C"] + "\n"
            )
    q1_count_chance = 2
    while q1_count_chance >= 1:
        answer1 = input("\nChoose A or B or C : ")
        if answer1.lower().strip() == "a" or answer1 == "A":
            speak("You picked: " + question1["A"])
            sound.play_correct_answer()
            speak("Correct!")
            print("\n===========================\n")
            score += 1
            q1_count_chance -= 2
        elif answer1.lower().strip() == "b" or answer1 == "B" or answer1.lower().strip() == "c" or answer1 == "C":
            sound.play_quiz_incorrect()
            speak("Option chosen is incorrect")
            print("\n===========================\n")
            q1_count_chance -= 2
        else:
            q1_count_chance -= 1
            if q1_count_chance >= 1:
                speak("Please enter a letter between A and C")
                print("\n===========================\n")
            elif q1_count_chance == 0:
                sound.play_quiz_incorrect()
                speak("You have entered two letters not in the options. Question missed!")
                print("\n===========================\n")
    q2_count_chance = 2
    speak("QUESTION 2")
    speak("Which one is NOT a legal variable name?")
    question2 = {
        "A": "_myvar",
        "B": "Myvar",
        "C": "my-var"
    }
    speak("Your Options are as follows.\n"
            + "A: " + question2["A"] + ",\n"
            + "B: " + question2["B"] + ",\n"
            + "C: " + question2["C"] + "\n"
            )
    while q2_count_chance >= 1:
        answer2 = input("\nChoose A or B or C : ")
        if answer2.lower().strip() == "c" or answer2 == "C":
            speak("You picked: " + question2["C"])
            sound.play_correct_answer()
            speak("Correct!")
            print("\n===========================\n")
            score += 1
            q2_count_chance -= 2
        elif answer2.lower().strip() == "b" or answer2 == "B" or answer2.lower().strip() == "a" or answer2 == "A":
            sound.play_quiz_incorrect()
            speak("Option chosen is incorrect")
            print("\n===========================\n")
            q2_count_chance -= 2
        else:
            q2_count_chance -= 1
            if q2_count_chance >= 1:
                speak("Please enter a letter between A and C")
                print("\n===========================\n")
            elif q2_count_chance == 0:
                sound.play_quiz_incorrect()
                speak("You have entered two letters not in the options. Question missed!")
                print("\n===========================\n")
    q3_count_chance = 2
    speak("QUESTION 3")
    speak("Which language does Terraform support from the below list?")
    question3 = {
        "A": "Hashicorp Language & JSON",
        "B": "XML",
        "C": "Plaintext"
    }
    speak("Your Options are as follows.\n"
            + "A: " + question3["A"] + ",\n"
            + "B: " + question3["B"] + ",\n"
            + "C: " + question3["C"] + "\n"
            )
    while q3_count_chance >= 1:
        answer3 = input("\nChoose A or B or C : ")
        if answer3.lower().strip() == "a" or answer3 == "A":
            speak("You picked: " + question3["A"])
            sound.play_correct_answer()
            speak("Correct!")
            print("\n===========================\n")
            score += 1
            q3_count_chance -= 2
        elif answer3.lower().strip() == "b" or answer3 == "B" or answer3.lower().strip() == "c" or answer3 == "C":
            sound.play_quiz_incorrect()
            speak("Option chosen is incorrect")
            print("\n===========================\n")
            q3_count_chance -= 2
        else:
            q3_count_chance -= 1
            if q3_count_chance >= 1:
                speak("Please enter a letter between A and C")
                print("\n===========================\n")
            elif q3_count_chance == 0:
                sound.play_quiz_incorrect()
                speak("You have entered two letters not in the options. Question missed!")
                print("\n===========================\n")
    # else statement is letter is not between a and c
    q4_count_chance = 2
    speak("QUESTION 4")
    speak("Which is not true about cloud computing?")
    question4 = {
        "A": "Cloud computing will decrease your capital expenses.",
        "B": "Cloud computing resources are usually constrained to a single region or availability zone.",
        "C": "Cloud service models include IaaS, SaaS and PaaS."
    }
    speak("Your Options are as follows.\n"
            + "A: " + question4["A"] + ",\n"
            + "B: " + question4["B"] + ",\n"
            + "C: " + question4["C"] + "\n"
            )
    while q4_count_chance >= 1:
        answer4 = input("\nChoose A or B or C : ")
        if answer4.lower().strip() == "b" or answer4 == "B":
            speak("You picked: " + question4["B"])
            sound.play_correct_answer()
            speak("Correct!")
            print("\n===========================\n")
            score += 1
            q4_count_chance -= 2
        elif answer4.lower().strip() == "a" or answer4 == "A" or answer4.lower().strip() == "c" or answer4 == "C":
            sound.play_quiz_incorrect()
            speak("Option chosen is incorrect")
            print("\n===========================\n")
            q4_count_chance -= 2
        else:
            q4_count_chance -= 1
            if q4_count_chance >= 1:
                speak("Please enter a letter between A and C")
                print("\n===========================\n")
            elif q4_count_chance == 0:
                sound.play_quiz_incorrect()
                speak("You have entered two letters not in the options. Question missed!")
                print("\n===========================\n")
    q5_count_chance = 2
    speak("QUESTION 5")
    speak("For which of the following reasons would you choose a region pair?")
    question5 = {
        "A": "To ensure compliance with local privacy regulations.",
        "B": "To replicate resources across longer distances to reduce impact of natural disasters or network outages that affect multiple nearby data centers.",
        "C": "To improve communications between pairs of applications."
    }
    speak("Your Options are as follows.\n"
            + "A: " + question5["A"] + ",\n"
            + "B: " + question5["B"] + ",\n"
            + "C: " + question5["C"] + "\n"
            )
    while q5_count_chance >= 1:
        answer5 = input("\nChoose A or B or C : ")
        if answer5.lower().strip() == "b" or answer5 == "B":
            speak("You picked: " + question5["B"])
            sound.play_correct_answer()
            speak("Correct!")
            print("\n===========================\n")
            score += 1
            q5_count_chance -= 2
        elif answer5.lower().strip() == "a" or answer5 == "A" or answer5.lower().strip() == "c" or answer5 == "C":
            sound.play_quiz_incorrect()
            speak("Option chosen is incorrect")
            print("\n===========================\n")
            q5_count_chance -= 2
        else:
            q5_count_chance -= 1
            if q5_count_chance >= 1:
                speak("Please enter a letter between A and C")
                print("\n===========================\n")
            elif q5_count_chance == 0:
                sound.play_quiz_incorrect()
                speak("You have entered two letters not in the options. Question missed!")
                print("\n===========================\n")
    speak("Your score is " + str(score) + " out of 5")
    print("\n===========================\n")
    if score >= 3:
        speak("CONGRATULATIONS!")
        # celebration sound
        sound.play_celebratory_song()
        speak("You have won the treasure. A SUM OF £10000!")
        print("\n===========================\n")
    elif score < 3:
        sound.play_game_over()
        speak("You have lost. Better luck next time\n")
    speak("Thank you for playing the game. Goodbye!")
    print("\n===========================")
