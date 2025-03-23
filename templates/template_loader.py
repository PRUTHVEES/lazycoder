import os

def get_template_path(template_name):
    """
    Returns the absolute path of a Jinja template file.
    """
    package_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(package_dir, template_name)

    if os.path.exists(template_path):
        return template_path
    else:
        raise FileNotFoundError(f"Template '{template_name}' not found.")
