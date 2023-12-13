import sys
import os
import lexer2
from parser import *
from assembly import *

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
    ast = parse(tokens)
    generate_assembly(ast)
    
def lex(i_filename):
    tokens = lexer2.generate_tokens(i_filename)
    return tokens

def parse(token_list):
    parser = Parser(token_list)
    ast_root = parser.parse()
    return ast_root

def generate_assembly(ast_root):
    assembly_generator = AssemblyGenerator()
    assembly_generator.translate(ast_root)
    for line in assembly_generator.assembly_code:
        print(line)

preprocess()