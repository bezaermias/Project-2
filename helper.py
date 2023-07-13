import requests
import pandas as pd
import sqlalchemy as db
import os
import json 


def make_google_fitness_tracking_api_request():
    muscle = 'biceps'
    url = 'https://api.api-ninjas.com/v1/exercises?muscle{}'.format(muscle) 
    response = requests.get(url, headers={'X-Api-Key': 'me7NFMjpZVgBax6mgRGN0g==JZ4C6IbPhz7NHl08'})
    data = response.json()
    
    workouts = []  
    for exercise in data:
        workout = {
            'name': exercise['name'],
            'type': exercise['type'],
            'difficulty': exercise['difficulty'],
            'equipment': exercise['equipment'],
            'instructions': exercise['instructions'],
            'muscle': exercise['muscle'],
        }
        work= workouts.append(exercise)
    return work

def save_users_to_database(user_info, user_db):
    data_frame = pd.DataFrame(user_info, columns=['username', 'password'])
    engine = db.create_engine(f'sqlite:///{user_db}.db')
    with engine.connect() as connection:
        data_frame.to_sql('book_info_table', con=connection, if_exists='replace', index=False)

