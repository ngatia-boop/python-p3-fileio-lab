def write_file(filename, content):
    """Writes content to a file, overwriting existing content"""
    with open(filename, 'w') as f:
        f.write(content)

def append_file(filename, content):
    """Appends content to a file"""
    with open(filename, 'a') as f:
        f.write(content + '\n')

def read_file(filename):
    """Reads and returns file contents"""
    with open(filename, 'r') as f:
        return f.read()

# Test the file operations
write_file("logfile.txt", "Log 1: bananas added")
append_file("logfile.txt", "Log 2: bananas subtracted")
print(read_file("logfile.txt"))
