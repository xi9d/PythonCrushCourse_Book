message = "hello this is the basic text, 🕸️🕸️";
print(message)

# Variable names can contain only letters, numbers, and underscores.
# They can start with a letter or an underscore, but not with a number.
# For instance, you can call a variable message_1 but not 1_message.
# •	 Spaces are not allowed in variable names, but underscores can be used
# to separate words in variable names. For example, greeting_message works,
# but greeting message will cause errors.
# •	 Avoid using Python keywords and function names as variable names;
# that is, do not use words that Python has reserved for a particular programmatic purpose,
# such as the word print. (See “Python Keywords
# and Built-in Functions” on page 489.)
# •	 Variable names should be short but descriptive. For example, name is
# better than n, student_name is better than s_n, and name_length is better
# than length_of_persons_name.
# •	 Be careful when using the lowercase letter l and the uppercase letter O
# because they could be confused with the numbers 1 and 0.


# Example of a variable error

# print(mesage)

# Let's work with Strings
name = "Fox bash"
print(name.title())
print(name.upper())
print(name.count("b"))

# concatenation
firstName = "fox"
lastName = "bash"
fullName = firstName + " " + lastName
print(fullName)

# Whitespace

print("\tThis is a tab")
print("\nGoes to next line\nAlso this one")

word = " python "
print("\nOriginal"+word)
print("This will remove any whitespace "+word.rstrip()+"check if there any whitespace on the right side")
print("This will remove from left" + word.lstrip()+"From left")
print("This will remove from every side"+word.strip())