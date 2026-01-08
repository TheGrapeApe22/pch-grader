# todo: make commands take in more than just the first token. "kai n" only takes in "kai"
# 10/7/2025

print('wassup')

# get correct roster file by period
period = ''
periods = ['1', '2', '4', '5']
period = input('enter period: ')
while period not in periods:
    period = input('not found. possible periods include ' + str(periods) + '. enter period: ')

roster_path = 'p%s roster.txt' % period
funny_number = 'six seven'
generate_commands = ['generate', 'output', 'cheese', 'hi anuraag', '67', ':)', ':(']
name_width = 32

# initialize students from roster
students = []
with open(roster_path, 'r', encoding='utf-8') as f:
    roster = f.readlines()
for line in roster:
    line = line.strip()
    tokens = line.split(' ')
    students.append({
        'name': line,
        'initials': tokens[1][0] + line[0],
        'score': '-',
        'search': tokens[1] + ' ' + line
    })

def generate():
    with open('out.txt', 'w', encoding='utf-8') as out:
        out.write('Name'.ljust(name_width) + 'Score\n')
        for student in students:
            out.write(student['name'].ljust(name_width) + student['score'] + '\n')
        out.write('anuraag'.ljust(name_width) + funny_number + '\n')
    print('\033[96m' + 'out.txt :)' + '\033[0m')

def grade(student, score):
    prev = student['score']
    student['score'] = score
    print('Set score for %s from %s to %s' % (student['name'], prev, score))

def parse_grade(command):
    tokens = command.split(' ')

    # search
    search_results = []
    names = []
    for s in students:
        if tokens[0].lower() == s['initials'].lower():
            search_results.append(s)
            names.append(s['name'])
    if len(search_results) == 0:
        for s in students:
            if tokens[0].lower() in s['search'].lower():
                search_results.append(s)
                names.append(s['name'])
    # search done

    if len(search_results) == 0:
        raise Exception("no student '%s' found" % tokens[0])
    if len(search_results) > 1:
        raise Exception("multiple students found:\n " + '\n '.join(names))

    grade(search_results[0], tokens[1] if len(tokens) > 1 else '5')

while True:
    try:
        command = input('> ').strip(' ')
        if (len(command) <= 1): continue
        print('[' + command, end='] ')
        if command.lower() in generate_commands:
            generate()
        else:
            parse_grade(command)
    except Exception as e:
        print('\033[91m' + 'Error!!!', e, ':(' + '\033[0m')
