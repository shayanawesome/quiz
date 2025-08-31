#make a quiz with score counting
#have 8 questions
# make the array for questions an array of arrays rather than array 
#of tuples 

score = 0

question_array = [
                  ["What is 3+10? ", 5], 
                  ["What is 6/2? ", 3],
                  ["What is 10*10? ", 100],
                  ["What is 3*4? ", 12],
                  ["What is 12/4? ", 3],
                  ["What is 9*8? ",72],
                  ["What is 2*5? ",10], 
                  ["What is 2*12? ",24],              
                ]

for question_tuple in question_array:
    question = question_tuple[0]
    correct_answer = str(question_tuple[1])
    answer = input(question)
    if answer == correct_answer:
        print("correct")
        score +=1
    else:
        print("incorrect")
        score -=1

if score < len(question_array)/2:
        print("You did a bad job. This is your score: ", score)
else:
        print("Good job, this is your score:", score)




   
                 
                 

                  


