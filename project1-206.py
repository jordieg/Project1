import os
import filecmp
from dateutil.relativedelta import *
import datetime


#Input: file name
def getData(file):
	# get a list of dictionary objects from the file
	inFile = open(file, 'r')
	lines = inFile.readlines()
	inFile.close()

	dictList = []

	for line in lines:

		dataDict = {}

		# split at first ,
		values = line.split(",")
		firstName = values[0]
		lastName = values[1]
		email = values[2]
		year = values[3]
		birth = values[4]

		# set up dictionart
		dataDict["First"] = firstName
		dataDict["Last"] = lastName
		dataDict["Email"] = email
		dataDict["Class"] = year
		dataDict["DOB"] = birth
		dictList.append(dataDict)

	#Ouput: return a list of dictionary objects where
	return dictList


#Input: list of dictionaries and col (key) to sort on
def mySort(data, col):
	# Sort based on key/column
	sortedList = sorted(data, key=lambda k: k[col], reverse = False)
	
	#Output: Return the first item in the sorted list as a string of just: firstName lastName
	retourner = sortedList[0]
	name = retourner['First'] + " " + retourner['Last']
	return name


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	freshman_count = 0
	sophomore_count = 0
	junior_count = 0
	senior_count = 0

	for dictionnaire in data:
		if dictionnaire["Class"] == 'Freshman':
			freshman_count += 1
		if dictionnaire["Class"] == 'Sophomore':
			sophomore_count += 1
		if dictionnaire["Class"] == 'Junior':
			junior_count += 1
		if dictionnaire["Class"] == 'Senior':
			senior_count += 1

	tup = [('Senior', senior_count), ('Junior', junior_count), ('Sophomore', sophomore_count), ('Freshman', freshman_count)]
	sortedTup = sorted(tup, key=lambda k: k[1], reverse = True)
	return sortedTup


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	month_count = {
		'1': 0,
		'2': 0,
		'3': 0,
		'4': 0,
		'5': 0,
		'6': 0,
		'7': 0,
		'8': 0,
		'9': 0,
		'10': 0,
		'11': 0,
		'12': 0
	}

	for dictionnaire in a:
		birth = dictionnaire['DOB']
		values = birth.split("/")
		month = values[0]
		if month in month_count:
			month_count[month] = month_count[month] + 1

	max_month = max(month_count, key=lambda k: month_count[k]) #should it be 1?
	return int(max_month)

def mySortPrint(a, col, fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outFile = open(fileName, 'w')

	sortedList = sorted(a, key=lambda k: k[col], reverse = False)
	for item in sortedList:
		if item["Email"] != "Email":
			outFile.write(item["First"] + "," + item["Last"] + "," + item["Email"] + "\n")
	outFile.close()


def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	age_list = []
	current = datetime.datetime.now()

	for dictionnaire in a:
		if dictionnaire["DOB"] != 'DOB\n':
			birth = dictionnaire['DOB']
			values = birth.split('/')
			month = values[0]
			day = values[1]
			year = values[2]

			birthdate = datetime.date(int(year), int(month), int(day))
			age = relativedelta(current, birthdate).years
			age_list.append(age)

	total = 0
	for item in age_list:
		total += age_list[item]

	average = total/(len(age_list))
	return int(average)

	


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
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
	data2 = getData('P1DataB2.csv')
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
