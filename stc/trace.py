'''
Trace loading utils
'''

def load_trace (filename, separator='\n'):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                for el in line.split(separator):
                    el = el.strip()
                    if len(el) > 0: yield el

