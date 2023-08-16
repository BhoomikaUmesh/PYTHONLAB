import heapq
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left :
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right,newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)
printNodes(nodes[0])


def decode_text(root, encoded_text):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_text += current_node.symbol
            current_node = root
    return decoded_text
encoded_text = (input("enter the code:"))
decoded_text = decode_text(nodes[0], encoded_text)
print("Decoded text:", decoded_text)


def encode_text(root, text):
    huffman_codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.symbol:
            huffman_codes[node.symbol] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    generate_codes(root)
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text
text=input("Enter text:")
encoded_text = encode_text(nodes[0], text)
print("Encoded text:", encoded_text)
