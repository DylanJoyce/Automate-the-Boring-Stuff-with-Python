#!/usr/bin/env python

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	print('Enter a name: (blank to quit)')
	name = raw_input()
	if name == '':
		break

	if name in birthdays:
		print('%s is the birthday of %s.' %(birthdays[name], name))
	else:
		print('I do not have birthday information for %s.' %name)
		print('What is their birthday?')
		birthday = raw_input()
		birthdays[name] = birthday
		print('The birthday database is updated.')