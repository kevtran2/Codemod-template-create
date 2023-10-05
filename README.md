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
