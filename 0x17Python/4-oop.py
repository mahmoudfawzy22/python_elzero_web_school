class Games:
    
    def __init__(self, name) :
         self.game = name

    def show_games(self) :
            if isinstance(self.game, list) :
                print("I Have Many Games: ")

                for games in self.game :
                    print(f"-- {games}")
            elif str(self.game).isdigit() :
                 print(f"I Have {self.game} Game")

            else :
                print(f"I Have One Game Called {self.game}")
            

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.