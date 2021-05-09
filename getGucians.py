#/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import pandas

source1 = requests.get( 'https://commits.top/egypt.html').text
soup = BeautifulSoup(source1, 'lxml')

name = []  
link = []
followers = []

for user_name in soup.find('tbody').find_all('a'):
        
            try:
                git_link = f'https://github.com/{user_name.text}'
                
                # give access to github link
                source2 = requests.get(git_link).text

                soup2 = BeautifulSoup(source2, 'lxml')

                check_uni = soup2.find('span', class_= 'p-org').text
                if ("German University" in check_uni):
                    # listing users' names
                    print(user_name.text)
                    name.append(user_name.text)
                    
                    # listing github links
                    link.append(git_link)

                    num_of_followers = soup2.find('span', class_= 'text-bold color-text-primary').text
                
                    # listing the number of followers
                    followers.append(num_of_followers)
            except:
                continue
        

df = pandas.DataFrame({'Name':name, 'Github link':link, 'Number of followers':followers})
df.to_csv('GithubGuciansData.csv', index = False, encoding = 'utf-8')