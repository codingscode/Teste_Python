# criar objeto de data
from datetime import datetime

meutempo = datetime(2021, 2, 14)


print(f'meutempo: {meutempo}')
print(meutempo.strftime('%B'))
print(meutempo.strftime('%A'))
print(meutempo.strftime('%C'))
print(meutempo.strftime('%D'))
# experimentar:
#%A, %a, %w, %d, %b, %B, %m, %y, %Y, %H, %I, %p, %M, %S, %f, %z, %Z, %j, %U, %W, %c, %x, %X, %%, %G, %u, %V

print('------------------------')
