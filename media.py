import webbrowser
"""webbrowser is a pre-defined python function that provides
an interface to display html web-based documents to users"""

class Movie():
    """this class stores information relating to movies.
    Below are instances variables of the class Movie().
    __init__ is the constructor of the class and assigns
    values to the following instance variables"""
    def __init__(self, title, storyline, poster_image, youtube_trailer, rating):
       """self is the object being defined. Movies are listed
       in entertainment_center.py"""
       self.title = title
       self.storyline = storyline
       self.poster_image_url = poster_image
       self.trailer_youtube_url = youtube_trailer
       self.rating = rating
                    
    def show_trailer(self):
       """opens a movie trailer in a web browser"""
       webbrowser.open(self.youtube_trailer)
