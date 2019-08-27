import queue as qu


def encode(input_str, i_series):
    temp = qu.Queue()
    output_str = ""
    index = 0
    for c in input_str:
        temp.enqueue(ord(c)+i_series[index])
        output_str += chr(temp.dequeue())
        index += 1
        if index == len(i_series):
            index = 0
    return output_str


def decode(input_str, i_series):
    temp = qu.Queue()
    output_str = ""
    index = 0
    for c in input_str:
        temp.enqueue(ord(c)-i_series[index])
        output_str += chr(temp.dequeue())
        index += 1
        if index == len(i_series):
            index = 0
    return output_str
