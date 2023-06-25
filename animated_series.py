from bs4 import BeautifulSoup
import requests

# url = 'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=1000,&genres=animation&sort=user_rating,desc&start='+str(page)+'&ref_=adv_nxt'

headers = {'Accept-Language': 'en-US,en;q=0.8'} 

movie_name = []
year = []


for page in range(1,31):
    response = requests.get('https://www.imdb.com/search/title/?title_type=tv_series&num_votes=1000,&genres=animation&sort=user_rating,desc&'+'start='+str(page)+'&ref_=adv_nxt', headers=headers)


    soup = BeautifulSoup(response.text, "html.parser")

    movie_div = soup.find_all('div', class_='lister-item mode-advanced')


    for container in movie_div:
        #name of movie
        name = container.h3.a.text
        movie_name.append(name)

print(movie_name)
print(len(movie_name))