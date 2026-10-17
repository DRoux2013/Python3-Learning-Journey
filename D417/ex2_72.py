"""# 1. Open and write to the file
f = open('file1.txt', 'w+')
for i in range(3):
    f.write('This is line %d.\n' % (i + 1))

f.close()

# 2. Read and print contents
f = open('file1.txt')
f_read = f.read()
print(f_read)
f.close()"""

# 3. Alternative method
with open('file1.txt', 'r') as f:
    f_read = f.read()
    print(f_read)