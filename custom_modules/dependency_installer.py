import subprocess

VALID_PACKAGE_MANAGERS = {
    "python": "pip",
    "js": "npm",
    "javascript": "npm",
    "php": "composer"
}


def validate_dependencies(dependencies):
    """Validates if dependencies are in a valid format (comma-separated list)."""
    if not dependencies:
        return []

    deps_list = [dep.strip() for dep in dependencies.split(",") if dep.strip()]

    if not deps_list:
        print("⚠️ No valid dependencies provided. Skipping installation.")
        return []

    return deps_list


def install_dependencies(language, dependencies, global_install=False):
    """Installs dependencies using the appropriate package manager."""
    deps_list = validate_dependencies(dependencies)

    if not deps_list:
        return  # Exit if no dependencies were provided

    if language not in VALID_PACKAGE_MANAGERS:
        print(f"⚠️ No installation support available for {language}. Skipping dependencies.")
        return

    package_manager = VALID_PACKAGE_MANAGERS[language]
    install_command = []

    if package_manager == "pip":
        install_command = ["pip", "install"] + deps_list
    elif package_manager == "npm":
        if global_install:
            install_command = ["npm", "install", "-g"] + deps_list
        else:
            # Initialize npm project if needed
            subprocess.run(["npm", "init", "-y"], check=False)
            install_command = ["npm", "install"] + deps_list
    elif package_manager == "composer":
        install_command = ["composer", "require"] + deps_list

    print(f"📦 Installing dependencies using {package_manager}: {', '.join(deps_list)}...")

    try:
        subprocess.run(install_command, check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Installation failed! Check if the dependencies are valid.")
