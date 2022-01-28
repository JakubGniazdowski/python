
def print_even(test_string) :
	for i in test_string:
		if i == "geeks":
			yield i

test_string = " The are many geeks around you, \
			geeks are known for teaching other geeks"


count = 0
print ("The number of geeks in string is : ", end = "" )
test_string = test_string.split()

for j in print_even(test_string):
	count = count + 1

print (count)
