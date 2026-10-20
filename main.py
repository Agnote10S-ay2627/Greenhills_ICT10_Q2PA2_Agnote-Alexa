# Set Operators
from pyscript import display, document


def add_members (e):
    document.getElementById.innerHTML('members') = ""

    grade_ten = {'Jett', 'Phoenix', 'Raze', 'Reyna', 'Sage'}
    grade_nine = {'Viper', 'Brimstone', 'Sova', 'Chamber', 'Yoru'}
    grade_eight = {'Gekko', 'Neon', 'Astra', 'Fade', 'Harbor'}
    grade_seven = {'Hush', 'Tejo', 'Miks', 'Clove', 'Iso'}

    total_members = grade_ten | grade_nine | grade_eight | grade_seven # Combining the 4 sets

    first_name = document.getElementById('Fname').value
    last_name = document.getElementById('Lname').value

    newmembers = first_name + " " + last_name # Concatenating the names inputted in the text box
    total_members.add(newmembers) # Adding the new name to the total member list

    display("br".join(total_members), target='members', raw="True") # Displaying list of members
    display(f'Total number of members: {len(total_members)}', target='members') # Displaying total number of members