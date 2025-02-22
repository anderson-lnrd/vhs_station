import sys
from colorama import Fore
from .repository import VideoStoreRepository
from .ui import MovieUI
from .models import Movie

class VideoStoreApp:
    def __init__(self) -> None:
        self.repository = VideoStoreRepository()
        self.ui = MovieUI()

    def run(self) -> None:
        while True:
            self.ui.display_program_title()
            self.ui.display_menu()
            self.handle_option()

    def handle_option(self) -> None:
        try:
            option = int(self.ui.get_input(Fore.YELLOW + "Escolha uma opção: "))
        except ValueError:
            self.ui.display_message("\nOpção inválida. Por favor, digite um número.\n", Fore.RED)
            self.ui.wait_for_user()
            return

        if option == 1:
            self.register_movie()
        elif option == 2:
            self.list_movies()
        elif option == 3:
            self.edit_movie()
        elif option == 4:
            self.delete_movie()
        elif option == 5:
            self.exit_app()
        else:
            self.ui.display_message("\nOpção inválida. Por favor, escolha uma opção válida.\n", Fore.RED)
            self.ui.wait_for_user()

    def register_movie(self) -> None:
        self.ui.clear_screen()
        print(Fore.BLUE + "\n--- Registrar um Novo Filme ---")
        title = self.ui.get_input("Digite o título do filme: ").strip()
        director = self.ui.get_input("Digite o nome do diretor: ").strip()
        year = self.ui.get_input("Digite o ano de lançamento: ").strip()
        movie = Movie(title, director, year)
        self.repository.add_movie(movie)
        self.ui.display_message(f"\nFilme '{title}', dirigido por {director} ({year}), registrado com sucesso!\n", Fore.GREEN)
        self.ui.wait_for_user()

    def list_movies(self) -> None:
        self.ui.clear_screen()
        print(Fore.BLUE + "\n--- Lista de Filmes ---\n")
        movies = self.repository.list_movies()
        self.ui.display_movies(movies)
        self.ui.wait_for_user()

    def edit_movie(self) -> None:
        self.ui.clear_screen()
        movies = self.repository.list_movies()
        if not movies:
            self.ui.display_message("Nenhum filme disponível para edição.", Fore.RED)
            self.ui.wait_for_user()
            return
        
        self.ui.display_movies_with_index(movies)
        try:
            choice = int(self.ui.get_input("\nDigite o número do filme a ser editado: ")) - 1
            if 0 <= choice < len(movies):
                selected_movie = movies[choice]
                new_title = self.ui.get_input(f"Novo título [{selected_movie.title}]: ") or selected_movie.title
                new_director = self.ui.get_input(f"Novo diretor [{selected_movie.director}]: ") or selected_movie.director
                new_year = self.ui.get_input(f"Novo ano [{selected_movie.year}]: ") or selected_movie.year
                updated_movie = Movie(new_title, new_director, new_year)
                self.repository.edit_movie(selected_movie.title, updated_movie)
                self.ui.display_message(f"\nFilme '{selected_movie.title}' editado com sucesso!\n", Fore.GREEN)
            else:
                self.ui.display_message("Número inválido.", Fore.RED)
        except ValueError:
            self.ui.display_message("Por favor, insira um número válido.", Fore.RED)
        
        self.ui.wait_for_user()


    def delete_movie(self) -> None:
        self.ui.clear_screen()
        movies = self.repository.list_movies()
        if not movies:
            self.ui.display_message("Nenhum filme disponível para exclusão.", Fore.RED)
            self.ui.wait_for_user()
            return

        # Mostrar filmes com índice
        self.ui.display_movies_with_index(movies)
        try:
            choice = int(self.ui.get_input("\nDigite o número do filme a ser excluído: ")) - 1
            if 0 <= choice < len(movies):
                selected_movie = movies[choice]
                self.repository.remove_movie(selected_movie.title)
                self.ui.display_message(f"\nFilme '{selected_movie.title}' excluído com sucesso!\n", Fore.GREEN)
            else:
                self.ui.display_message("Número inválido.", Fore.RED)
        except ValueError:
            self.ui.display_message("Por favor, insira um número válido.", Fore.RED)
        
        self.ui.wait_for_user()


    def exit_app(self) -> None:
        self.ui.clear_screen()
        self.ui.display_message("Encerrando a aplicação...", Fore.MAGENTA)
        sys.exit()
