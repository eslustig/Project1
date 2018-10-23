import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv


def getData(file):

	input_file = open(file,"r")
	lines = input_file.readlines()
	input_file.close()

	my_dicts = []
	
	for line in lines[1:]:
	    student_dict = {}

	    items = line.split(',')
	    first = items[0]
	    last = items[1]
	    email = items[2]
	    Year = items[3]
	    DOB = items[4]

	    student_dict['First'] = first
	    student_dict['Last'] = last
	    student_dict['Email'] = email
	    student_dict['DOB'] = DOB
	    student_dict['Class'] = Year
	    my_dicts.append(student_dict)
	return my_dicts


def mySort(data, col):
	sorted_students = sorted(data, key =  lambda x: x[col])
	that_student = sorted_students[0]
	return that_student['First'] + " " + that_student['Last']

def classSizes(data):
	senior_size = 0
	junior_size = 0
	sophomore_size = 0
	freshman_size = 0 
	for student in data:
		if student["Class"] == "Senior":
			senior_size += 1
		elif student["Class"] == "Junior":
			junior_size += 1
		elif student["Class"] == "Sophomore":
			sophomore_size += 1
		elif student["Class"] == "Freshman":
			freshman_size += 1
	class_size = [("Senior", senior_size), ("Junior", junior_size), ("Sophomore", sophomore_size), ("Freshman", freshman_size)]
	return sorted(class_size, key = lambda x: x[1], reverse = True)

def findMonth(a):
	birth_months = {}
	birth_occurances = []
	for x in a:
		birthday = x["DOB"].split("/")
		month = birthday[0]
		birth_occurances.append(month)
	for y in birth_occurances:
		if y not in birth_months:
			birth_months[y] = 0
		birth_months[y] += 1
	most_common = sorted(birth_months, key = lambda x: birth_months[x], reverse = True)
	return int(most_common[0])

def mySortPrint(a,col,fileName):
	sorted_students2 = sorted(a, key = lambda x: x[col]) # Same sort as mySort
	with open(fileName, "w") as e:
		filewriter = csv.writer(e, delimiter = "," ) # seperating by commas 
		for student in sorted_students2:
			filewriter.writerow([student["First"], student["Last"], student["Email"]])
	print("writing done")
	e.close()

def findAge(a):
	my_ages = []
	for x in a:
		dates = x["DOB"].split("/")
		year = dates[2]
		age = 2018 - int(year)
		my_ages.append(age)
	average_age = sum(my_ages)/len(my_ages)
	return round(average_age)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
	score = 0
	if got == expected:
		score = pts
		print(" OK ", end=" ")
	else:
		print (" XX ", end=" ")
	print("Got: ",got, "Expected: ",expected)
	return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
