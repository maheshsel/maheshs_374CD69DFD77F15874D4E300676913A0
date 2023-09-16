'''Implement a class called player that represents a cricket  player.the player class should have a
method called play() which prints" the player.Derive a two classes batsman and 
bowler , from the  players class. override the play() method in each derived class to print "the batsman
is batting" and "the bowler is blowing", respectively. creat a program to create subject or both the
batsman and bowler classes and call the play() method for each object.'''


# Define the base class player
class Player:
      def play(self):
          print ("the player is playing cricket.")

  # Define the base class batsman
class Batsman(Player):
      def play(self):
          print(" the batsman is batting.")

#Define the derived class bowler
class Bowler(Player):
      def play(self):
          print("the bowler is bowling.")

#creat object of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()