class Account:
  def __init__(self, first_name, last_name, handicap, username, password, is_admin=False):
      self.first_name = first_name
      self.last_name = last_name
      self.handicap = handicap
      self.username = username
      self.password = password
      self.is_admin = is_admin


class GolfApp:
  def __init__(self):
      self.accounts = []
      self.current_user = None

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
              course = create_custom_course()
              courses.append(course)
              print(f"\nGolf Course '{course.name}' added.")
          elif admin_choice == '2':
              print("Available Golf Courses:")
              for i, course in enumerate(courses, 1):
                  print(f"{i}. {course.name}")
              course_index = int(input("Enter the index of the course to delete: ")) - 1
              del courses[course_index]
              print("Golf Course deleted.")
          elif admin_choice == '3':
              break
          else:
              print("Invalid choice. Please enter a valid option.")

  def user_actions(self):
      while True:
          print("\nUser Menu:")
          print("1. Choose a Golf Course")
          print("2. Enter Scores")
          print("3. Calculate Total Score")
          print("4. Compete with Other Users")
          print("5. Logout")
          user_choice = input("Enter your choice (1-5): ")

          if user_choice == '1':
              course = get_course_choice()
              self.play_golf(course)
          elif user_choice == '2':
              if not self.current_user:
                  print("Please login first.")
              else:
                  course = get_course_choice()
                  self.play_golf(course)
          elif user_choice == '3':
              if not self.current_user:
                  print("Please login first.")
              else:
                  print(f"Total Score: {self.calculate_total_score()}")
          elif user_choice == '4':
              if not self.current_user:
                  print("Please login first.")
              else:
                  self.compete_with_users()
          elif user_choice == '5':
              break
          else:
              print("Invalid choice. Please enter a valid option.")

  def play_golf(self, course):
      for hole in course.holes:
          print(hole)
          strokes = int(input(f"Enter strokes for Hole {hole.hole_number}: "))
          self.current_user.play_hole(hole, strokes)

  def calculate_total_score(self):
      if self.current_user:
          return self.current_user.calculate_total_score()
      else:
          return 0

  def compete_with_users(self):
      if not self.current_user:
          print("Please login first.")
      else:
          print("Compete with other users functionality goes here.")


def main():
  golf_app = GolfApp()

  while True:
      print("\nWelcome to the Golf App!")
      print("1. Register")
      print("2. Login")
      print("3. Exit")
      choice = input("Enter your choice (1-3): ")

      if choice == '1':
          golf_app.create_account()
      elif choice == '2':
          if golf_app.login():
              if golf_app.current_user.is_admin:
                  golf_app.admin_actions()
              else:
                  golf_app.user_actions()
          else:
              print("Invalid username or password. Please try again.")
      elif choice == '3':
          print("Goodbye!")
          break
      else:
          print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
  courses = []  # List to store available golf courses
  main()