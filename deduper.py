# Use python ./hello.py to run a py file from cmd line
# 

print('Hello World')

# choose a delimiter, and a file
delimiter='\n\n' # \n\n is empty line
inputFile='CONTRIBUTORS.md'; # your file

# file to use
with open(inputFile, 'r') as myfile:
    # data=myfile.read().replace('\n\n', '')
    data=myfile.read().split(delimiter);
    # data=myfile.read()
    myfile.close()

# print(data)
# print(len(data))

def remove_duplicates(values):
	# this func by https://www.dotnetperls.com/duplicates-python
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

# Remove duplicates from this list.
result = remove_duplicates(data)
# print(len(result))
result='\n\n'.join(result)

# create new file with results
file=open('result.txt', 'w') # w is the mode for write, a is mode for append
file.write(result)
file.close()




