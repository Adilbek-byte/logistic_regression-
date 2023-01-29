import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://bookdown.org/tpinto_home/Regression-and-Classification/logistic-regression.html'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the data
table = soup.find('table')

# Extract the data from the table
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Store the data in a file or database for future use
with open('data.csv', 'w') as file:
    for row in data:
        file.write(','.join(row) + '\n')
