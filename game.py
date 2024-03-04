import pyttsx3 
engine = pyttsx3.init()

def weapon_room():
  user_input = ""
  print("Options: left/backward")
  engine.say("Options: left or backward")
  engine.runAndWait()
  user_input = input().lower()
  if user_input == "left":
    print("Your game restarts")
    engine.say("Your game restarts")
    engine.runAndWait()
    introScene()
  elif user_input == "backward":
    print("You got a weapon")
    engine.say("You got a weapon")
    engine.runAndWait()
    print("You win weapon so ")
    engine.say("You win weapon so ")
    engine.runAndWait()
    print("The door opens .")
    engine.say("The door opens .")
    engine.runAndWait()
  else: 
    print("Please enter a valid option for the adventure game.")
    engine.say("Please enter a valid option for the adventure game.")
    engine.runAndWait()
  

def haunted_room():
  user_input = ""
  print("Your are at dark room")
  engine.say("Your are at dark room")
  engine.runAndWait()
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  engine.say("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  engine.runAndWait()

  print("Options: right/backward")
  engine.say("Options: right or backward")
  engine.runAndWait()

  user_input = input().lower()
  
  if user_input == "right":
    print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
    engine.say("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
    engine.runAndWait()
    quit()
  elif user_input == "backward":
    print("You got a key of weapon room")
    engine.say("You got a key of weapon room")
    weapon_room()
  else:
    print("Please enter a valid option for the adventure game.")
    engine.say("Please enter a valid option for the adventure game.")
    engine.runAndWait()


def backward_room():
  print("You find that this door opens into a wall.")
  engine.say("You find that this door opens into a wall.")
  engine.runAndWait()
  print("YOU LOST!")
  engine.say("YOU LOST!")
  engine.runAndWait()

def forward_room():
  user_input = ""
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  engine.say("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  engine.runAndWait()
  print("Options: right or left or forward or backward")
  engine.say("right or left or forward or backward")
  engine.runAndWait()
  user_input = input().lower()
  if user_input == "left":
    print("There is a Monstar!")
    engine.say("There is a Monstar!")
    engine.runAndWait()
    print("You dead")
    engine.say("You dead")
    engine.runAndWait()
  elif user_input == "right":
    haunted_room()
  elif user_input == "backward":
    print("your game restarts")
    engine.say("your game restarts")
    engine.runAndWait()
    introScene()
  elif user_input == "forward":
    print("You win Gold")
    engine.say("You win Gold")
    engine.runAndWait()
    print("You find that this door opens.")
    engine.say("You find that this door opens.")
    engine.runAndWait()
    print("You won!")
    engine.say("You won!")
    engine.runAndWait()
  else: 
    print("Please enter a valid option for the adventure game.")
    engine.say("Please enter a valid option for the adventure game.")
    engine.runAndWait()

def left_room():
  print("You made it! You've found an exit.")
  engine.say("You made it! You've found an exit.")
  engine.runAndWait()
  quit()
def right_room():
  print("The road is blocked")
  engine.say("The road is blocked")
  engine.runAndWait()
  print("The game restarts")
  engine.say("The game restarts")
  engine.runAndWait()
  introScene()




def introScene():
  print(f"Hello {name},You are at junction, and you can choose right or left or forward or backword")
  engine.say("You are at junction")
  engine.say("and you can choose right or left or forward or backword")
  engine.runAndWait()
  print("Please enter left/right/backward/forward")
  engine.say("Please enter left or right or backward or forward")
  engine.runAndWait()
  user_input = input().lower()
  if user_input == "left":
    left_room()
  elif user_input == "right":
    right_room()
  elif user_input == "forward":
    forward_room()
  elif user_input == "backward":
    backward_room()
  else: 
    print("Please enter a valid option for the adventure game.")
    engine.say("Please enter a valid option for the adventure game.")
    engine.runAndWait()

if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    engine.say("Welcome to the Adventure Game!")
    engine.runAndWait()
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    engine.say("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    engine.runAndWait()
    print("However, during your exploration, you find yourself lost.")
    engine.say(" However, during your exploration, you find yourself lost.")
    engine.runAndWait()
    print("You can choose to walk in multiple directions to find a way out and win mysterious gifts.")
    engine.say(" You can choose to walk in multiple directions to find a way out and win mysterious gifts.")
    engine.runAndWait()
    print("Let's start with your name: ")
    engine.say("Let's start with your name")
    engine.runAndWait()
    name = input()
    introScene()
   
