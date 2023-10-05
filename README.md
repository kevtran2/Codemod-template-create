# Codemod-template-create
A Codemod for the Intuita Registry requires four files:
- index.js (contains the codemod transformation logic)
- test.js (contains test cases to verify the codemod works)
- config.json (contains meta data about the codemod)
- readME.md (describes the codemod and what it does)

Copying and pasting these four files, and then editing each file to tailor to many different codemods is repetitive and time-consuming.
The goal of this repository is to create tools to save time and to streamline the process so that Codemod importation can be a smooth and enjoyable experience.

The current template-create script prompts the user for the names of each Codemod, along with information about the engine, language, and owner and creates the templates
for each Codemod. The program takes into account similarities and differences commonly shared so that developers can save time and not worry about making these tedious small edits.

# Example Demo

Here we run the template-create script. It initially asks for the number of Codemods we create and then other information like the engine, language, and owner.
<img width="438" alt="Screen Shot 2023-10-04 at 5 57 09 PM" src="https://github.com/kevtran2/Codemod-template-create/assets/44513934/93b055a9-7a47-4971-8aa5-b1b4bd5950a1">
The confirm to continue(y/n) allows user to make changes if typos were made.

<img width="459" alt="Screen Shot 2023-10-04 at 5 57 36 PM" src="https://github.com/kevtran2/Codemod-template-create/assets/44513934/88827237-ae88-494f-a5c8-44a28fca29a8">

<img width="410" alt="Screen Shot 2023-10-04 at 5 57 26 PM" src="https://github.com/kevtran2/Codemod-template-create/assets/44513934/a22ec5e4-7609-4119-bd52-cce8a6c6ec6a">



