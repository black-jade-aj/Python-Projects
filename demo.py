#first_name = 'judith'
#last_name = 'smith'
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1} '.format(first_name, last_name)
#print(first_name + ' ' + last_name)
#Only available in Python 3.6 and above
print(output)
#{0} and {1} are placeholders for the first_name and last_name variables, respectively. The f-string allows for easier formatting of strings by directly embedding expressions inside string literals.