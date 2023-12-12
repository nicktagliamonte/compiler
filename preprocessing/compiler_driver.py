import sys
import os
import lexer2
from parser import Parser

def preprocess():
    input_file = sys.argv[1]
    check_extension(input_file)
    output_filename = replace_extension(input_file)
    preprocess_cmd = "gcc -E -P " + input_file + " -o " + output_filename
    run_command(preprocess_cmd)
    process(output_filename)

def check_extension(filename):
    file_components = os.path.splitext(filename)
    file_extension = file_components[1]
    if file_extension == ".c" or file_extension == ".h":
        pass
    else:
        raise Exception("Expected a .c or .h file")

def replace_extension(filename):
    file_components = os.path.splitext(filename)
    filebase = file_components[0]
    new_extension = filebase + ".i"
    return new_extension

def run_command(cmd):
    if os.system(cmd) != 0:
        raise Exception("Command failed: " + cmd)
    
def process(filename):
    tokens = lex(filename)
    parse(tokens)
    
def lex(i_filename):
    tokens = lexer2.generate_tokens(i_filename)
    return tokens

def parse(token_list):
    parser_object = Parser(token_list)
    parsed_result = parser_object.parse()
    print(parsed_result)

preprocess()