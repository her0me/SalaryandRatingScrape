import requests
import csv
from salary import Salary
import ratemyprofessor
from bs4 import BeautifulSoup

payList = []
salary = Salary(payList)
school = ratemyprofessor.get_school_by_name("University of Michigan")
ratingList = []

for data in salary.payList:
    
    professor = ratemyprofessor.get_professor_by_school_and_name(school, data[0] + " " + data[1])

    if professor is not None:
        print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
        if professor.school.name == "University of Michigan" :
            ratingList.append([professor.name, professor.rating])

            print("Rating: %s / 5.0" % professor.rating)
            print("Difficulty: %s / 5.0" % professor.difficulty)
            print("Total Ratings: %s" % professor.num_ratings)
            if professor.would_take_again is not None:
                print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
            else:
                print("Would Take Again: N/A")
        else:
            print("Doesn't work at UM")

Details = ['Name', 'Rating']
with open('ratings.csv', 'w', newline='') as f: 
    write = csv.writer(f) 
    write.writerow(Details) 
    write.writerows(ratingList) 
    
