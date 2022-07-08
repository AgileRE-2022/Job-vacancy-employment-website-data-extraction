# Job-vacancy-employment-website-data-extraction
A Job Vacancy / Employment website data extraction using django

Text Scrapping on Linkedin to find Jobs related to Information Systems and Relevant Keyword and Topic for Each Job using Django Python selenium and LDA Topic Modelling

# Prerequisites
1. Python
2. Django
3. numpy, pandas, regex, selenium, bs4, parsel, gensim, nltk library must be installed 

# Installation
1. Clone the Repositories
2. Edit file Parameter.py in folder scraping, change the email and password to your email and password used for login in linkedin

# How to Use
1. open terminal in project directories and run "python manage.py runserver"
2. Access http://127.0.0.1:8000/scraping
![image](https://user-images.githubusercontent.com/76902001/178029644-74cd13a8-a668-4cfe-9dda-3f90918e0dfa.png)
3. First click Data Button, it will run the scrapping process. You might run to some error "Selenium can't determine loading " you might have to refresh the page
![image](https://user-images.githubusercontent.com/76902001/178029755-711653d8-f0f1-46cc-8a89-448670850c3e.png)
4. To see the result click data from scraping button
![image](https://user-images.githubusercontent.com/76902001/178029557-2936de6b-4846-4ab1-806b-ab493de69020.png)
5. To See the relevant topic and keyword for each job listing click on Topic Modelling Result Button
![image](https://user-images.githubusercontent.com/76902001/178030919-d2dc4777-70db-4d8e-950f-bf4b93cadafb.png)
