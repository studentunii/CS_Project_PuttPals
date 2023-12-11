
from datetime import datetime

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

    def play_round(self, course):
        round_scores = {}
        print(f"\nPlaying at {course.name}...")
        for hole in course.holes:
            print(hole)
            strokes = int(input(f"Enter strokes for Hole {hole.hole_number}: "))
            round_scores[hole.hole_number] = strokes

        round_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.scores[round_date] = {"course": course.name, "scores": round_scores}
        print("\nRound completed!")

    def show_previous_rounds(self):
        if not self.scores:
            print("No previous rounds.")
            return

        print("\nPrevious Rounds:")
        print("{:<20} {:<20} {:<20}".format("Course", "Score", "Date"))
        for date, data in self.scores.items():
            total_score = sum(data["scores"].values())
            print("{:<20} {:<20} {:<20}".format(data["course"], total_score, date))

    def compete_with_friend(self, friend):
        print("\nComparing with your friend...")
        user_scores = self.scores.values()
        friend_scores = friend.scores.values()

        if not user_scores or not friend_scores:
            print("No rounds to compare.")
            return

        user_total = sum(sum(round["scores"].values()) for round in user_scores)
        friend_total = sum(sum(round["scores"].values()) for round in friend_scores)

        print(f"{self.name}'s total score: {user_total}")
        print(f"{friend.name}'s total score: {friend_total}")

    def __str__(self):
        return f"{self.name} - Handicap: {self.handicap}"


class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes


class Account:
    def __init__(self, first_name, last_name, handicap, username, password, is_admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.handicap = handicap
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.player = Player(f"{first_name} {last_name}", handicap)


class GolfApp:
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.courses = []  # List to store available golf courses

    def save_accounts(self, filename='accounts.txt'):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"{account.first_name},{account.last_name},{account.handicap},{account.username},{account.password},{account.is_admin}\n")

    def load_accounts(self, filename='accounts.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    first_name, last_name, handicap, username, password, is_admin = data
                    handicap = int(handicap)
                    is_admin = is_admin.lower() == 'true'
                    account = Account(first_name, last_name, handicap, username, password, is_admin)
                    self.accounts.append(account)
        except FileNotFoundError:
            pass

    def save_courses(self, filename='courses.txt'):
        with open(filename, 'w') as file:
            for course in self.courses:
                file.write(f"{course.name}\n")
                for hole in course.holes:
                    file.write(f"{hole.hole_number},{hole.par},{hole.stroke_index}\n")

    def load_courses(self, filename='courses.txt'):
        try:
            with open(filename, 'r') as file:
                line_iter = iter(file)
                while True:
                    try:
                        course_name = next(line_iter).strip()
                        holes = []
                        for _ in range(18):
                            hole_data = next(line_iter).strip().split(',')
                            hole_number, par, stroke_index = map(int, hole_data)
                            holes.append(Hole(hole_number, par, stroke_index))
                        course = Course(course_name, holes)
                        self.courses.append(course)
                    except StopIteration:
                        break
        except FileNotFoundError:
            pass

    def create_account(self):
        print("Registration:")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        handicap = int(input("Enter your handicap: "))
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account_type = input("Register as user or admin? (user/admin): ").lower()
        is_admin = account_type == 'admin'
        account = Account(first_name, last_name, handicap, username, password, is_admin)
        self.accounts.append(account)

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for account in self.accounts:
            if account.username == username and account.password == password:
                self.current_user = account
                return True
        return False

    def admin_actions(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Golf Course")
            print("2. Delete Golf Course")
            print("3. Logout")
            admin_choice = input("Enter your choice (1-3): ")

            if admin_choice == '1':
                course = self.create_custom_course()
                self.courses.append(course)
                print(f"\nGolf Course '{course.name}' added.")
            elif admin_choice == '2':
                print("Available Golf Courses:")
                for i, course in enumerate(self.courses, 1):
                    print(f"{i}. {course.name}")
                course_index = int(input("Enter the index of the course to delete: ")) - 1
                del self.courses[course_index]
                print("Golf Course deleted.")
            elif admin_choice == '3':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def user_actions(self):
      while True:
          print("\nUser Menu:")
          print("1. Let's play!")
          print("2. Show previous games")
          print("3. Compete with your puttpals")
          print("4. Logout")
          user_choice = input("Enter your choice (1-4): ")

          if user_choice == '1':
              if not self.current_user or not self.current_user.player:
                  print("Please login first.")
              else:
                  self.play_golf()
          elif user_choice == '2':
              if not self.current_user or not self.current_user.player:
                  print("Please login first.")
              else:
                  self.current_user.player.show_previous_rounds()
          elif user_choice == '3':
              if not self.current_user or not self.current_user.player:
                  print("Please login first.")
              else:
                  friend_username = input("Enter the username of your friend: ")
                  friend = next((account for account in self.accounts if account.username == friend_username), None)
                  if friend and friend.is_admin:
                      print("Cannot compete with an admin.")
                  elif friend:
                      self.current_user.player.compete_with_friend(friend.player)
                  else:
                      print(f"No user found with the username '{friend_username}'.")
          elif user_choice == '4':
              break
          else:
              print("Invalid choice. Please enter a valid option.")

    def play_golf(self):
      print("\nChoose a Golf Course:")
      for i, course in enumerate(self.courses, 1):
          print(f"{i}. {course.name}")

      choice = input("Enter the index of the course to play: ")

      if choice.isdigit() and 1 <= int(choice) <= len(self.courses):
          course = self.courses[int(choice) - 1]
          self.current_user.player.play_round(course)
      else:
          print("Invalid choice. Please enter a valid index.")

    def create_custom_course(self):
      course_name = input("Enter the name of the course: ")
      holes = []
      for i in range(1, 19):
          print(f"Enter details for Hole {i}:")
          par = int(input("Par: "))
          stroke_index = int(input("Stroke Index: "))
          holes.append(Hole(i, par, stroke_index))
      return Course(course_name, holes)

def main():
  golf_app = GolfApp()

  # Load existing accounts and courses
  golf_app.load_accounts()
  golf_app.load_courses()

  while True:
      print("\nWelcome to the Golf App!")
      print("1. Register")
      print("2. Login")
      print("3. Exit")
      choice = input("Enter your choice (1-3): ")

      if choice == '1':
          golf_app.create_account()
          # Save the accounts after each registration
          golf_app.save_accounts()
      elif choice == '2':
          if golf_app.login():
              if golf_app.current_user.is_admin:
                  golf_app.admin_actions()
              else:
                  golf_app.user_actions()
          else:
              print("Invalid username or password. Please try again.")
      elif choice == '3':
          # Save the courses before exiting
          golf_app.save_courses()
          print("Goodbye!")
          break
      else:
          print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
  main()