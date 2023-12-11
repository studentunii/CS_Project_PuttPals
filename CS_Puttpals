# streamlit_golf_app.py
import streamlit as st
from golf_app import GolfApp

# Create an instance of GolfApp
golf_app = GolfApp()

# Load existing accounts and courses
golf_app.load_accounts()
golf_app.load_courses()

st.title("Welcome to the Golf App!")

menu_choice = st.sidebar.radio("Menu", ["Home", "Register", "Login", "Exit"])

if menu_choice == "Home":
    st.write("This is the home page.")

elif menu_choice == "Register":
    st.subheader("Registration:")
    first_name = st.text_input("Enter your first name:")
    last_name = st.text_input("Enter your last name:")
    handicap = st.number_input("Enter your handicap:", min_value=0, step=1)
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password", key="register_password")
    account_type = st.radio("Register as user or admin?", ["User", "Admin"])
    is_admin = account_type == "Admin"

    if st.button("Register"):
        golf_app.accounts.append(golf_app.create_account(first_name, last_name, handicap, username, password, is_admin))
        golf_app.save_accounts()

elif menu_choice == "Login":
    st.subheader("Login:")
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password", key="login_password")

    if st.button("Login"):
        if golf_app.login(username, password):
            st.success("Login successful.")
            if golf_app.current_user.is_admin:
                st.sidebar.success("Logged in as Admin")
            else:
                st.sidebar.success("Logged in as User")
        else:
            st.error("Invalid username or password. Please try again.")

elif menu_choice == "Exit":
    # Save the courses before exiting
    golf_app.save_courses()
    st.balloons()
    st.write("Goodbye!")
    st.stop()

if golf_app.current_user:
    st.sidebar.subheader(f"Logged in as: {golf_app.current_user.username}")

    if golf_app.current_user.is_admin:
        st.sidebar.info("Admin actions:")
        admin_choice = st.sidebar.radio("Select an action", ["Add Golf Course", "Delete Golf Course", "Logout"])

        if admin_choice == "Add Golf Course":
            st.subheader("Add Golf Course:")
            course_name = st.text_input("Enter the name of the course:")
            holes = []
            for i in range(1, 19):
                st.write(f"Enter details for Hole {i}:")
                par = st.number_input(f"Par for Hole {i}:", min_value=1, step=1)
                stroke_index = st.number_input(f"Stroke Index for Hole {i}:", min_value=1, step=1)
                holes.append({"hole_number": i, "par": par, "stroke_index": stroke_index})

            if st.button("Add Golf Course"):
                golf_app.courses.append(golf_app.create_custom_course(course_name, holes))
                golf_app.save_courses()

        elif admin_choice == "Delete Golf Course":
            st.subheader("Delete Golf Course:")
            if not golf_app.courses:
                st.warning("No courses available for deletion.")
            else:
                course_options = [course.name for course in golf_app.courses]
                course_to_delete = st.selectbox("Select a course to delete:", course_options)
                if st.button("Delete Course"):
                    golf_app.courses = [course for course in golf_app.courses if course.name != course_to_delete]
                    golf_app.save_courses()
                    st.success(f"Golf Course '{course_to_delete}' deleted.")

        elif admin_choice == "Logout":
            golf_app.current_user = None
            st.success("Logged out.")
            st.sidebar.warning("Admin logged out.")

    else:  # User actions
        st.sidebar.info("User actions:")
        user_choice = st.sidebar.radio("Select an action", ["Let's play!", "Show previous games", "Compete with your puttpals", "Logout"])

        if user_choice == "Let's play!":
            st.subheader("Let's play!")
            if not golf_app.courses:
                st.warning("No courses available. Please add a course first.")
            else:
                course_options = [course.name for course in golf_app.courses]
                selected_course = st.selectbox("Select a course to play:", course_options)

                if st.button("Play"):
                    course = next(course for course in golf_app.courses if course.name == selected_course)
                    golf_app.current_user.player.play_round(course)
                    golf_app.save_accounts()

        elif user_choice == "Show previous games":
            st.subheader("Show previous games:")
            golf_app.current_user.player.show_previous_rounds()

        elif user_choice == "Compete with your puttpals":
            st.subheader("Compete with your puttpals:")
            friend_username = st.text_input("Enter the username of your friend:")
            friend = next((account for account in golf_app.accounts if account.username == friend_username), None)

            if st.button("Compete"):
                if friend and friend.is_admin:
                    st.error("Cannot compete with an admin.")
                elif friend:
                    golf_app.current_user.player.compete_with_friend(friend.player)
                else:
                    st.warning(f"No user found with the username '{friend_username}'.")
                    st.warning("Please enter a valid username.")

        elif user_choice == "Logout":
            golf_app.current_user = None
            st.success("Logged out.")
            st.sidebar.warning("User logged out.")
