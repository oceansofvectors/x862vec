from pwn import *
import os


class Binary:
    def __init__(self, filepath):
        self.filepath = filepath
        self.elf = ELF(self.filepath)

    def size(self):
        return os.path.getsize(self.filepath)

    def stripped(self):
        return bool(len(self.elf.functions))

    def get_function_assembly(self, func_name: str) -> str:
        return self.elf.functions.get(func_name).disasm()

    def assembly(self) -> str:
        data = ''
        for function in self.elf.functions:
            function_asm = self.elf.functions.get(function).disasm()
            data = data + function_asm
        return data
