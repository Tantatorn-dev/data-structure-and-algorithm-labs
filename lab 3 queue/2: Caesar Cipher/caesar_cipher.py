import queue as qu


def encode(input_str, i_series):
    temp = qu.Queue()

    index = 0
    for c in input_str:
        if c == ' ':
            value = ord(' ')
        else:
            value = ord(c)+i_series[index]

        # upper
        if c.isupper() and value > ord('Z'):
            value = (value - ord('Z')) + ord('A') - 1

        # lower
        if c.islower() and value > ord('z'):
            value = (value - ord('z')) + ord('a') - 1
            
        temp.enqueue(value)

        index += 1
        if index == len(i_series):
            index = 0
        

    output_str = ""
    for c in range(temp.size()):
        output_str += chr(temp.dequeue())

    return output_str


def decode(input_str, i_series):
    temp = qu.Queue()

    index = 0
    for c in input_str:
        if c == ' ':
            value = ord(' ')
        else:
            value = ord(c) - i_series[index]

        # upper
        if c.isupper() and value < ord('A'):
            value = ord('Z') + 1 - (ord('A')-value)

        # lower
        if c.islower() and value < ord('a'):
            value = ord('z') + 1 - (ord('a') - value)

        temp.enqueue(value)

        index += 1
        if index == len(i_series):
            index = 0
        
    output_str = ""
    for c in range(temp.size()):
        output_str += chr(temp.dequeue())
        
    return output_str
