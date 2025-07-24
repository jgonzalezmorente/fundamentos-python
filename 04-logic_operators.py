# and
age = 16
licesend = True

if age >= 18 and license:
    print('Puedes manejar')

# or
is_student = False
membership = False

if is_student or membership:
    print('Obtiene precio especial')

# not
is_admin = False

if not is_admin:
    print('Acceso denegado')

# Short Circuiting
name = None
print(name and name.upper())