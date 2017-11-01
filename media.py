import webbrowser


###############################################################################
###Parent class, takes in media title, storyline, and rating. Contains class###
###method that checks ratings to make sure they are valid otherwise returns ###
###an error: 'ERROR: RATING NOT VALID'.                                     ###
###############################################################################

class Media():
    def __init__(self, title, storyline,
                rating):
                self.title = title
                self.storyline = storyline
                self.rating = rating
                ALLOWEDRATINGS = ['G', 'PG', 'PG13', 'R', 'M', 'Not Rated']
                if self.rating not in ALLOWEDRATINGS:
                    self.rating = 'ERROR: RATING NOT VALID'
###############################################################################
###Child class TVShow.  Takes in title, storyline, rating, seasons, episodes###
###and episode_length length parameters.  This is child to Media, is only   ###
###for television shows.                                                    ###
###############################################################################

class TVShow(Media):
    def __init__(self, title, storyline, rating,
                seasons, episodes, episode_length):
                Media.__init__(self, title, storyline, rating)
                self.seasons = seasons
                self.episodes = episodes
                self.episode_length = episode_length
                TYPE = "TV Show"
################################################################################
###Child class Movie is child of Media.  Takes parameters title, storyline,  ###
###poster_image(url), trailer_youtube(url).Contains class method play_trailer###
### play_trailer, which opens the trailer URL in brower, in practice is only ###
### a method for testing our URL.                                            ###
################################################################################

class Movie(Media):
    """This class stores movie data as: media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)"""
    def __init__(self, title, storyline, rating,
                poster_image, trailer_youtube, duration):
                 Media.__init__(self, title, storyline, rating)
                 self.poster_image_url = poster_image
                 self.trailer_youtube_url = trailer_youtube
                 self.duration = duration
                 TYPE = "Feature Film"

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
