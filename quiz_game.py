questions = [
    {
        "question": "1. What is the chemical symbol for water?",
        "options": ["A. O2", "B. H20", "C. OH", "D. HO2"],
        "answer": "B",
        "prize": 200
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "B",
        "prize": 400
    },
    {
        "question": "3. Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Mark Twain"],
        "answer": "B",
        "prize": 800
    },
    {
        "question": "4. What is the largest ocean in the world?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C",
        "prize": 1200
    },
    {
        "question": "5. Who discovered gravity?",
        "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Edison"],
        "answer": "A",
        "prize": 1600
    },
    {
        "question": "6. Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Carbon dioxide", "C. Hydrogen", "D. Nitrogen"],
        "answer": "B",
        "prize": 2000
    },
    {
        "question": "7. What is the hardest natural substance?",
        "options": ["A. Gold", "B. Diamond", "C. Iron", "D. Platinum"],
        "answer": "B",
        "prize": 3000
    },
    {
        "question": "8. Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Elon Musk", "D. Bill Gates"],
        "answer": "A",
        "prize": 4000
    },
    {
        "question": "9. Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. UK", "B. Germany", "C. France", "D. Spain"],
        "answer": "C",
        "prize": 6000
    },
    {
        "question": "10. What is the largest organ in the human body?",
        "options": ["Liver", "Skin", "Heart", "Lungs"],
        "answer": "B",
        "prize": 10000
    }
]

money = 0

print("Welcome to the Quiz Game!")
print("Answer 10 questions correctly to win Rs 10,000!")
print("-------------------------------------------------\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    answer = input("\nEnter your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        money = q["prize"]
        print(f"Correct! Your current prize: Rs {money}\n")
    else:
        print("Wrong answer!")
        break

print("-------------------------------------------------")
print(f"You won a total of Rs {money}!")
print("Thank you for playing!")
