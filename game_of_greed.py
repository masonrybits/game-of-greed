from collections import Counter
import random
import re

class Game:

  def __init__(self,print_func=print, input_func=input):
    self._print = print_func
    self._input = input_func
  
  def play(self):
    self._print('Welcome to the Game of Greed')
    player_input = self._input('Wanna Play? Please enter "y" to play.')
    if player_input == 'y':
      self._print('Great! Check back tomorrow :D')
    else:
      self._print('OK. Maybe another time')

  def calculate_score(self, dices):
    count = Counter(dices)

    if count[1] == 2 and count[5] == 4:
      return 2000

    if len(count) == 6:
      return 1500

    if len(count) == 3 and count.most_common()[2][1] == 2:
      return 1500

    score = 0

    for dice in count:
      if count[1] > 2:
        score += ((count[1]-2)*1000)
      elif count[dice] > 2:
        score += ((count[dice]-2)*100) * dice
      elif dice == 1:
        score += count[dice] * 100
      elif dice == 5:
        score += count[dice] * 50

    return score

  def _do_roll(self):
    rolls = [random.randint(1,6) for _ in range(6)]

  def _set_aside(self):
    player_input = self._input('Enter dice to keep: ')
    inputs = re.findall(r"[1-6]", player_input)
    return inputs
  

if __name__ == "__main__":
    g = Game()
    g.play()
    print(g._set_aside())
   