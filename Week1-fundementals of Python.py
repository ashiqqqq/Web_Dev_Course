import turtle


turtle = turtle.Turtle()
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)

# global count = 0


#create a square w a function and using while Loop
def square(length):
    count = 0
    while True:
        turtle.forward(length)
        turtle.left(90)
        count += 1
    # print (count)
        if count == 4:
            break

square(240) #1.7s


#create a squre within a square - dimensions
# square(240/2)

# this is to create multiple squares, extend beyond current square and redo the while loop.
#turtle.forward(90)
# shape(4)  #2.4s

'''******************************************************************************'''
# FROM THE COURSE
#while loop
i = 0
while i<50:
    print (i)
    i += 1


'''******************************************************************************'''
# Challange
# print a while loop that goes from 100 - 0 and prints 'boom' instead when it reaches 0

i= 100
while i != 0:
    print (i)
    i -= 1
    if i == 0:
        print ('Boom!')


'''******************************************************************************'''

# for loops
for i in range(0, 101):
    if i == 100:
        print ('Boom!')
    else:
        print(i)


'''******************************************************************************'''

# Data types in python!
 # integer = 1, 2, 3
 # float = 1.342 , -2.3
 # string = ' sda '
 # list = ['hello', 'ugly'] - easy to manipulate, also known as array
 # tuple = {'bound', 'hello'} - Sealed and not easy to add and remove
 # *impt* :
  # dictionary = {"John": '81184365', 'Billy': '92342132'}

"*******************************************************************************"

# Slicing of strings
print('Orange'[3])
print('Orange'[2:5])
print('Orange'[::2])


"**********************************************************************************"
# lIST +len + LOOP + Append

groceries = ['apple', 'banana', 'orange']
print(groceries)
movies =['You', 'X-men', 'Avengers', 'Inception']
print(movies)

print(len(movies))

for movie in movies:
    print(movie)

# lists are mutable
movies.append('Spider-Man')
print(movies , len(movies))
print(movies[1:4])


"*********************************************************************************"

# Sum Challange using loops
scores = [100, 34 , 23, 84, 29, 84,69,13,52,103]

def sum(int_list):
    checkpoint = 0
    for score in int_list:
        # checkpoint = checkpoint + score
        checkpoint += score
    return checkpoint

print(sum(scores))
# Correct

# find max
# print(max(scores))
#  OR use a for loop for max
def maxi(int_list):
    checkpoint = int_list[0]
    for score in int_list:
        if score > checkpoint:
            checkpoint = score
    return checkpoint

print(maxi(scores))

# OR usinf indexes

def maxim(int_list):
    checkpoint = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > checkpoint:
            checkpoint = int_list[i]
    return checkpoint

print(maxim(scores))

# Minimum
def mini(int_list):
    checkpoint = int_list[0]
    for i in int_list:
        if i < checkpoint:
            checkpoint = i
    return checkpoint

print(mini(scores))


"***********************************************************************************"

# filters using tuples & Loops

movies = [('Intersteller', 10), ('Ironman', 9.2), ('IT', 5.8), ('Underground', 3)]
print(len(movies))
print(type(movies))

print(movies)

def filter_best(list, wanted_rating):
    best_movies = []
    for movie in list:
        if movie[1] >= wanted_rating:
            best_movies.append(movie)
    return best_movies

print(filter_best(movies, 5))



"***********************************************************************************"
#  Dictionery (basic)

phone_book = {'John': '92717382', 'Billy': '82716381'}
print(phone_book['Billy'])
movies = {'Intersteller': 10, 'Ironman': 9.2, 'IT': 5.8, 'Underground': 3}
print(movies['Ironman'])



'************************************************************************************'
# Frequency count

movies = {'Intersteller': 10, 'Ironman':8.2, 'IT': 5.8, 'Underground': 3, 'X-men': 5.5, 'Avengers': 8.5}
print(len(movies))

# in dictory all key is unique. If unique is impt use dictionery.
# However not good for order of things . List will be better if u want to identify what was identified first .

# Challange : create a word frequency counter with a sentence.

sentence = 'Hello my name is ashiq . How are you doing doing ? Would you be interested to go out for a swim ? Maybe my other friends can join us as well ?'

def frequency_counter(sentence):
    # Create a list of individual words in the string provided.
    elements = sentence.split(' ')
    # Create an empty dict for new variables to be added in
    dict = {}
    # Iterate the process of adding new word
    for i in elements:
        if i not in dict:
            # dict[i] = 1
            dict.update({i : 1})
        # or increasing the counter if the word already existed
        else:
            dict[i] +=1
    return dict

print(frequency_counter(sentence))
# Success :)

# OR
# def frequency_counter(sentence):
#     # Create a list of individual words in the string provided.
#     # elements = sentence.split(' ')
#     # Create an empty dict for new variables to be added in
#     dict = {}
#     # Iterate the process of adding new word
#     # for i in sentence.split(' '):
#         if i not in dict:
#             # dict[i] = 1
#             dict.update({i : 1})
#         # or increasing the counter if the word already existed
#         else:
#             dict[i] +=1
    # return dict



"***********************************************************************************"
