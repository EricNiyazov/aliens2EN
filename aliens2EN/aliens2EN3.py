#final version

#set answer1 to false
answer1 = False

#set answer2 to false
answer2 = False

#user introduction 
print ("There are aliens on Earth and we need to know there population")
print (" ")
print ("Please answer in whole numbers")
print ("First we need to know how many aliens landed to begin with. ")
print ("Please answer in one whole number in form ex 1,2,69")
weeks = ("week.")#set first week to "week" 

#while loop for answer1
while answer1 == False:
    try:
        pop = int(input("How many aliens landed? ")) #first variable/ask user question 1
        if pop >= 1: #if user inputs # greater than/equal to 1, then say: 
            print("Ok")
            answer1 = True #answer1 only sets to true if they answer question correctly
        else: 
            print ("That is not the answer I'm looking for")
            #answer1 is not true if user does not input correct answer

    except ValueError: #if user inputs incorrect answer
        print ("Please answer with a positive whole number") #re-explain directions


#while loop for answer2 
while answer2 == False:
    try:
        time = int(input("Now, how many aliens landed on Earth?")) #second variable/ask user question 2
        if time >= 1: #if user inputs # greater than/equal to 1, then say:
            print ("Ok very good") 
            answer2 = True #answer2 only sets to true if they answer question correctly 
        else:
            print ("That is not the answer I'm looking for")
            #answer1 is not true if user does not input correct answer

    except ValueError: #if user inputs incorrect answer 
        print ("Please answer with a positive whole number") #re-explain direction 

#for loop
for i in range(time):
    print ("There are", pop*(2)**(i+1), "aliens on Earth after",i+1, weeks,) #calculations 
    weeks = ("weeks.") #set weeks to "weeks" 
