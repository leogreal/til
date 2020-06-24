print('Strings')

name = 'leonardo gregório de almeida'
print('title', name.title())
print('upper', name.upper())
print('lower', name.lower(), '\n')

print('==>', 'Template string')
first_name = 'Leonardo'
last_name = 'Gregório de Almeida'
full_name = f'{first_name} {last_name}'
print(full_name, '\n')

print('==>', 'Spaces and tab')
print('Python')
print('\tPython', '\n')
print('Languages:\nPython\nC\nJavascript', '\n')
print('Languages:\n\tPython\n\tC\n\tJavascript', '\n')

print('==>', 'removing blanks')
name = '  Leonardo  '
print(name)
print('rstrip', name.rstrip())
print('lstrip', name.lstrip())
print('strip ', name.strip())


