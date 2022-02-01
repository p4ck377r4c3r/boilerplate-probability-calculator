import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    for color, times in kwargs.items():
      while times > 0:
        self.contents.append(color)
        times -= 1

  def draw (self, num):
    if num > len(self.contents):
      return self.contents
    else:
      drawn = []
      while num > 0:
        index = random.randint(0, len(self.contents)-1)
        drawn.append(self.contents[index])
        del self.contents[index]
        num -= 1
    
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num = 0
  matches = 0
  while num < num_experiments:

    hat_copy = copy.deepcopy(hat)

    drawn = hat_copy.draw(num_balls_drawn)
    drawn_balls = {}
    for color in drawn:
      if drawn_balls.get(color) == None:
        drawn_balls[color] = 1
        continue
      drawn_balls[color] += 1

    match = True
    for ball,times in expected_balls.items():
      if drawn_balls.get(ball) == None or drawn_balls[ball] < times:
        match = False
        break

    if match:
      matches += 1
    
    num += 1
   
  return matches/num_experiments
