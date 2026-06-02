

class Movie:
    def __init__(self,movie_id:int,name:str,duration_mins:int):
        self.movie_id=movie_id
        self.name=name 
        self.duration_mins=duration_mins
            

    def __repr__(self):
        return f"Movie(movie_id={self.movie_id},name={self.name})"