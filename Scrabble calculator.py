#create a dictionary of letters and their scores

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = { letters:points for letters, points in zip(letters, points) }
letter_to_points[""] = 0

# example dictionary players to words theyve played
player_to_words = {"player1": ["BLUE","TENNIS", "EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"] }

#function to score any word
##Add in triple word/double word/double letter/triple letter
def score_word(word):
  point_total = 0
  for letter in word:
    letter = letter.capitalize()
    point_total += letter_to_points.get(letter)
  return point_total

#function to play a word for a specific player
def play_word(player,word):
  current_game[player].append(word)

#function to say who just played a word
def recently_played(current_player):
  if current_player != "":
    print(current_player, "has just played a word")
    
#function to start playing words
def player_turn(current_game):
  print("Choose a player to play a word")
  for player in current_game.keys():
    print("-",player)
  player = input(">  ").capitalize()
  word = input("What word did they play? >  ")
  play_word(player,word)
  scores = update_point_totals(current_game)
  recently_played(player)
  continue_end(scores)
  return player 


#functions to add new players to a game
def add_single_player():
  new_player = (input("Enter player name: "))
  players[new_player] = []
  add_player = input("Would you like to add a new player? Y/N >  ")
  return add_player
  
players = {}
def add_players(players = players):
  add_player = add_single_player()
  while True:
    if add_player == "Y":
      add_player = add_single_player()
    else:
      return players
      
#function creating dictionary containing players and their point score
def update_point_totals(player_to_words = player_to_words):
  player_to_points = {}
  for player,words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)
  return player_to_points

#function to continue/end the game
def continue_end(scores):
  next_turn = input("Would you like to continue? Y/N >  ").capitalize()
  if next_turn == "Y":
    current_player = player_turn(current_game)
  else:
    print("Final scores are")
    print(scores)
    
current_game = add_players()
current_player = player_turn(current_game)



