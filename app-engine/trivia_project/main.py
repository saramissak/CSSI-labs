import webapp2
import jinja2
import os

from google.appengine.api import urlfetch
import json
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Trivia Game </h1>')
        trivial_url_endpoint = "https://opentdb.com/api.php?amount=15&category=12&difficulty=medium&type=multiple"
        response = urlfetch.fetch(trivial_url_endpoint).content

        responses_as_json = json.loads(response)
        for i in range(len(responses_as_json['results'])):
            first_result = responses_as_json['results'][i]
            question = first_result['question']
            correct_answer = first_result['correct_answer']
            incorrect_answers = first_result['incorrect_answers']
            all_answers =[]
            all_answers.append(incorrect_answers[0])
            all_answers.append(incorrect_answers[1])
            all_answers.append(incorrect_answers[2])
            all_answers.append(correct_answer)
            random.shuffle(all_answers)

            self.response.write('<h3>' + question + '</h3>')
            for k in all_answers:
                self.response.write('<br>' + k + '<br>')

            self.response.write('<button onclick="document.getElementById(\'correct\').style.visibility = \'visible\';">Click me for answer</button>')
            self.response.write('<p  style="visibility: hidden;" id="correct">'+ correct_answer+'</p>')

class GiphyPage(webapp2.RequestHandler):
    def get(self):
        api_key = '3DOZUnqc7qtK003xSpYX4HaDf6V9XJAk'
        giphy_endpoint_url = 'http://api.giphy.com/v1/gifs/search?api_key=3DOZUnqc7qtK003xSpYX4HaDf6V9XJAk&q=doggie'
        result = urlfetch.fetch(giphy_endpoint_url).content
        result_as_json = json.loads(result)
        url = result_as_json['data'][0]['images']['original']['url']
        self.response.write('<img src='+url+'>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/giphy', GiphyPage)
], debug=True)
