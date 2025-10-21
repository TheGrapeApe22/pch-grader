# JH = Juyoung Han, Julia Hyun

# rename assignemtns

name_width = 25
grade_width = 7

with open('../p2 roster.txt', 'r', encoding='utf-8') as file:
    lines = [line for line in file if line.strip()]

students = {}
i=0
for line in lines:
    names = line.split(' ')
    students['%s%s' % (names[1][0], names[0][0])] = {
        'name': line.strip(),
        'id': i,
        '1': '',
        '2': ''
    }
    i += 1

def write(student):
    out = ''
    out += student['name'].ljust(name_width)
    out += student['1'].ljust(grade_width)
    out += student['2'].ljust(grade_width)
    out += '\n'
    return out

def update(student):
    with open("pch grades.txt", "r") as file:
        lines = file.readlines()
    # print(students['id']+1)
    print(len(lines))
    lines[student['id']+1] = write(student)
    with open("pch grades.txt", "w") as file:
        file.writelines(lines)

def generate():
    with open("pch grades.txt", "w") as file:
        file.write('Name'.ljust(name_width))
        file.write('1'.ljust(grade_width))
        file.write('2'.ljust(grade_width))
        file.write("\n")
        for student in students.values():
            file.write(write(student))

while True:
    try:
        print('Enter {initials} {grade} {assignment=1}:\n > ', end='')
        words = input().split(' ')
        # generate
        if (words[0] == 'generate'):
            generate()
            continue
        # input grade
        words[0] = words[0].upper() # capitalize initials
        assignment = '1' if len(words) <= 2 else words[2]
        student = students[words[0]]
        student[assignment] = words[1]
        print("Assigned score %s to %s for assignment %s\n" % (words[1], student['name'], assignment))
        update(student)
    except Exception as e:
        print('Error!!!', e, ':(')
