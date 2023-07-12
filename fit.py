import requests
import pandas as pd
import sqlalchemy as db
import os
import json 


def make_google_fitness_tracking_api_request():
    muscle = 'biceps'
    url = 'https://api.api-ninjas.com/v1/exercises?muscle{}'.format(muscle) 
    response = requests.get(url, headers={'X-Api-Key': 'me7NFMjpZVgBax6mgRGN0g==JZ4C6IbPhz7NHl08'})
    # response = requests.get(url,  headers={'X-Api-Key': 'me7NFMjpZVgBax6mgRGN0g==JZ4C6IbPhz7NHl08'})
    data = response.json()
    print(data)
    return data

# def extract_fitness_type(data):
#     fit_info = []
#     unique_fitness = set()
#     for item in data['items']:
#         title = item['muscle']['name']
#         lowercase_title = title.lower()
#         published_date = item['muscle'].get('type', 'Unknown')
#         average_rating = item['muscle'].get('averageRating', 0)  
#             unique_titles.add(lowercase_title)
#             fit_info.append((title, published_date, average_rating))
#     # Convert the title to lowercase for case-insensitive uniqueness check
#     return fit_info

# def save_fittness_tracking_to_database(fit_info, fit_database):
#     data_frame = pd.DataFrame(fit_info, columns=['fit_type', 'water', 'yoga'])
#     engine = db.create_engine(f'sqlite:///{fit_database}.db')
#     with engine.connect() as connection:
#         data_frame.to_sql('fit_info_table', con=connection, if_exists='replace', index=False)

# def retrieve_from_database(fit_database, sort_by):
#     engine = db.create_engine(f'sqlite:///{fit_database}.db')
#     with engine.connect() as connection:
#         if sort_by == 'publication':
#             query = "SELECT * FROM fit_info_table ORDER BY published_date DESC"
#         elif sort_by == 'rating':
#             query = "SELECT * FROM fit_info_table ORDER BY average_rating DESC"
#         else:
#             query = "SECRET * FROM fit_info_table "

#         query_result= connection.execute(db.text(query)).fetchall()

#         return db.DataFrame(query_result)

data = make_google_fitness_tracking_api_request()
print (data)
# if 'items' not in data:
#     print("Invalid fitness.")
#     exit()

# fit_info = extract_fittness_type(data)
# save_fittness_tracking_to_database(fit_info, 'fit_database')

# sort_option = input("Sort by (publication/rating): ")
# retrieve_tracking_info = retrieve_from_database('fit_database', sort_option)
# display_tracking()
