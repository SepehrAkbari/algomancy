'''
Huffman coding.
'''

import heapq
import sys
from collections import Counter


class Node:
    '''
    A node in Huffman Tree.
    '''
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq 
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
class HuffmanCoder:
    '''
    Builds Huffman tree and encodes/decodes text.
    '''
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}
        self.reverse_codes = {}
        
    def _build_tree(self):
        '''
        Builds Huffman tree using min-heap.
        '''
        frequency = Counter(self.text)

        heap = [Node(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap) # converts to min-heap based on frequency

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        # remaining node is root
        if heap:
            self.root = heap[0]
            
    def _generate_codes(self, node, current_code):
        '''
        Traverses tree to generate binary codes for each character.
        '''
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")
        
    def encode(self):
        '''
        Encodes char string.
        '''
        if not self.text:
            return ""

        self._build_tree()
        self._generate_codes(self.root, "")

        encoded_text = "".join([self.codes[char] for char in self.text])
        return encoded_text
    
    def decode(self, encoded_text):
        '''
        Decodes binary string.
        '''
        if not encoded_text or not self.root:
            return ""

        decoded_text = []
        current_node = self.root

        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_text.append(current_node.char)
                current_node = self.root

        return "".join(decoded_text)
    
class CanonicalHuffman:
    """Implements Canonical Huffman Coding using the 'coin exchange' shift logic."""
    def __init__(self, symbol_lengths):
        # We start with just the symbols and their required code lengths.
        # e.g., {'A': 2, 'B': 2, 'C': 3, 'D': 3}
        self.symbol_lengths = symbol_lengths
        self.encode_table = {}
        self.decode_table = {}
        
        if self.symbol_lengths:
            self._build_tables()

    def _build_tables(self):
        """Builds the encoding and decoding tables using canonical rules."""
        
        # 1. Sort the customers (symbols)
        # Primary sort: Ascending by code length (shortest codes first)
        # Secondary sort: Alphabetically (lexicographically)
        sorted_symbols = sorted(
            self.symbol_lengths.keys(),
            key=lambda s: (self.symbol_lengths[s], s)
        )

        # 2. Count the denominations needed
        # How many 1-bit codes do we need? How many 2-bit? 
        max_length = max(self.symbol_lengths.values())
        length_counts = {i: 0 for i in range(1, max_length + 1)}
        for length in self.symbol_lengths.values():
            length_counts[length] += 1

        # 3. The "Coin Exchange" step: Calculate starting integer for each length
        # next_code[L] will store the first available binary integer for length L
        next_code = {1: 0}
        current_code_value = 0
        
        for length in range(1, max_length + 1):
            # Add the number of codes we handed out in the PREVIOUS length.
            # Then shift left (<< 1). This is the exact act of "making change" 
            # by breaking the next largest denomination into two smaller ones.
            current_code_value = (current_code_value + length_counts.get(length - 1, 0)) << 1
            next_code[length] = current_code_value

        # 4. Hand out the codes
        for symbol in sorted_symbols:
            length = self.symbol_lengths[symbol]
            
            # Format the integer into a binary string padded with leading zeros
            bin_string = format(next_code[length], f'0{length}b')
            
            # Store in our lookup tables
            self.encode_table[symbol] = bin_string
            self.decode_table[bin_string] = symbol
            
            # Increment the integer so the next symbol of the SAME length 
            # gets the next sequential serial number.
            next_code[length] += 1

    def encode(self, text):
        """Encodes text instantly using the O(1) hash map."""
        return "".join([self.encode_table[char] for char in text])

    def decode(self, binary_string):
        """Decodes binary string back to text."""
        decoded_text = []
        current_bits = ""
        
        for bit in binary_string:
            current_bits += bit
            # Check if our current buffer matches a known code
            if current_bits in self.decode_table:
                decoded_text.append(self.decode_table[current_bits])
                current_bits = "" # Reset for the next character
                
        return "".join(decoded_text)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "canonical":
        required_lengths = {
            'C': 3,
            'A': 2,
            'D': 3,
            'B': 2
        }
        
        coder = CanonicalHuffman(required_lengths)

        print("Canonical Code Assignments:")
        for symbol, code in coder.encode_table.items():
            print(f"Symbol: {symbol} | Length: {required_lengths[symbol]} | Code: {code}")
    else:
        sample_text = "AABCBAD"
        print(f"Original: '{sample_text}'\n")

        coder = HuffmanCoder(sample_text)

    encoded_data = coder.encode()
    print(f"Encoded: {encoded_data}")
    print(f"Code Dictionary: {coder.codes} \n")

    decoded_data = coder.decode(encoded_data)
    print(f"Decoded: '{decoded_data}'\n")

    original_bits = len(sample_text) * 8 # ASCII
    encoded_bits = len(encoded_data)
    print(f"Original size: {original_bits} bits")
    print(f"Compressed size: {encoded_bits} bits")