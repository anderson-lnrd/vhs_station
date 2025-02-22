import os
from colorama import Fore, Style
from typing import List, Optional
from .models import Movie

class MovieUI:
    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def wait_for_user(message: str = "Pressione Enter para continuar...") -> None:
        input(message)

    @staticmethod
    def display_program_title() -> None:
        MovieUI.clear_screen()
        print(Fore.CYAN + Style.BRIGHT + """
    ▚▞ █▬█ ▟▛ ▟▛ ▜▛ ▞▚ ▜▛ █ ██ ▛▟
        """)
        print(Fore.CYAN + Style.BRIGHT + "Bem-vindo ao VideoStoreApp!\n")

    @staticmethod
    def display_menu() -> None:
        print(Fore.GREEN + "1. Registrar um Filme")
        print(Fore.GREEN + "2. Listar Filmes")
        print(Fore.GREEN + "3. Editar Filme")
        print(Fore.GREEN + "4. Excluir Filme")
        print(Fore.RED + "5. Sair\n")

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def display_message(message: str, color: Optional[str] = None) -> None:
        if color:
            print(color + message)
        else:
            print(message)

    @staticmethod
    def display_movie(movie: Movie) -> None:
        print(Fore.CYAN + f"Título: {movie.title}")
        print(Fore.CYAN + f"Diretor: {movie.director}")
        print(Fore.CYAN + f"Ano: {movie.year}\n")

    @staticmethod
    def display_movies(movies: List[Movie]) -> None:
        if movies:
            for movie in movies:
                MovieUI.display_movie(movie)
        else:
            print(Fore.RED + "Nenhum filme registrado.\n")
            
    @staticmethod
    def display_movies_with_index(movies: List[Movie]) -> None:
        if movies:
            for idx, movie in enumerate(movies, start=1):
                print(Fore.CYAN + f"{idx}. {movie.title} ({movie.year}) - Direção: {movie.director}")
        else:
            print(Fore.RED + "Nenhum filme registrado.\n")

