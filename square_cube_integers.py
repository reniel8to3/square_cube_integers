#Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

#def process for opening file
with open("integers.txt") as integer_list:
    integers = integer_list.read().split()
#compute int squared
def square(x):
    return x **2
#computed int cubed
def cube(x):
    return x** 3
#create list for both even & odd
even=[]
odd=[]
#check if even or odd



#make text files for both even and odd.