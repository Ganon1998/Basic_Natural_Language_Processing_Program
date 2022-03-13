from SentenceReadingAgent import SentenceReadingAgent
import time
import matplotlib.pyplot as plt

def test():
    #This will test your SentenceReadingAgent
	#with nine initial test cases.

    test_agent = SentenceReadingAgent()
    Time = []
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    startTime = time.perf_counter()
    print(test_agent.solve(sentence_1, question_1))  # "Ada"
    endTime = time.perf_counter()
    Time.append(endTime - startTime)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_1, question_3))  # "Irene"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_1, question_4))  # "short"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_2, question_5))  # "David"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_2, question_6))  # "school"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_2, question_8))  # "walk"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    startTime2 = time.perf_counter()
    print(test_agent.solve(sentence_2, question_9))  # "8:00AM"
    endTime2 = time.perf_counter()
    Time.append(endTime2 - startTime2)

    # display tim taken to execute each task
    fig, ax = plt.subplots()
    ax.plot(x, Time)
    ax.grid()
    plt.xlabel('Trial Number')
    plt.ylabel('Time taken to complete task')
    ax.text(0.5, 0.5, 'Jordan Elijah Greene', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation='30')
    plt.show()

    # Other sentences if you want to try them
    s1 = "There are a thousand children in this town."
    q1 = "Where are the children?"

    s2 = "The white dog and the blue horse play together."
    q2 = "What animal is blue?"

    s3 = "The red fish is in the river."
    q3 = "What is in the river?"

    s4 = "Serena and Ada took the blue rock to the street."
    q4 = "Who was with Ada?"

    s5 = "This tree came from the island."
    q5 = "Where did the tree come from?"

    s6 = "My dog Red is very large."
    q6 = "How big is Red?"

    s7 = "The red fish is in the river."
    q7 = "Where is the fish?"

    s8 = "Bring the box to the other room."
    q8 = "Where should the box go?"

    s9 = "My dog Red is very large."
    q9 = "What is my dog's name?"

    s10 = "She will write him a love letter."
    q10 = "Who was written a love letter?"

    s11 = "The white dog and the blue horse play together."
    q11 = "What do the dog and horse do?"

    s12 = "The house is made of paper."
    q12 = "What is made of paper?"

    s13 = "Serena ran a mile this morning."
    q13 = "What did Serena run?"

    s14 = "Lucy will write a book."
    q14 = "What will Lucy write?"

    s15 = "The water is blue."
    q15 = "What color is the water?"

    s16 = "There are one hundred adults in that city."
    q16 = "Where are the adults?"

    s17 = "The water is blue."
    q17 = "What color is the water?"

    s18 = "She will write him a love letter."
    q18 = "What will she write to him?"

    s19 = "The white dog and the blue horse play together."
    q19 = "What color is the dog?"

    s20 = "Their children are in school."
    q20 = "Who is in school?"

    s21 = "This year will be the best one yet."
    q21 = "What will this year be?"

    s22 = "The island is east of the city."
    q22 = "Where is the island?"

    s23 = "Give us all your money."
    q23 = "How much of your money should you give us?"

    s24 = "There are three men in the car."
    q24 = "Who is in the car?"

    s25 = "She told her friend a story."
    q25 = "What did she tell?"

    s26 = "Serena saw a home last night with her friend."
    q26 = "Who was with Serena?"


if __name__ == "__main__":
    test()