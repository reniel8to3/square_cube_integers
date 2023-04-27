#Name: Malabo, Reniel A.            #Section: BSCPE 1-5
#Subject: Object-Oriented Programming 
print ('This program sorts integers from 1-20 into even or odd and separates them into two text files. Even numbers are squared and added to double.txt while odd numbers are cubed and added to triple.txt')
#Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.
#def process for opening file
with open ("integers.txt", "r") as integer_file:
    integers = list(map(int, integer_file.read().split()))
#compute int squared
def squared(x):
    return x **2
#computed int cubed
def cubed(x):
    return x** 3
#create list for both even & odd
even=[]
odd=[]
#check if even or odd
for i in integers:
    integer=int(i)
    #if even, add to even list
    if integer %2 ==0:
        even.append(integer)
    #if odd, add to odd list
    else:
        odd.append(integer)
#make text files for both even and odd
with open("double.txt", "w") as squared_file:
    for even in even:
        squared_file.write(str(squared(even))+"\n")
with open("triple.txt", "w") as cubed_file:
    for odd in odd:
        cubed_file.write(str(cubed(odd))+"\n")