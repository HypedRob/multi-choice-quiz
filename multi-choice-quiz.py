# lists
questions = ["What is 1 + 1",
             "Who is the 45th president of the United States?",
             "True or False... The Toronto Maple Leafs have won 13 Stanley Cups?",
             "What was the last year the Toronto Maple Leafs won the Stanley Cup?",
             "True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau?"]
answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
                  "a)Barack Obama\nb)Hillary Clinton\nc)Donald Trump\nd)Tom Brady\n:",
                  ":",
                  "a)1967\nb)1955\nc)1987\nd)1994\n:",
                  ":"]
correct_choices = [{"b", "2"},
                   {"c", "donald trump"},
                   {"true", "t"},
                   {"a", "1967"},
                   {"false", "f"}]
answers = ["1 + 1 is 2",
           "The 45th president is Donald Trump",
           "",
           "The last time the Toronto Maple Leafs won the Stanley Cup was 1967",
           "The current Prime Minster of Canada is Justin Tredeau"]

questions_b = ["Who painted the Mona Lisa",
               "Which planet is closest to the sun?",
               "How many valves does the heart have?",
               "What nut is in the middle of a Ferrero Rocher?",
               "How many minutes in a game of rugby league?"]
answer_choices_b = ["a)Vincent Van Gogh\nb)Leonardo da Vinci\nc)Michelangelo\nd)Pablo Picasso\n:",
                    "a)Mercury\nb)Venus\nc)Mars\nd)Neptune\n:",
                    "a)Three\nb)One\nc)Five\nd)Four\n:",
                    "a)Walnut\nb)Hazelnut\nc)Almond\nd)Macadamias\n:",
                    "a)80 minutes\nb)60 minutes\nc)40 minutes\nd)20 minutes\n:"]
correct_choices_b = [{"b", "Leonardo da Vinci"},
                     {"a", "Mercury"},
                     {"d", "Four"},
                     {"b", "Hazelnut"},
                     {"a", "80 minutes"}]

answers_b = ["Leonardo da Vinci painted the Mona Lisa",
             "Mercury is the planet closest to the sun",
             "The heart has four valves",
             "A hazelnut is in the middle of a Ferrero Rocher",
             "There are 80 minutes in a game of rugby league"]
run = "y"


def quiz_a():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")



def quiz_b():
    score = 0
    for question, choices, correct_choice, answer in zip(questions_b, answer_choices_b, correct_choices_b, answers_b):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")


# start of program
# Quiz B is people age 8 to 11
# Quiz A is people less than 8

name = input("Welcome to this multi-choice quiz designed for people between 5 and 11.\
            \nWhat is your name?: ")
age = int(input("How old are you?: "))
print(f"Welcome {name}. You are {age} years old.")
while run == "y":
    if age < 5:
        leave = input("You are too young. Do you still want to play? y/n: ")
        if leave == "n":
            print("Goodbye")
            break
        elif leave == "y":
            print("Starting now. You will be doing Quiz A")
            quiz_a()
            play_again = input("Do you want to play Quiz B now? y/n: ")
            if play_again.lower() == "y":

                quiz_b()
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Goodbye")
                break

        else:
            break
    elif age > 11:
        leave = input("You are too old. Do you still want to play? y/n: ")
        if leave == "n":
            print("Goodbye")
            break
        elif leave == "y":
            print("Starting now. You will be doing Quiz B")
            quiz_b()
            play_again = input("Do you want to do the other quiz? y/n: ")
            if play_again.lower() == "y":
                print("Okay starting Quiz A")
                quiz_a()
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Goodbye")
                break
        else:
            break
    elif age <= 5 and age < 8:
        print("Starting now. You will be doing Quiz A")
        quiz_a()
        play_again = input("Do you want to do the other quiz? y/n: ")
        if play_again.lower() == "y":
            print("Okay starting Quiz B")
            quiz_b()
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Goodbye")
            break
    else:
        if age >= 8 and age <= 11:
            print("Starting now. You will be doing Quiz B")
            quiz_b()
            play_again = input("Do you want to do the other quiz? y/n: ")
            if play_again.lower() == "y":
                print("Okay starting Quiz A")
                quiz_a()
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Goodbye")
                break
