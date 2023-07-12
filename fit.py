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
    # print(data)
    return data

# def extract_fitness_exercises(data):
#     exercise_info = []
#     for item in data:
#         name = item['name']
#         difficulty = item['difficulty']
#         equipment = item['equipment']
#         exercise_info.append((name,difficulty, equipment))
#     print(exercise_info)
#     return exercise_info




# print (data)
# if 'items' not in data:
#     print("Invalid fitness.")
#     exit()

# print (fit_info)
# save_fittness_tracking_to_database(fit_info, 'fit_database')

# sort_option = input("Sort by (publication/rating): ")
# retrieve_tracking_info = retrieve_from_database('fit_database', sort_option)
# display_tracking()
