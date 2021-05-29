# Web_Scrapping_challenge
WebScraping Homework

Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

See: Mission_to_Mars.ipynb

Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data. Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function. Store the return value in Mongo as a Python dictionary. Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data. Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

Please review the following documents: scrap_mars.py, index.html, app.py Mission_to_Mars.ipynb SCREEN PRINT: available at capture.png

To view: Your site is published at 

SUMMARY: Was able to work through all the various issues and publish a working site! I am still unable to understand why I cannot reset the index of the dataframe. This was the core error that continued to plague me. I had to comment out: mars_df.set_index(0, inplace=True) and replace it with mars_df.index.drop mars_df.index.names= [None] mars_df.columns= ['Compare', 'Mars', 'Earth'] to get the site to function. I will bring this up in office hours to figure out what is the heart of the issue.

Additionally, if you want to review the multiple versions of code I tried / copied / re-wrote / mutilated. please review the contents of the ATTEMPTS folder.

About
WebScraping Homework

Resources
 Readme
Releases
No releases published
Packages
No packages published
Environments 1
 github-pages Active
Languages
Jupyter Notebook
58.2%
 
Python
23.9%
 
HTML
17.7%
 
CSS
0.2%
