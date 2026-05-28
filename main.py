import turtle
import pandas as pd

"""TEXT"""
FONT = ("Courier", 10, "normal")

"""Path For Files"""
IMAGE = "Armenian_Final_map.gif"
REGIONS_DATA_PATH = "armenian_regions.csv"

"""Screen Settings"""
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("--Armenian-Map-Guessing GAME--")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

"""Answer List"""
right_answers = []
all_regions = []
not_guessed = []
new_data = pd.DataFrame(not_guessed) 

"""Processing Data:"""
processed_data = pd.read_csv(REGIONS_DATA_PATH)
data_list = processed_data["region"].to_list()

"""User Input"""
user_input = screen.textinput(title="Guess the region", prompt="What is your guess? ")

# Safety check in case the user hits cancel on the very first prompt
if user_input is None:
    user_input_polished = "Exit"
else:
    user_input_polished = user_input.title()

while len(right_answers) < 10:
    if user_input_polished == "Exit":
        for region in data_list:
            if region not in right_answers:
                not_guessed.append(region)
        # Create the dataframe and save to CSV
        new_data = pd.DataFrame(not_guessed, columns=["region"])
        new_data.to_csv("regions-to-learn.csv", index=False)
        break

    # Make sure we don't count the same correct guess multiple times
    if user_input_polished in data_list and user_input_polished not in right_answers:
        right_answers.append(user_input_polished)
        region_coord_row = processed_data[processed_data["region"] == user_input_polished]

        # X and Y coordinates
        x_cor = int(region_coord_row["x"].item())
        y_cor = int(region_coord_row["y"].item())

        # Creating text on map with turtle
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.goto(x_cor, y_cor)
        text_turtle.write(user_input_polished, font=FONT)
        
    # Ask for the next guess 
    user_input = screen.textinput(title=f"{len(right_answers)}/11 Correct", prompt="What's another region's name? ")
    
    # Check if they hit cancel, if so, trigger the exit logic on the next loop
    if user_input is None:
        user_input_polished = "Exit"
    else:

        # THE FIX: Polish the NEW input so the loop can check it!
        user_input_polished = user_input.title()

print(f"You guessed {len(right_answers)} regions. Check 'regions-to-learn.csv' for what you missed!")


"""-------------------------------------------------------------------------------------------------------------------------------"""