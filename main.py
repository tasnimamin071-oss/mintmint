question = ("who is the king?: ",
            "who is the goat?: ",
            "who is the fastest?: ")

option = (("A. agy", "B. you"),
         ("A. agy", "B. you"),
         ("A. agy", "B. you"))

answer = ("A", "A", "A")

guesees = []
score = 0
question_num = 0

for q in question:
    print("------------------")
    print(q)

    for o in option[question_num]:
        print(o)

    print("------------------")
    guess = input("enter(A or B): ").upper()
    guesees.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("Correct!")

    else:
        print("Wrong!")

    question_num += 1

print("---------RESULT--------------")


print("answer: ", end="")
for a in answer:

    print(a, end=" ")
print()


print("guess: ", end="")
for guess in guesees:

    print(guess, end=" ")
print()

score = int(score / len(question) * 100)
print(f"score: {score}")

print("TWIN,U KNOW MY WIFE IS THE BEST RIGHT?")























