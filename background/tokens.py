token_patterns = [
    (r'\b(int|float|char|void)\b', 'KEYWORD'),    # Keywords
    (r'\b(if|else|while|for)\b', 'CONTROL'),       # Control structures
    (r'\b(return)\b', 'RETURN'),                    # Return keyword
    (r'\b(\d+(\.\d+)?)\b', 'NUMBER'),               # Numbers
    (r'\b(\w+)\b', 'IDENTIFIER'),                   # Identifiers
    (r'[-+*/=<>]', 'OPERATOR'),                     # Operators
    (r'\b(\w+)\s*\(', 'FUNCTION'),                  # Function names
    (r'[;,\(\)\{\}]', 'PUNCTUATION'),               # Punctuation
    (r'"(.*?)"', 'STRING'),                         # Strings
    (r'//.*?$|/\*[\s\S]*?\*/', 'COMMENT'),         # Comments
    (r'\s+', None)                                  # Ignore whitespace
]