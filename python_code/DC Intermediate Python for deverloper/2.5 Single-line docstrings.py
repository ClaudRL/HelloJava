# Exercise
# Single-line docstrings
# Docstrings are used to explain the purpose of a function. While the function name should be descriptive, this needs to be balanced with the length of the function name, so docstrings allow you to provide more detail.

# In this exercise, you'll take the previously created clean_text function and add a single-line docstring.

# Instructions
# 100 XP
# Add a docstring stating """Swap spaces to underscores and convert text to lowercase.""".
# Access the function's docstring using the appropriate attribute.

def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase."""
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__) # 输出: Swap spaces to underscores and convert text to lowercase.