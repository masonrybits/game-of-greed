from collections import Counter

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

    if count[1] == 1 and count[2] == 1 and count[3] == 1 and count[4] == 1 and count[5] == 1 and count[6] == 1:
      return 1000

    if len(count) == 3 and count.most_common(3)[1] == 2 and count.most_common(3)[2] == 2 and count.most_common(3)[3] == 2:
      return 1500

    score = 0
    for dice in count:
      if count[dice] > 2:
        score += ((count[dice]-2)*100) * dice
      elif dice == 1:
        score += count[dice] * 100
      elif dice == 5:
        score += count[dice] * 50

    return score


if __name__ == "__main__":
    g = Game()
    g.play()
    dices = [1,1,2,2,4,5]
    print(g.calculate_score(dices))