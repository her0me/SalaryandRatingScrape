In order to run the web scraping do the following:

1. Install python, making sure you also have pip
2. $ pip install beautifulsoup4
3. $ pip install requests
3. $ python -m pip install RateMyProfessorAPI
4. run whichever file you want.  salary.py will grab just the salary data.  rmp.py will grab the ratemyprofessor (rmp) data and the salary data automatically.  rmp.py requires the data from salary to search for professors on rmp.

$ python rmp.py 
or
$ python main.py

(make sure your terminal/powershell is in the correct directory)

Salary data:
-In order to get the Salary data into a csv make sure to uncomment the towards the bottom

Final data:
-This webscraping got the data close enough for me to just adjust the data myself, but I did have to patch it up a bit.  The main thing that happened is that a lot of the people in the payroll list aren't on ratemyprofessor, so I needed to delete all those people's records by hand.  Theoretically this could be done pretty easily with code too.  The idea would be to pass the payList back through and check it with the ratingList, then delete any element not found in the ratingList.

-You might also consider adding code to do other departments too!  I will watch for pull requests.