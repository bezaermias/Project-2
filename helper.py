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
    workouts = []  # List to store workout data
    for exercise in data['results']:
        workout = {
            'name': exercise['name'],
            'type': exercise['type'],
            'difficulty': exercise['difficulty'],
            'equipment': exercise['equipment'],
            'instructions': exercise['instructions'],
            'muscle': exercise['muscle'],
        }
        workouts.append(workout)
    return workouts

