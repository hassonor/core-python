import datetime

with open("logfile.txt", "a") as log:
    time = datetime.time()
    log.write(f"Update from {time}:]\n")

# End of with block - file is closed automatically

# Basic Structure - The `with` Statement
# ______________________________________

# with expression as target_var:
#     do_something(target_var)

"""
- The 'expression' returns an object that is stored in memory as a context manager*.
- When the object is created, its '__enter__()' method is invoked, and the value it returns 
  is assigned to 'target_var' if we have defined one.
- Upon exiting the block, the '__exit__()' method of the object, if it exists, is invoked.
  This method can handle tasks such as closing files, processes, releasing variables, and more (clean-up code),
  without the need for explicit calls. This makes the code more readable and easier to maintain.
"""
