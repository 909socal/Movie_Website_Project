import webbrowser



#Class movie that is used to for my instant variables in entertainment.py file

class Movie():

    #Constructor used for Class Movie to call the instant variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #Instant methid used to show trailers    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
                    
