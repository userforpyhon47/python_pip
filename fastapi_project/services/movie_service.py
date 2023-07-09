from config.database import Session
from models.movie import Movie


class MovieService():
    """Class to implemet DB session service"""
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_movies(self):
        return self.db.query(Movie).all()
    
    def get_movie(self, id):
        return self.db.query(Movie).filter(Movie.id==id).first()
    
    def query_movie(self, category):
        return self.db.query(Movie).filter(Movie.category.contains(category.lower())).all()
    
    def create_movie(self, movie):
        movie_data = movie.dict() # convert model to dict
        movie_data.pop("id") # pop autoincrement primary key
        new_movie = Movie(**movie_data) # Creates an instance with the database Movie table model, receives **kwargs
        self.db.add(new_movie) # Simply add to Movie table model the new created movie
        self.db.commit() # save the changes to the DB
        return True
    
    def delete_movie(self, id):
       movie_instance = self.db.query(Movie).filter(Movie.id==id).first()
       if not movie_instance:
           return Exception(f"movie by id {id}")
       self.db.delete(movie_instance)
       self.db.commit()

    def update_movie(self, id, movie: Movie):
        movie_instance = self.db.query(Movie).filter(Movie.id==id).first()
        if not movie_instance:
            return Exception(f"movie by id {id}")
        movie_instance.title = movie.title
        movie_instance.overview = movie.overview
        movie_instance.year = movie.year
        movie_instance.rating = movie.rating

        self.db.commit() # Commit changes to db