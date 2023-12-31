import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char, self.freq, self.left, self.right = char, freq, None, None
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(chars, freqs):
    heap = [HuffmanNode(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        combined = HuffmanNode(None, left.freq + right.freq)
        combined.left, combined.right = left, right
        heapq.heappush(heap, combined)
    
    return heapq.heappop(heap)

def build_huffman_codes(root, code='', codes={}):
    if root:
        if root.char:
            codes[root.char] = code
        build_huffman_codes(root.left, code + '0', codes)
        build_huffman_codes(root.right, code + '1', codes)

def encode_decode_string(encoded, root):
    decoded, current = '', root
    for bit in encoded:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded += current.char
            current = root
    return decoded

def get_input(message, count, data_type):
    return [data_type(input(f"{message} {i+1}: ")) for i in range(count)]

n = int(input("Enter the number of characters: "))
characters = get_input("Enter Character", n, str)
frequencies = get_input("Enter Frequency of Character ", n, float)

huffman_tree = build_huffman_tree(characters, frequencies)
huffman_codes = {}
build_huffman_codes(huffman_tree, '', huffman_codes)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(char, ":", code)

string_to_encode = input("Enter a string to encode: ")
encoded_string = ''.join(huffman_codes[char] for char in string_to_encode)
print("Encoded String is:", encoded_string)

encoded_string_to_decode = input("Enter the encoded string to decode: ")
decoded_string = encode_decode_string(encoded_string_to_decode, huffman_tree)
print("Decoded String is:", decoded_string)

