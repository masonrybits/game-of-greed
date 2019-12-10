from game_of_greed import Game

def test_play_yes():
  prints = ['Welcome to the Game of Greed', 'Great! Check back tomorrow :D']
  prompts = ['Wanna Play? Please enter "y" to play.']
  response = ['y']

  def print_for_testing(message):
        if len(prints):
            assert message == prints.pop(0)

  def input_for_testing(prompt):
        if len(prompts):
            assert prompt == prompts.pop(0)
            return response.pop(0)

  player = Game(print_for_testing, input_for_testing)

  player.play()

def test_play_no():
  prints = ['Welcome to the Game of Greed', 'OK. Maybe another time']
  prompts = ['Wanna Play? Please enter "y" to play.']
  response = ['n']

  def print_for_testing(message):
        if len(prints):
            assert message == prints.pop(0)

  def input_for_testing(prompt):
        if len(prompts):
            assert prompt == prompts.pop(0)
            return response.pop(0)

  player = Game(print_for_testing, input_for_testing)

  player.play()