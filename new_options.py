import options 
import states_and_links

# Get the state input from the user
state_var = str(input("Enter a state: "))

# Capitalize the first letter of each word and replace spaces with underscores
modified_state_var = state_var.title().replace(' ', '_')

# Check if the modified state name exists in the options file
if hasattr(options, modified_state_var):
    state_list = getattr(options, modified_state_var)
    cities_dd5 = state_list[:5]
    # Print the first 5 cities
    print(cities_dd5)
else:
    print(f"State '{state_var}' not found in the options file.")
    exit()

city = str(input("Select a city from the above cities: "))

# Check if the selected city is valid
if city.title() not in state_list:
    print(f"City '{city}' not found in the selected state.")
    exit()

modified_city = city.lower().replace(' ', '-')

# Dynamically select state link from states_and_links
if hasattr(states_and_links, modified_state_var):
    state_link = getattr(states_and_links, modified_state_var)
    upd_link = state_link + modified_city + "/"
else:
    print(f"State link for '{state_var}' not found.")
    exit()

# Get the category input from the user
cate = str(input("Enter the category: "))
mod_cate = cate.title()

# Check if the category exists in the options.categories list
if mod_cate in options.categories:
    tempfile = mod_cate.lower().replace(' ', '-')
    final_file = upd_link + tempfile + ".htm"
    print(final_file)
else:
    print(f"Category '{mod_cate}' not found.")
