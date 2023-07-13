import requests
import pandas as pd
import sqlalchemy as db
import os
import json 


def make_google_fitness_tracking_api_request():
    url = 'https://api.api-ninjas.com/v1/exercises'
    api_key = 'me7NFMjpZVgBax6mgRGN0g==JZ4C6IbPhz7NHl08'
    data = []
    offset = 0
    limit = 10
    total_items = 0

    while total_items < 30:
        params = {
            'offset': offset,
            'limit': limit
        }

        response = requests.get(url, headers={'X-Api-Key': api_key}, params=params)
        response_data = response.json()
        data.extend(response_data)
        total_items += len(response_data)
        offset += limit

        if len(response_data) < limit:
            break

    return data[:] 

def save_users_to_database(user_info, user_db):
    data_frame = pd.DataFrame(user_info, columns=['username', 'password'])
    engine = db.create_engine(f'sqlite:///{user_db}.db')
    with engine.connect() as connection:
        data_frame.to_sql('book_info_table', con=connection, if_exists='replace', index=False)

