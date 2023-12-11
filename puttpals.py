class Hole:
  def __init__(self, hole_number, par, stroke_index):
      self.hole_number = hole_number
      self.par = par
      self.stroke_index = stroke_index

  def __str__(self):
      return f"Hole {self.hole_number} - Par: {self.par}, Stroke Index: {self.stroke_index}"

class Player:
  def __init__(self, name, handicap):
      self.name = name
      self.handicap = handicap
      self.scores = {}

  def play_hole(self, hole, strokes):
      self.scores[hole.hole_number] = strokes

  def calculate_total_score(self):
      return sum(self.scores.values())

  def __str__(self):
      return f"{self.name} - Handicap: {self.handicap}, Total Score: {self.calculate_total_score()}"

class Course:
  def __init__(self, name, holes):
      self.name = name
      self.holes = holes

def get_player_info():
  name = input("Enter player's name: ")
  handicap = int(input("Enter your handicap: "))
  return Player(name, handicap)

def create_custom_course():
  course_name = input("Enter the name of the course: ")
  holes = []
  for i in range(1, 19):
      print(f"Enter details for Hole {i}:")
      par = int(input("Par: "))
      stroke_index = int(input("Stroke Index: "))
      holes.append(Hole(i, par, stroke_index))
  return Course(course_name, holes)

def get_course_choice():
  print("Choose a golf course:")
  print("1. Ostschweizerischer Golfclub Niederbüren")
  print("2. Golfclub Appenzell")
  print("3. Golfpark Waldkirch")
  print("4. Create a new course")
  choice = input("Enter your choice (1-4): ")

  if choice == '1':
      predefined_holes = [Hole(1, 5, 13), Hole(2, 4, 9), Hole(3, 4, 1), Hole(4, 5, 3), Hole(5, 3, 11), Hole(6, 4, 17), Hole(7, 4, 7), Hole(8, 3, 15), Hole(9, 4, 5), Hole(10, 3, 8), Hole(11, 4, 18), Hole(12, 4, 12), Hole(13, 4, 6), Hole(14, 4, 2), Hole(15, 5, 16), Hole(16, 3, 10), Hole(17, 4, 4), Hole(18, 5, 14)]
      return Course("Ostschweizerischer Golfclub Niederbüren", predefined_holes)
  elif choice == '2':
      predefined_holes = [Hole(1, 3, 15), Hole(2, 4, 13), Hole(3, 5, 5), Hole(4, 4, 7), Hole(5, 4, 3), Hole(6, 5, 9), Hole(7, 3, 17), Hole(8, 5, 1), Hole(9, 4, 11), Hole(10, 3, 14), Hole(11, 4, 12), Hole(12, 3, 18), Hole(13, 5, 2), Hole(14, 4, 4), Hole(15, 4, 6), Hole(16, 4, 8), Hole(17, 4, 10), Hole(18, 3, 16)]
      return Course("Golfclub Appenzell", predefined_holes)
  elif choice == '3':
      predefined_holes = [Hole(1, 4, 13), Hole(2, 4, 3), Hole(3, 3, 11), Hole(4, 5, 5), Hole(5, 3, 17), Hole(6, 4, 1), Hole(7, 4, 9), Hole(8, 4, 7), Hole(9, 5, 15), Hole(10, 5, 6), Hole(11, 3, 16), Hole(12, 4, 4), Hole(13, 4, 14), Hole(14, 3, 10), Hole(15, 4, 12), Hole(16, 4, 2), Hole(17, 3, 18), Hole(18, 5, 8)]
      return Course("Golfpark Waldkirch", predefined_holes)
  else:
      return create_custom_course()

def main():
  course = get_course_choice()

  players = []

  while True:
      player = get_player_info()
      players.append(player)

  
      for hole in course.holes:
          print(hole)
          strokes = int(input(f"Enter strokes for Hole {hole.hole_number}: "))
          player.play_hole(hole, strokes)

      another_player = input("Is there another player? (yes/no): ").lower()
      if another_player != 'yes':
          break

  players.sort(key=lambda x: x.calculate_total_score())
  print(f"\nResults at {course.name}:")
  for player in players:
      print(player)

if __name__ == "__main__":
  main()