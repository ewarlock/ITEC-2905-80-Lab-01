#get number of classes
class_number = input('How many classes are you taking this semester? ')

#convert user's entry to an int
#this program would benefit from data validation...
class_int = int(class_number)

#blank list to be filled with class names
class_list = []

#prompt user to enter name of class x amount of times
#where x is the number the user initially entered
for x in range(class_int):
    class_list.append(input('Enter the name of the class: '))

#print all the user's classes one line at at time
print('Your classes are:')
for entry in class_list:
    print(entry)