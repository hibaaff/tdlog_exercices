"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
def processLines(lines) -> str:
    # Lecture des données d'entrée
    N = int(lines[0])  # Nombre de sprints
    T = int(lines[1])  # Nombre de tâches dans le backlog initial
    
    # Initialisation du backlog avec T tâches
    backlog = T
    
    # Boucle sur les N sprints pour mettre à jour le backlog
    for i in range(2, 2 + N):
        V, U = map(int, lines[i].split())  # V est le nombre de tâches validées, U est la variation du backlog
        backlog -= V  # Retirer les tâches validées
        backlog += U  # Ajuster avec les tâches ajoutées ou supprimées
    
    # Si le backlog est vide, on retourne "OK", sinon "KO"
    return "OK" if backlog == 0 else "KO"