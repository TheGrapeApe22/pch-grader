# hi anuraag
`pch-grader` is a utilitarian enterprise I have instituted and adapted in order to facilitate the grueling and laborious drudgery of inscribing credits earned by the fellow apprentices of Mrs. Jaehnig.  It is a pinnacle of computational engineering, serving as a robust and efficacious instrument that fulfills the gratifying human necessity to automate perfunctory undertakings.

Okay, but really, it's a Python program that stores students' scores on assignments and can output them in a format that's easy to transcribe to the gradebook.

## How to Use
1. Set the correct period roster in the first line of `grader3.py`.
   - The line looks like this by default: `roster_path = 'p2 roster.txt'`
   - The rosters for other periods are available in the repo as well.
2. Run `grader3.py` with python3 and enter lines in this format: [name or initials] [score]
   - The score will default to 5 if not entered.
   - Currently, it only reads the first token of the line as the name, I'll fix this later to allow searching with spaces.
   - If a search gets zero or more than one result, it'll alert you in red text with more details to clarify.

3. Finally, type "generate" to write an output file to out.txt.
   - A few other keywords work too, you might be able to find them in the source code :P

 ## Grading multiple assignments at a time
 - The program stores only one score per student, meaning you need to rerun it for each individual assignment.
 - An easy workaround for this is to have a different text file listing the scores of each assignment, and run the program separately / collect the output using each text file as input.
   - Make sure your multi-line command ends with a newline, or else the last line won't register.

Message me (Discord: ```@thegrapeape22```) if you have further questions.

No AI or Large Language Models were used in creating any part of this project.
#### written with pycharm
