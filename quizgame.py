questions = ("Which planet is known as the Red Planet?",
             "What is the chemical symbol for gold?",
             "Who wrote the famous play Romeo and Juliet?",
             "What is the tallest mammal on Earth?",
             "Which country is known as the Land of the Rising Sun?")

options = (("A.Venus ", "B.Mars ", "C.Jupiter ", "D.Saturn "),
           ("A.Au ", "B.Ag ", "C.Fe ", "D.Hg "),
           ("A.William Shakespeare ", "B. Jane Austen ", "C.Scott Fitzgerald ", "D.Charles Dickens "),
           ("A.Giraffe ", "B.Elephant ", "C.Blue Whale ", "D.Hippopotamus "),
           ("A.China ", "B.Japan ","C.India ","D.South Korea"))


answers = ("B","A","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("enter the options(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")

    question_num +=1

print("---------------------------------------------")
print("                RESULTS                       ")
print("----------------------------------------------")


print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your score is {score}%")

