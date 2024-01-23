filename = 'me.obj'

s = open(filename, 'r').read()
print(s[:200])
lines = s.split('\n')
tlines = []
for line in lines:
    if line.startswith('f '):
        xs = [_.strip() for _ in line.split(' ')]
        t = 'f '
        for x in xs[1:]:
            t += x.split('/')[0] + ' '
        t = t.strip()
        tlines.append(t)
    else:
        tlines.append(line)
tlines = '\n'.join(tlines)

open('simplified-' + filename, 'w').write(tlines)
