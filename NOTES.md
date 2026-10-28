# NOTES: Three Layers

Your name: Mariah Mitchell

Fill each TODO. Write plain, short sentences. Do not delete the headings.

## Part 1. Predict, then find [S1]

Write your prediction before you open any code. Then search. In the last column, write each file the search finds and what that file does.

| Action | Search word | My prediction (file) | Files found and what each does |
|---|---|---|---|
| Prints "Not yet. Try again." | `Not yet` | app.py | app.py |
| Decides that the second miss shows the answer | `reveal` | dataman/logic.py | dataman/logic.py |
| Saves one attempt | `save_attempt` | dataman/store.py | dataman/store.py|
| Refuses the 11th problem | `SetFull` | dataman/logic.py | dataman/logic.py |

Search command: `grep -rn "SEARCH WORD" --include=*.py .`

## Part 2. What the program remembered [S1]

After the restart, what did the program remember? The program saved one attempt before the interruption.

Which file made that possible? dataman_store.json

## Part 3. The interface change [S1]

What did you change in `app.py`? I reprhased the incorrect answer output message.

Why did no test need to change? I only changed the output message, which does not affect the program or any calculations.

## Part 4. The rule in the real library [S2]

The same 10-problem rule exists in the real library. Write the file and the function name. dataman/logic.py and add_problem.

## Part 5. The red test [S2]

With the rule removed from the library, what did the screen show? The screen showed: Problem id to add. Added Set holds from 1 - 11. Failed: DID NOT RAISE <class ' dataman.logic.SetFull'>

With the rule removed, which test failed? I think the maximum number of problems will fail because it might pass 10 problems.

## Part 6. The data swap [S2]

A real database would replace which file? dataman_store.json

Which file holds the rules and does not change when the database changes? dataman/logic.py

## Reflection [S2]

Write 3 to 5 sentences. Pick one layer. Say what you changed in it. Say what stayed the same in the other two layers. I changed the interface layer by updating the storage option in app.py from memory to JSON. This allowed the program to save practice attempts in and resume progress after restarting. The business logic layer in stayed the same because the rules for checking answers and managing problem sets did not change. The data layer also stayed the same because it already supported JSON storage. This showed me how changing one layer can add functionality without requiring changes to the other layers.
## Beta feedback (optional)

This bonus is a beta test. Which step took longer than its time? What confused you? Write it here. Your answer helps the next class. Identifying which test failed when the maximum-size rule was removed took the longest to complete. I was a little confused about how the three layers worked together and how JSON storage allowed the program to remember practice attempts after restarting. The instructions, the chat, and running the tests helped me understand how the interface, business logic, and data layers work together.
