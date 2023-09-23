# Define a class called Color
class Color:
    # Initialize the Color object with default RGB values
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # Define how to handle attribute access for special attributes
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return self.red, self.green, self.blue
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError  # Raise exception for unrecognized attributes

    # Define how to handle attribute setting for special attributes
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            # Default behavior for attribute setting
            super().__setattr__(attr, val)

    # Define a custom directory for the object, listing all accessible attributes
    def __dir__(self):
        return "red", "green", "blue", "rgbcolor", "hexcolor"


# Create a Color object
cls1 = Color()

# Access and print the rgbcolor attribute
print(cls1.rgbcolor)

# Access and print the hexcolor attribute
print(cls1.hexcolor)

# Modify the rgbcolor attribute
cls1.rgbcolor = (125, 200, 86)

# Print the updated rgbcolor and hexcolor attributes
print(cls1.rgbcolor)
print(cls1.hexcolor)

# Print the red attribute
print(cls1.red)

# Print the list of all attributes and methods accessible on the object
print(dir(cls1))
