import random

current_score = 0
questions_answered = 0


math = [{"question": "What is 2 + 2?", "options": ["A: 3", "B: 4", "C: 5", "D: 6"], "answer": "B"},
            {"question": "What is 5 * 6?", "options": ["A: 30", "B: 35", "C: 25", "D: 40"], "answer": "A"},
            {"question": "What is 10 / 2?", "options": ["A: 2", "B: 4", "C: 5", "D: 6"], "answer": "C"},
            {"question": "What is 9 - 3?", "options": ["A: 5", "B: 6", "C: 7", "D: 8"], "answer": "B"},
            {"question": "What is 29 + 102?", "options": ["A: 234", "B: 131", "C: 132", "D: 146"], "answer": "B"}]


history = [{"question": "Who was the first president of the United States?", "options": ["A: George Washington", "B: Thomas Jefferson", "C: Abraham Lincoln", "D: John Adams"], "answer": "A"},
            {"question": "In which year did World War II end?", "options": ["A: 1945", "B: 1939", "C: 1918", "D: 1950"], "answer": "A"},
            {"question": "Who was the leader of the Soviet Union during World War II?", "options": ["A: Joseph Stalin", "B: Vladimir Lenin", "C: Nikita Khrushchev", "D: Leon Trotsky"], "answer": "A"},
            {"question": "What was the name of the ship that sank in 1912?", "options": ["A: Titanic", "B: Lusitania", "C: Britannic", "D: Olympic"], "answer": "A"},
            {"question": "Who was the first man to step on the moon?", "options": ["A: Neil Armstrong", "B: Buzz Aldrin", "C: Michael Collins", "D: Yuri Gagarin"], "answer": "A"}]


science = [{"question": "What is the chemical symbol for water?", "options": ["A: H2O", "B: CO2", "C: O2", "D: N2"], "answer": "A"},
            {"question": "What planet is known as the Red Planet?", "options": ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"], "answer": "B"},
            {"question": "What is the speed of light?", "options": ["A: 299,792 km/s", "B: 150,000 km/s", "C: 1,080,000 km/s", "D: 300,000 km/s"], "answer": "A"},
            {"question": "What is the largest organ in the human body?", "options": ["A: Heart", "B: Liver", "C: Skin", "D: Brain"], "answer": "C"},
            {"question": "What is the process by which plants make their food?", "options": ["A: Photosynthesis", "B: Respiration", "C: Transpiration", "D: Fermentation"], "answer": "A"}]
    
def progress(answer, topic_name):
    global current_score
    global questions_answered
    if answer == topic_name[questions_answered]["answer"]:
        current_score += 1
        print("Correct!")
    else:
        print("Incorrect.")
    questions_answered += 1

def question_prompt(topic_name):
    global science
    global history
    global math

    if topic_name == "math":
        topic_name = math
    elif topic_name == "history":
        topic_name = history
    elif topic_name == "science":
        topic_name = science
    else:
        print("\nInvalid topic. Please choose Math, History, or Science.")
        return question_prompt(input("Choose a quiz topic (Math, History, Science): ").lower())
    
    random.shuffle(topic_name)
    for q in topic_name:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer_prompt(topic_name)


def user_answer_prompt(topic_name):
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer not in ["A", "B", "C", "D"]:
        print("\nInvalid input. Please enter A, B, C, or D.")
        return user_answer_prompt(topic_name)
    else:
        progress(user_answer, topic_name)
        print("")

print("===================================================")
print("            Welcome to the Quiz Game!")
print("===================================================")
print("\nTest your knowledge in Math, History, or Science.")
print("Answer the questions by entering A, B, C, or D.")
print("Your score will be displayed at the end of the quiz.")
print("Good luck!\n")
print("Let's get started!")

topics = input("Choose a quiz topic (Math, History, Science): ").lower()
question_prompt(topics)

print("Quiz completed!")
print(f"Your Final Score is {current_score} out of 5.")
if current_score == 5:
    print("Excellent work! You got a perfect score!")
elif current_score < 3:
    print("Better luck next time! Keep practicing to improve your score!")
else:
    print("Great job! You scored above average!")