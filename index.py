from jinja2 import Environment, FileSystemLoader
import os

# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the template from the correct directory
env = Environment(loader=FileSystemLoader(script_dir))

# Load the template
template = env.get_template("php_template.php.jinja")

# Define data
data = {
    "class_name": "Profile",
    "properties": ["name", "email", "age"]
}

# Render template
php_code = template.render(data)

# Save to a PHP file
with open("generated_files/User.php", "w") as f:
    f.write(php_code)

print("PHP Class Generated Successfully!")
