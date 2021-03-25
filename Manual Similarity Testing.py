# lists to store results and used scenarios
test_data = []
used = []


import random
len1 = len(jobs_text)
len2 = len(courses_text)

# randomly finds a job and 2 courses
# runs until a unique selection of jobs and courses is found
# prints out the job and 2 courses
# asks the user which course is more similar to the job
fail = True
while fail == True:
    job1=(random.randint(0,len1))
    course1=(random.randint(0,len2))
    course2=(random.randint(0,len2))
    
    tuples = (job1,course1,course2)
    if course1 == course2 or tuples in used:
        fail = True
    else:
        used.append(tuples)
        print("job\n")
        print(jobs_text[job1])
        print("course1\n")
        print(courses_text[course1])
        print("course2")
        print(courses_text[course2])
        
        Similarity_score = input("Which is more similar? ") 
        tuples = (job1,course1,course2,int(Similarity_score))
        test_data.append(tuples)
        fail = False
