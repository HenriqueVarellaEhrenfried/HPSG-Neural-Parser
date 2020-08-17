def remove_newline(file_input):
    f = open(file_input, 'r+')
    new_file = [line.rstrip('\r\n') for line in f]
    f.close()
    f = open(file_input, 'w')
    f.write(" ".join(new_file))
    f.close()

f = open('./paths.txt', 'r+')
lines = [line.rstrip('\r\n') for line in f]
f.close()
for l in lines:
    remove_newline(l)
