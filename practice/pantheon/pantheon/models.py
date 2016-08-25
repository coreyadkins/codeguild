"""pantheon Models."""

import csv


with open('pantheon/pantheon.tsv') as csvfile:
    pantheon_reader = csv.DictReader(csvfile, delimiter= '\t')
    people = [person for person in pantheon_reader]

print(people)
