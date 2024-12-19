# AUTHOR: John Nico T. De Castro
# CREATION DATE: 12/18/2024
# DESCRIPTION: A program that simulates huffman coding. Resource used: 3.4 Huffman Coding - Greedy Method by Abdul Bari (https://youtu.be/co4_ahEDCho?si=hJHv_8oR1EsTGHGG).

import math

class Node:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.left = None
        self.right = None
        
    def setLeftRight(self, left, right):
        self.left = left
        self.right = right
        

def get_min_node(nodes):
    min_node = None
    for node in nodes:
        if min_node == None or node.count < min_node.count:
            min_node = node
    return min_node
            

def preorder_traversal(head, code, codes):
    if head.left != None:
        preorder_traversal(head.left, code+'0', codes)
        
    if head.left == None and head.right == None:
        codes.append(code)
    
    if head.right != None:
        preorder_traversal(head.right, code+'1', codes)


def huffman_coding(message):
    '''Performs coding by frequency (least-most) with variable-size codes
    '''
    # generate freq table
    # char | freq
    freqs = {}
    num_chars = 0
    
    for char in message:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    num_chars = len(freqs.keys())

    # sort
    freqs = {key: val for key, val in sorted(freqs.items(), key=lambda ele: ele[1])}

    # calculate # of bits required
    bits = math.ceil(math.log(num_chars, 2))
    if bits == 0:       # To handle 1 character messages
        bits = 1

    # generate coding table
    coding = []

    coding.append([key for key in freqs.keys()])
    coding.append([val for val in freqs.values()])
    
    nodes = [Node(key, val) for key, val in freqs.items()]
    
    while len(nodes) != 1:
        min_node_1 = get_min_node(nodes)
        insert_index_1 = nodes.index(min_node_1)
        nodes.remove(min_node_1)
        min_node_2 = get_min_node(nodes)
        insert_index_2 = nodes.index(min_node_2)
        nodes.remove(min_node_2)
        
        if insert_index_1 > insert_index_2:
            min_node_1, min_node_2 = min_node_2, min_node_1
            insert_index_1, insert_index_2 = insert_index_2, insert_index_1
        
        new_node = Node(None, min_node_1.count+min_node_2.count)
        new_node.setLeftRight(min_node_1, min_node_2)
        
        nodes.insert(insert_index_1, new_node)
        
    tree_head = nodes[0]
    
    # do preorder traversal and save codes
    saved_codes = []
    preorder_traversal(tree_head, '', saved_codes)

    if len(saved_codes) == 1:
        saved_codes = ['0']

    # add codes, current format: [[char, ...], [count, ...], [code, ...]]
    coding.append([code for code in saved_codes])
    
    # convert to [[char, count, code], ...]
    coding_table = []
    for i in range(num_chars):
        coding_table.append([coding[0][i], coding[1][i], coding[2][i]])
        
    # sort by alpha
    coding_table = sorted(coding_table, key=lambda ele: ele[0])
    
    # # print the table
    print()
    print("Character".ljust(15), "|", "Count".ljust(15), "|", "Code".ljust(15))
    for i in range(num_chars):
        print(str(coding_table[i][0]).ljust(15), "|", str(coding_table[i][1]).ljust(15), "|", str(coding_table[i][2]).ljust(15))
    print()
        
    # print equivalent of message in the coding scheme
    message_code = []
    for m_char in message:
        for i in range(num_chars):
            if coding_table[i][0] == m_char:
                message_code.append(coding_table[i][2])

    print("Message:")
    for char in message:
        print(char.ljust(bits+1), end="")
    print()
    print("Coded Message:")
    for code in message_code:
        print(code.ljust(bits+1), end="")
    print()
    
    # # print size
    print()
    message_size = 0
    for i in range(num_chars):
        message_size += coding_table[i][1] * len(coding_table[i][2])
    table_size = num_chars*8+sum([len(code) for code in saved_codes])
    print("Size of Message:", message_size)
    print("Size of Table:", table_size)     # ASCII chars are encoded in 8 bits
    print("Total size of Message:", message_size+table_size)
    print()


def non_huffman_coding(message):
    '''Performs coding alphabetically with fixed-size codes
    '''
    # generate freq table
    # char | freq
    freqs = {}
    num_chars = 0
    
    for char in message:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    num_chars = len(freqs.keys())

    # sort
    freqs = {key: val for key, val in sorted(freqs.items(), key=lambda ele: ele[0])}

    # calculate # of bits required
    bits = math.ceil(math.log(num_chars, 2))
    if bits == 0:       # To handle 1 character messages
        bits = 1

    # generate coding table
    coding = []

    coding.append([key for key in freqs.keys()])
    coding.append([val for val in freqs.values()])
    coding.append([])
    print("Num Chars:", num_chars)
    print("Bits required:", bits)
    for i in range(num_chars):
        code = []
        
        while i != 0:
            code.insert(0, str(i % 2))
            i = i // 2
        
        while len(code) != bits:
            code.insert(0, '0')
        
        coding[2].append(''.join(code))

    # print the table
    print()
    print("Character".ljust(15), "|", "Count".ljust(15), "|", "Code".ljust(15))
    for i in range(num_chars):
        print(str(coding[0][i]).ljust(15), "|", str(coding[1][i]).ljust(15), "|", str(coding[2][i]).ljust(15))
    print()
        
    # print equivalent of message in the coding scheme
    message_code = []
    for m_char in message:
        for i in range(num_chars):
            if coding[0][i] == m_char:
                message_code.append(coding[2][i])

    print("Message:")
    for char in message:
        print(char.ljust(bits+1), end="")
    print()
    print("Coded Message:")
    print(" ".join(message_code))
    
    # print size
    print()
    message_size = len(message)*bits
    table_size = num_chars*8+num_chars*bits
    print("Size of Message:", message_size)
    print("Size of Table:", table_size)     # ASCII chars are encoded in 8 bits
    print("Total size of Message:", message_size+table_size)
    print()


def main():
    message = 'BCCABBDDAECCBBAEDDCC'
    while True:
        print(f"1. New Message (Default: {message})")
        print("2. Huffman Coding")
        print("3. Non-huffman Coding")
        print("4. Exit")
        try:
            choice = int(input("\nEnter choice: "))
        except:
            print("\nInvalid input")
            break
        if choice == 1:
            message = input("Enter new message: ")
        elif choice == 2:
            huffman_coding(message)
        elif choice == 3:
            non_huffman_coding(message)
        elif choice == 4:
            break
        else:
            print("Invalid input\n")
        

if __name__ == "__main__":
    main()