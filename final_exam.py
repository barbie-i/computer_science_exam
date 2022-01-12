#1
def add_function(number, anotherNumber):
    return number + anotherNumber

result = add_function(1, 2)

#2
import random
def get_random(start, end):
    random_number = random.randint(start, end)
    return random_number

random_num = get_random(0, 99) 
print(random_num)

#3
counter = 0
while(counter < 4):
    print("Today, I am outstanding in every way", counter)
    counter = counter + 1

#4
for quote in range(200):
    print("I become what I think about most of the time")

#5
an_input = input("Enter your name:")
print("You look great today", an_input)

#6
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
print(alphabet_length)

#7
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_j = alphabet.index("j")
print(position_of_letter_j + 1)

#8
from array import array
array =  array("i", [90, 70, 40, 60, 98, 97, 93])

print(array)

#9
array.append(80)
print(array)

#10
length_of_array = len(array)
print(length_of_array)

#11
computer_science_student_names =  ["Fluffy Pigeon", "Just Pigeon", "Arsalon"]

#12
computer_science_student_names.remove("Arsalon")

#13
computer_science_student_names.sort()
print(computer_science_student_names)

#14
student_and_scores = {
    "Fluffy Pigeon": [1, 1, 1], 
    "Just Pigeon": [1, 1, 1], 
    "Arsalon": [99, 100, 99]
}

#15
Arsalon_scores = student_and_scores.get("Arsalon")
print(Arsalon_scores)
