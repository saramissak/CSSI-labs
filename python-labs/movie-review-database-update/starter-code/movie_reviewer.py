#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

nemo = {
    "title": "finging nemo",
    "id": "tt0266543",
    "year_released": 2003,
    "rating": "G",
    "score": 8.1,
    "reviews": 873104,
    "genre": ['animation','comedy','adventure']
}

ratatouille = {
    "title": "ratatouille",
    "id": "tt0382932",
    "year_released": 2007,
    "rating": "G",
    "score": 8.0,
    "reviews": 583870,
    "genre": ['animation','comedy','adventure']
}

movies = [inside_movie, nemo, ratatouille]
inside_movie["score"] = 8.2
inside_movie['reviews']= 541305
inside_movie['year_released']= 2015
inside_movie.pop("out_of")
inside_movie['genre'] = ['animation','comedy','adventure']

picked_genre = raw_input("What genre would you like? ")
with_genre = []
for i in range(len(movies)):
    movie = movies[i]
    if picked_genre in movie['genre']:
        with_genre.append(movie)

max = with_genre[0]
for next in with_genre:
    if next["score"] > max["score"]:
        print('test')
        max = next


print("The movie with the highest rating is: " + max['title'])
