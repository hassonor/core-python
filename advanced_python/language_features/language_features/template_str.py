from string import Template

templ = Template("You're watching ${title} by ${author}")

# Use the substitute method with keyword arguments
str2 = templ.substitute(title="Cool Movie", author="Or Hasson")
print(str2)

# Use the substitute method with a dictionary
data = {
    "author": "Or Hasson",
    "title": "Cool Movie"
}

str3 = templ.substitute(data)
print(str3)
