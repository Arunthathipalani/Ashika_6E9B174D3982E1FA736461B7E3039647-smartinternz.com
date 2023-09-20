class Player:
  def Play(self):
    print("the player is playing cricket.")
    
class Batsman(Player):
  def play(self):
    print("the batsman is batting.")
    
class Bowler(Player):
  def play(self):
    print("the bowler is bowling.")
    
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()
