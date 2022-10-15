# k = input("enter size s m l" )
# p = input()
# q = input()
# bill = 0
# if k == 's':
#  bill +=15
# elif k == 'm':
#  bill+=20
# else :
#    bill +=25
# if p == 'y':
#     if k == 's':
#         bill +=2
#     else :
#         bill +=3
# if q == "y":
#     bill +=1
# print(bill)                                         
                      
# d = k[0]
# y =k[1]
# t = int(d) + int(y)    #doing a type conversion from the input string to integer 



# if k>40:
#     z= k+4
#     print(z)
# if k%4==0:
#     print(k)

#Kulyash stays in room that has a single bulb and NN buttons. The bulb is initially on.

# The initial states of the buttons are stored in a binary string SS of length NN — if S_iS 
# i
# ​
#   is 00, the ii-th button is off, and if S_iS 
# i
# ​
#   is 11, the ii-th button is on. If Kulyash toggles any single button then the state of the bulb reverses i.e. the bulb lights up if it was off and vice versa.

# Kulyash has toggled some buttons and the final states of the buttons are stored in another binary string RR of length NN. He asks you to determine the final state 


#&& is invalid syntax in python
#here bmi already < than 18.5 so it jumped to next so need for and and condition
# a = "Aviral"
# b=a.lower()
# c = a.upper()
# d = a.count("{a}")
# print("",b,"\n",c,"/n",d) 

#print(" \' ")



# y = input("input size: ")
# z = input('peproni?:')
# k = input('chesse ')
# b = 0
# if y == "s" :
#     b+=15
# elif y == "m" :
#     b+=20
# else:
#     b+=25
# #for multiple if statements we can use another if statement    
# if z == 'y' :
#     if y == 's':
#         b+=1
#     else:
#         b+=3 
# #this was a separate if statement can be used in c++ also           
# if k == 'y':
#     b+=1   
# print(f"your bill is {b} ")
             
   
   
   
   
   
    # DAY 4 # building a rock paper scissor game at the end of the day
    #RANDOMISATION
    #MERSENNE TWISTER USED TO GENERATE A RANDOM NUMBER IN PYTHON







import random          #has many functions that can be used to generate random numbers(integers , floating point numbers etc.)
# [a = random.randrange(4, 15)]      #this funvction generates a random 
# [print(a ,"\n")  ]   #hover over the code or i should say over the rand range function and get to know a lot about it 
#[b = random.randint(4, 15)]     #both of these generate random integers 
# [print(b)]
# #module is resposible for differrent function like when building a car 
# #we need different parts and it is made by diiferent gropu of people who splits the work among them
# #some car may have different functions so different bodies are setup for making different parts
  
  
# #we can build our own pyhton modules also by creating a new python file and use a stored function or value in this pyhton code 
# #by filename.function_name   


# [c = random.random()]   #generates random number between 0 and 1(1 not included)
# [print(c)]
# #print a random number between 0 and 5

# #[d = random.randint()] #here i was trying to add a random integer between 0 and 5 and a floating number] 
# [e=random.random()]
# [print(e*5)]



    #DAY 4 lec 3 CREATE A PROGRAM TO GENERATE RANDOM HEAD OR TAIL
# a = random.randint(0,1)  #always the lower one first and then the higher one on the right
# if (a==1) :
#     print("heads")
# else:
#     print("tails")    
       
       
       #DAY 4 LEC4 lists - a way of storing nd organising data
       
# fruits =["cherry", 35,TRUE, "mango","grapes"]
# print(fruits[1]," ",fruits[2]," ",fruits[-1],"\n") 
# usa = ["delawrae", "pennsylvania "] 
# print(f"the two states of america are {usa[0]} & {usa[1]}")
# #we can change the items in the list using index like this
# fruits[1]="banana"
# print(fruits)   
# fruits.append("oranges")#used to add items to the list
# print (fruits)   #DO WATCH FROM 10:55 TIME STAMP AGAIN

# DAY 4 WHO IS PAYING THDE BILL 



# persons = input("input names")
# name = persons.split(",") #here split splits the string using some indicator we will give it here comma and create them into list
# c=len(name)
# # d = random.randint(0,c-1)
# e = random.choice(name)
# # print(f"{name[d]} is going to pay the bill" )
# print(f"{e} is going to pay the bill" ) #here random.choice is doing the same thing as before

#lec 6 day 4

# fruits =["cherry", 35, "TRUE", "mango","grapes"]

# usa = ["delawrae", "pennsylvania "] 
# d = [fruits,usa]
# print(d)      #  nested list it prints the output as [['cherry', 35, 'TRUE', 'mango', 'grapes'], ['delawrae', 'pennsylvania ']]




#in nested  list we firstspecfy which list we are accesing inside the parent list and then specify the index number of the element inside the dughter list
 #eg 
 #day 4 lec 8
# fruits =["cherry", 35, "TRUE", "mango","grapes"]

# usa = ["delawrae", "pennsylvania "] 
# d = [fruits,usa]
# print(d[0][1]) #0 is the index of the list inside the parent list and 1 is the index of the element of the nested list we are trying to access    
 
 #list can be 2d 3d or 4d also               
#DAY 4 LEC 9 rock paper scissors project


# g = ["rock", "paper", "scissor"]
# e = int(input("enter between 0 and 2"))
# d= random.randint(0,2)
# print(f"your choice:{g[e]}")
# print(f"program choice:{g[d]}")

      
      
      
        #DAY 5 STARTS HERE LOOPS 
        
#lec 2 for loop 
# fruits =["cherry", 35, "TRUE", "mango","grapes"]
# for fruit in fruits:
#     print(fruit)  #for loop works differently in python than in c++
  
 #DAY 5 LEC 3 AVERAGE HEIGHT OF THE CLASS 
 
# h = input().split(",")
# #c=len(h) 


# for a in range(0,len(h)): #here range function is used instead of relational opertaor(As used in c++ such as a<n etc) for looping
#     h[a]=int(h[a])


# d = 0
# c=0



# for a in h:
#     if a>d:
#         d=a
# print( d,"\n")
#max and min function are used to find max and min in a list and sum used to find the sum of numbers in a list 


# h = 0
# for a in range(1,101):
#     if(a%3==0) and (a%5==0):
#         print("fizzbuzz")
#     elif (a % 3==0):
#         print("fizz")
#     elif (a %5==0):
#         print("buzz")
#     else :
#         print(a)        

#   DAY 5 lec 8 - completed on repel it
# a = int(input("how many letters would you like in ypur password? "))
# b = int(input("how many symbols would you like in ypur password? ")) 
# c = int(input("how many numbers would you like in your password "))
# for
 
 
 
 
 # DAY -6  LEC 2 defining a function 

# def a() :#here paranthesis is necessary to tell the machine that we are defining a function
#     print("this is how a function is created")
#     print("then we call the function whenever we want and use it  ")
# a() #here i have called the function and it has excuted the program i hav instucted it to do

    #indentation in the next line in a block of code is 4 spaces  


    #while loops lec 6


#loop will continue to go till a condition is true

# c = input()
# print(type(c))     #input always taken in string in python

# a = int(input())
# for x in range (a):
#     b = int(input())
#     n = math.log(b)/math.log(2)
#     print(n)
#     k = 0
    # while(b>c):
    #     c*=2
    #     n+=1
    # if ((2**(n+1)) == b):
    #     k=0
    # else:    
       
    #     d = b
    #     while (d>0):
    #         d-=2**n
    #         n = -1
    #         k+=1
    #         while(d>c):
    #             c*=2
    #             n+=1
            
        

        
            
    # print(k)    
    
    
    #DAY7
#Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# c = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {c}.')
# d = len(c)
# k=[]
# for x in range(d):
#   k.append("_")
# print(k)  
  
# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# i = 0
# tu = 0
# while(i<d) and (tu<5):
#   g = input("Guess a letter: ").lower()
  
#   #TODO-2: - Loop through each position in the chosen_word;
#   #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#   #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#   r = 0
#   for y in range(d):
#       if c[y] == g:
#           k[y] = g
#           i+=1
#           r = 1
#       # else :
#       #   print("try again")
#       #   g = input("Guess a letter: ").lower()
#   if (r==0):
#     print("try again")
#     d+=1
#   print(k)
# if (i==d):
#   print("very well you have solved the problem")
# else:
#     print("you have lost the game")  
  #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    
#in and not in is a keyword in  python to check a particular element or condition in python 

#    DAY 8 --- Caesaer Cipher
# def g(name):   #task was to create a function that greets you   
#       print(f"hello {name}")
#       print(f"nice to meet you {name}")#here in python we dont have to specify the type of data we are inputting inside the function
# # a = input()
# def h(k):
#       print(k**2)
# p = int(input())      
# print(p**2)
      





#    DAY -9 --- Python Dictionary and nesting
#build a  silent bidding program

#lec 2   in dictionary there are key and associated value of the key


#everyhting is inside a curly brace    {key : value,key:value,....}



# practicing_naming =  {#dictionary can be written in multiple lines
#     "yashu" : "chota bhai",
#     "kanchan prakash / micky" : "mummy",
#     "prakash yadav":"papa" 
#     }


#to retrive or use data/value instead of index 
# as in list we use key here and it gives the value
  
#eg

# print(practicing_naming["yashu" ],"\n" )        #here the output recieved is chota bhai
# print(practicing_naming)#here it printed the whole dictionary keys and values both






# #  wipe an existing dictionary 
# practicing_naming = {}
# print(practicing_naming) 


# #here the result was an empty dictionary

# #now we can redefine a key in python like dictionary_name[key] = value


# #if the key is not present then python will add a new key and use value 


# practicing_naming["micky"]="mummy" ## avery important thing to note here is that we are using = sign not the : sign for adding 
# print(practicing_naming)
# #one very important thing here i dont have to comment out all the codes 
# #i can keep the codes writes the notes beside it and make a new cell more convinient


#how to loop through a dictionary


#for thing in practicing_naming:
#    print(thing)
    
# '''here a wonderful thing happend i was able to print out the key of 
#  the dictionary instead of value'''
   
   
    # print(practicing_naming[thing]) 
    
#now this will print value that certainly helps me get a hold of item certainly     
#day 9 repeated by me


# a = {"yeti":"a monster","well":"drink water", "why" : "keeps you healthy",
#      "can also be ":"written in multiple ",
#      "lines ":"like this"}
# print(a["yeti"])#this is the way to retrieve data from a dictionary
# #this way we can only access the value not the key  
# print(a)#prints the whole dictionary

#  #when looping through the dictionary it prints or gives the hold of key not the values for eg
# for like in a:
#     print(like)  #it printed the keys like is a random word used for looping and that is confusing for me 
# #for getting  hold of values in loop simply write it like this 

# for k in a :
#     print(a[k])   


# #video 4 nesting  in dictionary watch it again too easy and too lazy of me to code whole o it
# #eg 
# a = {"e":{"pikachu":"electric type", "buizel": "water type","charizard":"fire type"},"favorite ones":["dawn", "brock","misty","serena", "bonnie", "clemont"] }
# #video 5 day 9 do again easy peasy walk through


#the final bidding program 
import os


# k = {"my current wish":{"personal": ["get an amount of money so that i can support my family","can live without any fear"]},"professional":"i wish to be better"}
# print(k)
# a = int(input())
# if (a==1):
#     os.system('cls') #here this works fine too
# else:
#     print("this works fine and clears the whole console that's really good ")

#FINAL VIDEO



# ans = "yes"
# while (ans == "yes"):
#     bid = {}
#     a = input("what is your name?:")
#     b = int(input("enter your bid:"))
#     ans = input("are there any other bidders?")
#     bid[a]= b
#     os.system('cls')

# k  = 0 
# for m in bid:
#     if bid[m]>k:
#         k = bid[m]
#         t = m
# print(m)  
#yes i have coded the whole program myself and done this day 



#DAY 9 COMPLETED AND DAY 10 STARTS
 

         









 