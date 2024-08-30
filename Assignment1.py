#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Python code to print name,course and python version
import sys

# Define your name and course name
name = "JItesh bhojwani"  # Replace with your actual name
course_name = "MCA"  # Replace with your actual course name
sapid = "590013713"
# Get the Python version
python_version = sys.version

# Print the information
print(f"Name: {name}")
print(f"sap id _ : {sapid}")
print(f"Course Name: {course_name}")

print(f"Python Version: {python_version}")


# In[11]:


# Print Hello,Python World
print("Hello, Python World!")


# In[13]:


# Get the user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Reverse the order of the names
reversed_name = last_name + " " + first_name

# Print the reversed name
print("Your name in reverse order:", reversed_name)


# In[13]:


#String methods used are
#lower():Converts all uppercase characters in a string into lowercase
#Upper(): Converts all lowercase characters in a string into uppercase

# Python3 program to show the
# working of upper() function
text = 'HellO Upes DehradUn'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())


# In[2]:


# Get user input
user_input = input("Enter a number: ")

# Convert input to different numeric data types
try:
    # Convert to integer
    integer_value = int(user_input)
    print(f"Integer value: {integer_value}")
except ValueError:
    print("Invalid input for integer conversion.")

try:
    # Convert to float
    float_value = float(user_input)
    print(f"Float value: {float_value}")
except ValueError:
    print("Invalid input for float conversion.")

try:
    # Convert to complex
    complex_value = complex(user_input)
    print(f"Complex value: {complex_value}")
except ValueError:
    print("Invalid input for complex conversion.")


# In[ ]:


#Integer ( int ): represents positive or negative whole numbers like 3 or -512. 
#Floating point number ( float ): represents real numbers like 3.14159 or -2.5. 
#Complex :consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex numbe


# In[3]:


# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Get user input for length and width
try:
    length = float(input("Enter the length of the rectangle: "))  # Prompt for length
    width = float(input("Enter the width of the rectangle: "))    # Prompt for width

    # Calculate the area
    area = calculate_area(length, width)

    # Display the result
    print(f"The area of the rectangle is: {area} square units")
except ValueError:
    print("Please enter valid numerical values for length and width.")
    


# In[5]:


# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Get user input for length and width
try:
    length = float(input("Enter the length of the rectangle: "))  # Prompt for length
    width = float(input("Enter the width of the rectangle: "))    # Prompt for width

    # Calculate the area
    area = calculate_area(length, width)

    # Display the result formatted to two decimal places
    print("The area of the rectangle is: {:.2f} square units".format(area))
except ValueError:
    print("Please enter valid numerical values for length and width.")


# In[7]:


# Function to calculate the average of three numbers
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Get user input for three numbers
try:
    number1 = float(input("Enter the first number: "))  # Prompt for the first number
    number2 = float(input("Enter the second number: ")) # Prompt for the second number
    number3 = float(input("Enter the third number: "))   # Prompt for the third number

    # Calculate the average
    average = calculate_average(number1, number2, number3)

    # Display the result using % formatting
    print("The average of the three numbers is: %.2f" % average)
except ValueError:
    print("Please enter valid numerical values for the numbers.")


# In[8]:


# Function to determine if the number is positive, negative, or zero
def determine_number_type(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")  # Prompt for a number

    if user_input.lower() == 'exit':  # Check if the user wants to exit
        print("Exiting the program. Goodbye!")
        break  # Exit the loop

    try:
        # Convert input to float
        number = float(user_input)

        # Determine the type of the number
        number_type = determine_number_type(number)

        # Display the result
        print(f"The number you entered is {number_type}.")
    except ValueError:
        print("Please enter a valid numerical value.")


# In[10]:


# Function to determine if the numbers are even or odd
def check_even_odd(num1, num2):
    # Check if both numbers are even
    if num1 % 2 == 0 and num2 % 2 == 0:
        return "Both numbers are even."
    # Check if both numbers are odd
    elif num1 % 2 != 0 and num2 % 2 != 0:
        return "Both numbers are odd."
    # If one is even and the other is odd
    else:
        return "One number is even and the other is odd."

# Get user input for two numbers
try:
    number1 = float(input("Enter the first number: "))  # Prompt for the first number
    number2 = float(input("Enter the second number: ")) # Prompt for the second number

    # Ensure that the numbers are integers for even/odd check
    if number1.is_integer() and number2.is_integer():
        # Call the function to check even or odd
        result = check_even_odd(int(number1), int(number2))
        # Display the result
        print(result)
    else:
        print("Please enter valid integer values for even/odd check.")
except ValueError:
    print("Please enter valid numerical values.")


# In[11]:


# Function to convert an integer to binary, octal, and hexadecimal
def convert_number(num):
    # Initialize empty strings for binary, octal, and hexadecimal
    binary = ""
    octal = ""
    hexadecimal = ""

    # Convert to binary using bitwise operators
    for i in range(31, -1, -1):  # Loop from 31 to 0 for a 32-bit representation
        if num & (1 << i):  # Check if the ith bit is set
            binary += "1"
        else:
            binary += "0"

    # Remove leading zeros from binary representation
    binary = binary.lstrip("0") or "0"  # Ensure at least one '0' if the number is 0

    # Convert to octal using bitwise operators
    temp_num = num
    while temp_num > 0:
        octal = str(temp_num & 7) + octal  # Get the last 3 bits (octal digit)
        temp_num >>= 3  # Right shift by 3 bits to process the next octal digit

    # If the number is 0, set octal to "0"
    if num == 0:
        octal = "0"

    # Convert to hexadecimal using bitwise operators
    temp_num = num
    while temp_num > 0:
        hex_digit = temp_num & 15  # Get the last 4 bits (hexadecimal digit)
        if hex_digit < 10:
            hexadecimal = str(hex_digit) + hexadecimal  # Convert to string
        else:
            hexadecimal = chr(hex_digit - 10 + ord('A')) + hexadecimal  # Convert to A-F
        temp_num >>= 4  # Right shift by 4 bits to process the next hex digit

    # If the number is 0, set hexadecimal to "0"
    if num == 0:
        hexadecimal = "0"

    return binary, octal, hexadecimal

# Get user input
try:
    number = int(input("Enter an integer: "))  # Prompt for an integer

    # Convert the number and get its representations
    binary_rep, octal_rep, hex_rep = convert_number(number)

    # Display the results
    print(f"Binary: {binary_rep}")
    print(f"Octal: {octal_rep}")
    print(f"Hexadecimal: {hex_rep}")
except ValueError:
    print("Please enter a valid integer.")

