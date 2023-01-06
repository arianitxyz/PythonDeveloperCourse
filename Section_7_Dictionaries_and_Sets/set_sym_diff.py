morning = ["Java", "Ruby", "C#", "Lisp", "C"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)
