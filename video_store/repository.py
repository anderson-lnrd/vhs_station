from typing import List, Optional
from .models import Movie

class VideoStoreRepository:
    def __init__(self) -> None:
        self.movies: List[Movie] = [
            Movie("Um sonho de liberdade", "Frank Darabont", "1994"),
            Movie("O Poderoso Chefão", "Francis Ford Coppola", "1972"),
            Movie("Pulp Fiction", "Quentin Tarantino", "1994"),
            Movie("O Cavaleiro das Trevas", "Christopher Nolan", "2008"),
            Movie("Matrix", "Lana Wachowski", "1999")
        ]

    def add_movie(self, movie: Movie) -> None:
        self.movies.append(movie)

    def list_movies(self) -> List[Movie]:
        return self.movies

    def find_movie_index(self, title: str) -> Optional[int]:
        for index, movie in enumerate(self.movies):
            if movie.title.lower() == title.lower():
                return index
        return None

    def remove_movie(self, title: str) -> bool:
        index = self.find_movie_index(title)
        if index is not None:
            self.movies.pop(index)
            return True
        return False

    def edit_movie(self, title: str, new_movie: Movie) -> bool:
        index = self.find_movie_index(title)
        if index is not None:
            self.movies[index] = new_movie
            return True
        return False
