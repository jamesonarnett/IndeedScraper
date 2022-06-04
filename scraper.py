import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    url = 'https://www.indeed.com/jobs?q=web%20developer&l=Remote&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'cardOutline')
    for item in divs:
        title = item.find('a').text
        company = item.find('span', class_ = 'companyName').text.strip()   
        try: 
            salary = item.find('span', class_ = 'salary-snippet-container').text.strip()
        except:
            salary = ''
        summary =  item.find('div', class_ = 'job-snippet').text.strip().replace('\n', "")

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return


joblist = []

for i in range(0, 40, 10):
    print(f'Getting Page - {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
