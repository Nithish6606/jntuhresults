import requests
from bs4 import BeautifulSoup

# URL of the JNTUH results page
url = 'https://jntuh.ac.in/results/result'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the form element that contains the search form
form = soup.find('form', {'name': 'frmresults'})

# Find the select element that contains the list of courses
select = form.find('select', {'name': 'ddlcourse'})

# Find all the option elements within the select element
options = select.find_all('option')

# Print the list of courses
print('Courses:')
for option in options:
    print(option.text)

# Prompt the user to enter their hall ticket number
hall_ticket = input('Enter your hall ticket number: ')

# Prompt the user to select a course from the list
course = input('Enter the course code: ')

# Create a payload with the user's input
payload = {
    'ddlcourse': course,
    'txtregno': hall_ticket,
    'btnviewresults': 'View Results'
}

# Send a POST request to the URL with the payload
response = requests.post(url, data=payload)

# Parse the HTML content of the results page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div element that contains the results table
results_div = soup.find('div', {'id': 'div1'})

# Find the table element within the div element
table = results_div.find('table')

# Find all the tr elements within the table element
rows = table.find_all('tr')

# Print the results
print('Results:')
for row in rows:
    cells = row.find_all('td')
    if cells:
        print(cells[0].text, cells[1].text)
