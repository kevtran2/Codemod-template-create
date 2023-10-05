import os


"""
This script prompts the user for the number of codemod templates they would like to create.
It then prompts the user x times to collect codemod names. Once the user confirms all of the info 
is correct, the script will create folders for each codemod in the current directory. 
"""
def main():
    codemod_names = get_codemod_names()
    owner_name = get_owner_name()
    engine = get_engine_name()
    language = get_language_name()
    
    create_files(codemod_names, owner_name, engine, language)


    """
    version_name = get_version_name()
    framework_name = get_framework_name()
    destination_ver_name = get_dest_ver_name()
    description = get_description()
    applicable_file_ext = get_file_ext()
    """

    # allow user to edit misinputted data
    # create template

def create_files(codemod_names, owner_name, engine, language):
    for name in codemod_names:
        folder_name = f"{name}"
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.mkdir(folder_path)

        index_file_name = f"{folder_path}/index.ts"
        with open(index_file_name, 'w') as file:
            file.write(f"Code for: {name}")

        """ config.json outline
        {
            "schemaVersion": "[vx.x.x]",
            "name": "[framework/version/codemod-name]",
            "engine": "[jscodeshift/ts-morph/piranha/repomod-engine]",
            "language": "[java/ts/tsx]", (Optional - Only if engine is Piranha)
            "dependencyVersionLowerThan": ["[framework]", "[vx.x.x]"],
            "owner": "[codemod owner name]"
        }
        """
        config_file_name = f"{folder_path}/config.json"
        with open(config_file_name, 'w') as file:
            if engine == None or "": engine = "[jscodeshift/ts-morph/piranha/repomod-engine]"
            if language == None or "": language = "[java/ts/tsx] (Optional - Only if engine is Piranha)"
            if owner_name == None or "": owner_name = "[codemod owner name]"
        # DO NOT INDENT the ROWS BELOW, it will break the corrected spacing. ****
            file.write((f'{{\n\
    "schemaVersion": "[vx.x.x]",\n\
    "name": "{name}",\n\
    "engine": "{engine}",\n\
    "language": "{language}",\n\
    "dependencyVersionLowerThan": ["[framework]", "[vx.x.x]"],\n\
    "owner": "{owner_name}"\n}}'))
        # DO NOT INDENT the ROWS ABOVE, it will break the corrected spacing. ****

        test_file_name = f"{folder_path}/test.ts"
        with open(test_file_name, 'w') as file:
            file.write(f"Test code for {name}")

        readme_file_name = f"{folder_path}/READme.md"
        with open(readme_file_name, 'w') as file:
            file.write(f"readme description for {name} codemod")

        print(f"Template created for {name} codemod.")

def enum_print(l: list):
    for i in range(len(l)):
        print(f"{i + 1}: {l[i]}")

def get_codemod_names() -> list: 
    while True:
        name_list = []
        num_mods = ""
        while not num_mods.isnumeric():
            num_mods = input("Enter NUMBER of codemod templates to create: ")
        for _ in range(int(num_mods)):
            codemod_name = input("Enter CODEMOD NAME: ")
            name_list.append(codemod_name)
        print("\nPlease confirm the CODEMOD NAMES listed below: ")
        enum_print(name_list)
        correct_bool = input("\nType \'y\' to confirm or \'n\' to edit: ")
        if correct_bool.lower().startswith('y'): break
    
    return name_list

def get_language_name() -> str:
    while True:
        language = input("Enter LANGUAGE name: ")
        print("\nPlease confirm the LANGUAGE name below:")
        print("Language:", language)
        correct_bool = input("\nType \'y\' to confirm or \'n\' to edit: ")
        if correct_bool.lower().startswith('y'): break
    return language



def get_framework_name() -> str:
    return ""

def get_dest_ver_name() -> str:
    return ""

def get_description() -> str:
    return ""

def get_engine_name() -> str:
    while True:
        engine_name = input("Enter ENGINE name: ")
        print("\nPlease confirm the ENGINE name below:")
        print("Engine:", engine_name)
        correct_bool = input("\nType \'y\' to confirm or \'n\' to edit: ")
        if correct_bool.lower().startswith('y'): break
    return engine_name

def get_version_name() -> str:
    return ""

def get_file_ext() -> str:
    return ""

def get_owner_name() -> str:
    while True:
        owner_name = input("Enter codemod OWNER name: ")
        print("\nPlease confirm the OWNER name below:")
        print("Owner:", owner_name)
        correct_bool = input("\nType \'y\' to confirm or \'n\' to edit: ")
        if correct_bool.lower().startswith('y'): break
    return owner_name
    




if __name__ == "__main__":
    main()