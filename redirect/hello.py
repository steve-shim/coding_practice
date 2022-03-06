'''
python hello.py 1> stdout.txt 2> stderr.txt
'''
import sys

print('[2]This message will be displayed on the screen.')

original_stdout = sys.stdout # Save a reference to the original standard output

with open('filename.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('[1]This message will be written to a file by change sys.stdout=f')
    print('[1]This is file')
    sys.stdout = original_stdout # Reset the standard output to its original value
    print('[2]This is output')
    print('[3]This is output err', file=sys.stderr)
    print('[1]This message will be written to a file by file=f', file=f)
'''
While it may appear like regular output to us, 
for the computer it is displayed through different pipelines.
'''
print('[2]This message will be displayed via standard output.')
sys.stdout = sys.stderr # Redirect the standard output to the standard error.
print('[3]This message will be displayed via the standard error.')

sys.stdout = original_stdout # Reset the standard output to its original value
print('[2]original')