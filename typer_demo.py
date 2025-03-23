import typer
import re
from custom_modules.dependency_installer import *


app = typer.Typer()

VALID_LANGUAGES = {"python", "javascript", "js", "swift", "php"}

VALID_FRAMEWORKS = {
    "python": {"flask", "django"},
    "js": {"react", "vue", "svelte", "angular"},
    "javascript": {"react", "vue", "svelte", "angular"},
    "php": {"laravel"}
}

VALID_FLAGS = {"constructs", "output", "init", "install", "flat", "structure", "git"}

def initialize_project(language, framework):
    pass

def validate_inputs(language, framework, flags):
    errors = []

    if language not in VALID_LANGUAGES:
        errors.append(f"❌ Invalid language: {language}")

    if framework and framework not in VALID_FRAMEWORKS.get(language, {}):
        errors.append(f"❌ Invalid framework '{framework}' for language '{language}'")

    for flag in flags:
        if flag and flag not in VALID_FLAGS:
            errors.append(f"❌ Unknown flag: {flag}")

    return errors


def parse_constructs(constructs_str):
    """Parses constructs to extract class names, methods, and properties."""
    constructs = {}

    # match = re.match(r"(\w+):(\w+)(?:\[(.*?)\])?", item.strip())
    # match = re.match(r"(\w+):([\w_]+)(?:\[(.*?)\])?", item)
    match = re.match(r"(\w+):([\w_]+)(?:\[(.*?)\])?", constructs_str)

    if match:
        construct_type, name, details = match.groups()
        methods, props = {}, []

        if details:
            # Extract methods and properties using regex
            method_section = re.search(r"method:([^;]+)", details)  # Extract methods
            prop_match = re.search(r"prop:([^;]+)", details)  # Extract properties

            if method_section:
                method_matches = re.findall(r"([\w_]+(?:\([^\)]*\))?)", method_section.group(1))
                #methods = method_match.group(1)

                for method in method_matches:
                    method_name, args = re.match(r"([\w_]+)(?:\((.*?)\))?", method).groups()
                    methods[method_name] = args.split(",") if args else []
            if prop_match:
                props = prop_match.group(1).split(",")
                #props = prop_match.group(1)

        if construct_type == "class":
            constructs[name] = {"type": "class", "methods": methods or None, "properties": props or None}
        else:
            constructs[name] = {"type": construct_type}

    print(constructs)
    return constructs

def generate_files(language, framework, constructs, structures, output_dir, init, git, dependencies):
    """Generates a formatted output based on user input."""
    parsed_constructs = parse_constructs(constructs) if constructs else {}

    construct_details = []
    for name, data in parsed_constructs.items():
        if data["type"] == "class":
            methods = data["methods"] or []
            props = data["properties"] or []

            method_str = ", ".join(f"{m}({', '.join(args)})" if args else m for m, args in methods.items()) if methods else "None"
            prop_str = ", ".join(props) if props else "None"

            construct_details.append(f"class {name} (Methods: {method_str}, Props: {prop_str})")
        else:
            construct_details.append(f"{data['type']} {name}")

    structures_str = ", ".join(structures) if structures else "None"

    initialize_project(language,framework)

    if dependencies:
        install_dependencies(language, dependencies)


    print("\n✅ Generating Project with the following details:")
    print(f"- Language: {language}")
    print(f"- Framework: {framework if framework else 'None'}")
    print(f"- Constructs: {', '.join(construct_details) if construct_details else 'None'}")
    print(f"- Structures: {structures_str}")
    print(f"- Output Directory: {output_dir}\n")



@app.command()
def generate(
        l: str = typer.Option(None, "-l", "--language", help="Specify the programming language"),
        f: str = typer.Option(None, "-f", "--framework", help="Specify the framework"),
        c: str = typer.Option(None, "-c", "--constructs",
                              help="Specify the Constructs (e.g., class:User[method:init,login;prop:username,email])"),
        s: str = typer.Option(None, "-s", "--structure",
                              help="Specify the Structures you want to initialize within the Constructs"),
        o: str = typer.Option(".","-o","--output",help="Specify the output directory for generated files"),
        init: bool = typer.Option(False,"--init",help="Initialize a new Project Structure"),
        git: bool = typer.Option(False, "--git", help="Initialize a Git repository"),
        i: str = typer.Option(None, "--install", help="Installs dependencies for the selected framework (e.g., npm install for React).")
):
    entered_flags = [flag for flag in [
        "constructs" if c else None,
        "structure" if s else None,
        "init" if init else None,
        "git" if git else None
    ] if flag]

    errors = validate_inputs(l, f, entered_flags)

    # Fix: Ensure constructs and structures are correctly processed
    constructs = c if c else ""
    structures = s.split(",") if s else []

    if errors:
        print("\n".join(errors))  # Print all errors
    else:
        generate_files(l, f, constructs, structures, o, init, git, i)


if __name__ == "__main__":
    app()
