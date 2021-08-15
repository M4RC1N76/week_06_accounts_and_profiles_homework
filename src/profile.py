class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_favourite(self, movie):
        self.favourites.append(movie)

    def remove_favourite(self, movie):
        self.favourites.remove(movie)

    def get_favourites(self):
        return self.favourites
        #my idea overcomplicateds and not working -- my idea wrong
        #self.favourites.list_of_favourite_movies(profile_1) -- wrong