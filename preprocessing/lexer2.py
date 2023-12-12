#!/usr/bin/env python

import re
import sys
sys.path.insert(0, '/home/nicktagliamonte/background')
from tokens import token_patterns

def tokenize_c_code(code):
    tokens = []

    while code:
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                tokens.append((token_type, match.group(0)))
                code = code[match.end():].lstrip()
                break

    return tokens

def tokenize_c_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if not line.strip().startswith('//')]
        c_code = '\n'.join(lines)

    return tokenize_c_code(c_code)

def generate_tokens(file):
    return tokenize_c_file(file)

generate_tokens(sys.argv[1])