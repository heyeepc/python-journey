scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 60, 'Eve': 95}
passed_students = {name: 'Passed' for name, score in scores.items() if score >= 80}
print(passed_students)
