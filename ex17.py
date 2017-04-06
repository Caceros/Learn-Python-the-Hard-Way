from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copying from %s to %s' % (from_file, to_file))

in_file = open(from_file)
data = in_file.read()

print('The unput file is %d bytes long' % len(data))

print('Does the output file exist? %r' % exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(data)

print('Done.')

out_file.close()
in_file.close()
