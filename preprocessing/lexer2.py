#!/usr/bin/env python

import re
import sys
sys.path.insert(0, '/home/nicktagliamonte/background')
from tokens import token_patterns

def tokenize_c_code(code):
    tokens = []
    pos = 0

    while pos < len(code):
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code[pos:])
            if match:
                if token_type:
                    if token_type != 'COMMENT':
                        tokens.append((token_type, match.group(0)))
                pos += match.end()
                break
        else:
            raise ValueError(f"Cannot tokenize: {code[pos:]}")

    return tokens

def tokenize_c_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if not line.strip().startswith('//')]
        c_code = '\n'.join(lines)

    return tokenize_c_code(c_code)

def generate_tokens(file):
    return tokenize_c_file(file)

generate_tokens(sys.argv[1])