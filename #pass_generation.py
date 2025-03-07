import string
import random

# print(string.digits) # = the numbers 0,1,2,3,4,5,6,7,8,9
# print(string.ascii_letters) # = all letters, both uppercase and lowercase
# print(string.ascii_lowercase) # all lowercase letters
# print(string.ascii_uppercase) # all uppercase letters

def make_serial(count):
    all_chars = string.ascii_letters + string.digits 
    # print(all_chars) # this will print all characters, regardless of the parameter
    
    chars_count = len(all_chars) # = 62 (26 lowercase + 26 uppercase + 10 digits)
    # print(chars_count)

    serial_list = []

    while count > 0:
        random_number = random.randint(0, chars_count - 1) 
        # Why chars_count - 1? Because the indexes are zero-based (0 to 61), 
        # and I want a random index within the range of available characters.
        
        random_character = all_chars[random_number] 
        # Getting a random character from all_chars using the random index
        
        serial_list.append(random_character)

        count -= 1 # Decrease count by 1 (count = count - 1)
        
        print("".join(serial_list)) 
        # After each loop, this prints the current serial as a string

make_serial(30) 
# This will generate a 30-character serial, showing the serial growing with each iteration
