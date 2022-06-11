questions = open('questions.txt', 'r')
questions_list = [question.strip() for question in questions]
questions.close()

max_score = len(questions_list)

score = 0

for question in questions_list:
    q, a = question.split('=')
    answer = input(f"{q}=")
    if answer == a:
        score += 1
        
result = open('result.txt', 'w')
result.write(f"Your final score is {score}/{max_score}.")
result.close()
