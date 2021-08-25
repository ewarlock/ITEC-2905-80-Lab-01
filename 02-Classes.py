class_number = input('How many classes are you taking this semester? ')

class_int = int(class_number)

class_list = []

for x in range(class_int):
    class_list.append(input('Enter the name of the class: '))

print('Your classes are:')
for entry in class_list:
    print(entry)