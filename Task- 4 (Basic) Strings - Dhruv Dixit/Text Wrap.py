import textwrap

def wrap(string, max_width):
    t=textwrap.wrap(string,max_width)
    s=""
    for i in t:
        s=s+i+"\n"
    return s
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)