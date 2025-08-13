def write_file(filename, content):
    with open(filename, 'w') as f: #"""Writes content to a file, overwriting existing content"""
        f.write(content)

def append_file(filename, content):
  with open(filename, 'a') as f: # """Appends content to a file"""
        f.write(content + '\n')

def read_file(filename):
   with open(filename, 'r') as f: #"""Reads and returns file contents"""
        return f.read()

# Test the file operations
#write_file("logfile.txt", "Log 1: bananas added")
#append_file("logfile.txt", "Log 2: bananas subtracted")
#print(read_file("logfile.txt"))
