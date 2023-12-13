class AssemblyGenerator:
    def __init__(self):
        self.assembly_code = []

    def translate(self, ast):
        self.assembly_code.append(f"\t.file\t\"return_2.c\"")
        self.assembly_code.append("\t.text")
        self.assembly_code.append("\t.globl\tmain")
        self.assembly_code.append("\t.type\tmain, @function")
        self.assembly_code.append("main:")
        
        self.translate_statement(ast.children[0])

        self.assembly_code.append("\t.size\tmain, .-main")
        self.assembly_code.append('\t.ident\t"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"')
        self.assembly_code.append('\t.section\t.note.GNU-stack,"",@progbits')

    def translate_statement(self, node):
        self.translate_expression(node.children[0])
        self.assembly_code.append("\tret")

    def translate_expression(self, node):
        value = node.value
        self.assembly_code.append(f"\tmovl\t${value}, %eax")