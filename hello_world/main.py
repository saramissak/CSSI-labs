# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os
from model import Meme



# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

meme_img = {
    "dog" : {
                'name': 'Dog',
                'url':"https://i.kym-cdn.com/entries/icons/original/000/029/671/wide_dog_cover2_.jpg",
            },
    "long-neck-giraffee" : {
                'name': 'Long neck giraffee',
                'url': "http://www.freakingnews.com/pictures/78000/Giraffe-with-a-Very-Long-Neck--78020.jpg",
            },
    "girl-like-what" : {
                            'name': 'girl like what',
                            'url':"https://images.hellogiggles.com/uploads/2018/04/08115021/twitter-squinting-girl-meme-e1523213473157.jpg",
                        }
            }
added_img = {

}


class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')

        the_variable_dict = {
            "greeting": "Welcome",
            "adj": "meme",
            "meme_types": meme_img,
            "im_ur": "https://ww2.kqed.org/education/wp-content/uploads/sites/38/2019/03/tomemeornot3.jpg"
        }
        self.response.write(welcome_template.render(the_variable_dict))



class MemePage(webapp2.RequestHandler):
    def post(self):
        welcome_template = the_jinja_env.get_template('templates/results.html')

        checked = self.request.get("color")
        line1 = self.request.get("first-line")
        line2 = self.request.get("second-line")
        img_link = self.request.get("link-line")
        img_name = self.request.get("name-line")

        added_img['name']=img_name
        added_img['url']=img_link
        meme_img[img_name] = added_img
        meme_type = self.request.get("meme-type")
        img_url = meme_img[meme_type]['url']
        #add to database
        user_meme = Meme(line1 = line1, line2 = line2 , img_url = img_url, dark_mode=checked=="black")
        user_meme.put()

        meme_query = Meme.query()
        memes = meme_query.fetch()


        the_variable_dict = {
            "Line1": line1,
            "Line2": line2,
            "color": checked,
            "img_url": img_url,
            "all_memes": memes
        }
        self.response.write(welcome_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/memeresult', MemePage),

], debug=True)
