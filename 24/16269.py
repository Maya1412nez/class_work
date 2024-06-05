s, nafig, nado = open('24/16269.txt').readline(), 'TUVW', 'XYZ'
for letter in nafig: s = s.replace(letter, ' ')
for letter in nado: s = s.replace(letter * 4, letter * 2 + ' ' + letter * 2).replace(letter * 3, letter * 2 + ' ' + letter * 2).replace(letter * 2, 'GG').replace(letter, ' ')
print(max(list(map(len, s.split()))))