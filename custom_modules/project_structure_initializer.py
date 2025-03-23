import os

def create_structure(structures):
    """Creates directories for the project."""
    for structure in structures:
        folder = structure.split(":")[0] + "s"  # e.g., model -> models
        os.makedirs(folder, exist_ok=True)
        print(f"📂 Created directory: {folder}/")
