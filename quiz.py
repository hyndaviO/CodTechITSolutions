def quiz_play() :
    questions = [
    "How many elements are in periodic table",
    "Which planet in the solar system is the hottest?",
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet",
    "What does USB stand for?",
    "What is the tallest building in the world?"
    ]
    options = [
    ("A. 116","B. 117","C. 118","D. 119"),
    ("A. Mercury ","B. Venus","C. Earth","D. Mars"),
    ("A. Rome","B. Paris","C. Berlin","D. Madrid"),
    ("A. William Shakespeare","B. Thomas Dekker","C. Ben jonson","D. John Marston"),
    ("A. Unique Serial Bus","B. Universal serial bus","C. Unary Serial Bus","D. Universal Secondary Bus"),
    ("A. Shaghai Tower","B. Abraj AI-Bait Clock Tower","C. Lotte World Tower","D. Burj Khalifa"),
     ]
    answers = ("C","B","B","A","B","D")
    guesses = []
    score = 0 
    question_num = 0 
    for question in questions:
        print("----------------")
        print(question)
        for option in options[question_num]:
            print(option)
        user_guess = input("Enter (A,B,C,D): ").upper()
        guesses.append(user_guess)
        if user_guess == answers[question_num]:
            score += 1 
            print("CORRECT!")
        else:
            print("INCORRECT")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1
    print("-----------------------------------")
    print("-----------------------------------")
    print("RESULTS")
    print("-----------------------------------")
    print("-----------------------------------")

    print("answers: ",end="")
    for ans in answers:
        print(ans,end=" ")
    print()
    print("YOUR ANSWERS: ",end="")
    for guess in guesses:
        print(guess,end=" ")
    print() 
    score = int(score/len(questions) * 100)
    print(f"Your score is : {score}%")



print("WELCOME TO QUIZ GAME")
print("Are you ready to play..")
user_input = input("Enter yes or no: ").lower()
if (user_input == "yes"):
    quiz_play()
if (user_input == "no"):
    print("Thank You for response")




