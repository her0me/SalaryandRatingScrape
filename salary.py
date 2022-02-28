import requests
from bs4 import BeautifulSoup
import csv

class Salary:
    def __init__(self, payList):
        self.payList = payList
        self.grabData()
    
    def grabData(self):

        payList = self.payList

        # Making a GET request
        for p in range(5):
            print('https://www.umsalary.info/deptsearch.php?Dept=eecs&Year=0&page='+str(p+1))
            r = requests.get('https://www.umsalary.info/deptsearch.php?Dept=eecs&Year=0&page='+str(p+1))
            
            # Parsing the HTML
            soup = BeautifulSoup(r.content, 'html.parser')
            
            s = soup.find('table', class_='index')
            content = s.find_all('td')
            
            i = 3
            count = 0

            while i < len(content)-1:

                if i >= 3: 
                    text = content[i-3].text
                    lastName = text[:text.find(",")]
                    firstName = text[text.find(",")+2:]

                    if(firstName.find(" ") != -1):
                        firstName = firstName[:firstName.find(" ")]

                    payList.append([firstName, lastName, content[i].text[2:-3].replace(",", "", 1)]) 

                    #print(payList[count][0] + payList[count][1])
                    #print(payList[count][2])
                i+=5
                count+=1

        #uncomment these lines if you want the salary data to save in a csv
        #Details = ['First', 'Last', 'Salary']
        #count = 0
        #with open('salaries.csv', 'w', newline='') as f: 
            #write = csv.writer(f) 
            #if count == 0:
                #write.writerow(Details) 
            #write.writerows(payList) 
            #count += 1
        
        self = payList
