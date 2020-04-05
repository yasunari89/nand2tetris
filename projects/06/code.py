class Code:
    def dest(self, mnemonic):
        dest_dict = {
            None: '000', 
            'M': '001', 
            'D': '010', 
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
        }
        for dest in dest_dict:
            if mnemonic == dest:
                return dest_dict[dest]
        raise ValueError('NO DEST MNEMONIC')
    

    def comp(self, mnemonic):
        comp_dict = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            'M': '1110000',
            '!D': '0001100',
            '!A': '0110001',
            '!M': '1110001',
            '-D': '0001111',
            '-A': '0110011',
            '-M': '1110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'M+1': '1110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'M-1': '1110010',
            'D+A': '0000010',
            'D+M': '1000010',
            'D-A': '0010011',
            'D-M': '1010011',
            'A-D': '0000111',
            'M-D': '1000111',
            'D&A': '0000000',
            'D&M': '1000000',
            'D|A': '0010101',
            'D|M': '1010101'
        }
        for comp in comp_dict:
            if mnemonic == comp:
                return comp_dict[comp]
        raise ValueError('NO COMP MNEMONIC')


    def jump(self, mnemonic):
        jump_dict = {
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'        
        }
        for jump in jump_dict:
            if mnemonic == jump:
                return jump_dict[jump]
        raise ValueError('NO JUMP MNEMONIC')