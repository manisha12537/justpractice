# import requests
# from bs4 import BeautifulSoup
# import pprint
# def scrap_movie():
#     data=requests.get("https://www.imdb.com/")
#     soup=BeautifulSoup(data.text,"html.parser")
#     main_div=soup.find_all("div",class_="ipc-sub-grid ipc-sub-grid--page-span-3 ipc-sub-grid--nowrap ipc-sub-grid--4-unit-at-s ipc-shoveler__grid")
#     movie_rank=main_div.find("span",class_="ipc-rating-star ipc-rating-star--baseAlt ipc-rating-star--imdb").text
#     print(movie_rank)
# scrap_movie





from bs4 import BeautifulSoup
import requests
import os.path
import json
import re
import pprint
def scrap_top_list():
    url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")
    main_div=soup.find_all("tbody",class_="lister-list")
    movie_ranks=[]
    movie_names=[]
    no_of_Reviews=[]
    movie_urls=[]
    movie_ratings=[]
    year_of_realease=[]
    for tr in main_div:
        for i in tr.find('tr')[1:]:
            movie_rank = tr.find("td", "titleColumn").text
            # movie_ranks.append(movie_rank)
            print(movie_rank)
    #         # print(movie_ranks)
    #         movie_name = i.find("a", class_="unstyled articleLink").text.strip() 
    #         # print(movie_name) 
    #         name=movie_name
    #         movie_name=re.split('(\d+)',name)
    #         year_of_realease.append(movie_name[-2])
    #         # print(year_of_realease)

    #         names=movie_name[0]
    #         namename=names.replace("(","")
    #         movie_names.append(namename)
    #         # print(movie_names)
            
    #         movie_review= i.find("td",class_="right hidden-xs").get_text()
    #         no_of_Reviews.append(movie_review)
    #         # print(no_of_Reviews)

    #         movie_rating = i.find("span",class_="tMeterScore").get_text()
    #         movie_ratings.append(movie_rating)
    #         # print(movie_rating)

    #         url=i.find("a",class_="unstyled articleLink")['href']
    #         movie_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"+url
    #         movie_urls.append(movie_url)
    #         # print(movie_url)
    
    # Top_Movies=[]
    # details={'position':'','Rating':'','Name':'','year':"",'url':'','movie_Reviews':''}
    # for i in range(0,len(movie_ranks)):
    #     details['position']=str(movie_ranks[i])
    #     details['Rating']=str(movie_ratings[i])
    #     details['Name']=str(movie_names[i])
    #     details['year']=str(year_of_realease[i])
    #     details['url']=movie_urls[i]
    #     details['movie_Reviews']=str(no_of_Reviews[i])
    #     Top_Movies.append(details.copy())
    # # with open("movies.json","w")as file:
    # #     data=json.dump(Top_Movies,file,indent=4)
    #     print(Top_Movies)
    #     return Top_Movies     
   
scrap_top_list()

