# reading adnd writing files file-input-file-output

# a simple idea is to direct printout to a file
# fout is a common name for file output object
# 'w' will (over)write the file 'a' will append to the file. 't' is for text (the default)
fout = open('log.txt', 'at') 
print('warning - lots of interesting loggy stuff', file=fout)
fout.close() # clean up when done

# we can write to a file a bit at a time
long_str = '''we can use a while loop to automatically close any open file access objects
This saves us doing it explicitly'''
try:
    fout   = open('other.txt', 'xt') # 'a' to append, 'x' for exclusive access
    size   = len(long_str)
    offset = 0
    chunk  = 24
    while True:
        if offset > size:
            fout.write('\n') # we need to put our own new line at the end of the file (if needed)
            break
        else:
            fout.write(long_str[offset:offset+chunk])
            offset+=chunk
except FileExistsError as err:
    print('the file already exists', err.errno)
except Exception as err:
    print(err)
finally:
    print('all done')

# next we read content in from text files via a file access object
fin = open('other.txt', 'r') # 'r' for read ('t' is the default)
# received = fin.read() # reads the entire file
received = fin.readline()+'---'+fin.readline() # reads TWO lines!
fin.close() # tidy up
print(received)

# writing and reading byte files
# we need some bytes
b = bytes( range(0, 256) )
print(b)

fout = open('bfile', 'wb') # 'wb' to (over)write bytes
fout.write(b)
fout.close()

# now read them back in
fin = open('bfile', 'rb') # 'rb' to read bytes
retrieved_b = fin.read() # read the whole file
fin.close()

print(retrieved_b)