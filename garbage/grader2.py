n=34

# initialize students from roster
students = []
with open('../p2 roster.txt', 'r', encoding='utf-8') as f:
    roster = f.readlines()
for line in roster:
    line = line.strip()
    names = line.split(' ')
    students.append({
        'name': line,
        'search': line + names[1][0] + names[0][0],
        'scores': {}
    })
# initialize student scores
with open('data.txt', 'r', encoding='utf-8') as data:
    assignments = data.readline().strip().split(',')
    assignments = list(filter(None, assignments))
    for assignment in assignments:
        scores = data.readline().split(' ')
        for i in range(len(students)):
            students[i]['scores'][assignment] = scores[i]

print(students)

def create(assignment):
    if assignment in assignments:
        print('nope')
        return
    assignments.append(assignment)
    with open('data.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open('data.txt', 'w', encoding='utf-8') as data:
        data.writelines(a+',' for a in assignments)
        data.writelines(lines[1:])
    data.write('\n')
    with open('data.txt', 'a', encoding='utf-8') as data:
        for i in range(1, n):
            data.write("-1 ")
    data.write('\n')

def output():
    name_width = 25
    score_width = 16
    with open('../out.txt', 'w', encoding='utf-8') as out:
        out.write('Name'.ljust(name_width))
        for assignment in assignments:
            out.write(assignment.ljust(score_width))
        out.write('\n')
        for student in students:
            out.write(student['name'].ljust(name_width))
            for score in student['scores'].values():
                out.write(score.ljust(score_width))
            out.write('\n')

def update_data(assignment):
    with open('data.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    # find assignment number
    line_number = -1
    for i in range(len(assignments)):
        if assignment == assignments[i]:
            line_number = 2*i+3
    if line_number == -1:
        raise Exception('assignment not found')
    # edit line
    edit = ""
    for student in students:
        edit += student['scores'][assignment] + ' '
    lines[line_number] = edit

    # rewrite in data
    with open('data.txt', 'w', encoding='utf-8') as data:
        data.writelines(lines)

def grade(student, score, assignment):
    student['scores'][assignment] = score
    update_data(assignment)

prev = 'asdf'

while True:
    try:
        print('> ', end='')
        command = input()
        first = command.split(' ')[0]
        print(first == 'create')
        if first == 'create':
            create(command[len(first) + 1:])
            continue
        if first == 'output':
            output()
            continue
        # grade
        split = command.split(' ')
        print(command[len(first) + len(split[1]) + 2:])
        assignment = command[len(first) + len(split[1]) + 2:] if len(split) > 2 else prev
        prev = assignment

        student = None
        for s in students:
            if first in s['search']:
                if student is not None:
                    raise Exception('multiple students have that name')
                student = s
        if student is None:
            raise Exception('no student found')
        grade(student, split[1], assignment)
    except Exception as e:
        print('Error!!!', e, ':(')

"""
read from roster
read from raw file
create assignment
list of assignments
store (student, scores)
"""
