from google.appengine.ext import ndb

class Meme(ndb.Model):
    line1 = ndb.StringProperty()
    line2 = ndb.StringProperty()
    img_url = ndb.StringProperty()
    dark_mode = ndb.BooleanProperty()

    def getLines(self):
        return self.line1 + " " + self.line2
