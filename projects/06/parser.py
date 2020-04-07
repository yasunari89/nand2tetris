class Parser:
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            raw_lines = f.readlines()

            self.lines = []
            for line in raw_lines:
                comment_index = line.find('//')
                if comment_index != -1:
                    line = line[:comment_index]
                line = line.strip()
                if line == '':
                    continue
                self.lines.append(line)
            
            self.max_index = len(self.lines) - 1
            self.current_index = 0
            self.command = self.lines[self.current_index]
    

    def has_more_commands(self):
        if self.current_index < self.max_index:
            return True
        else:
            return False
    

    def advance(self):
        if self.has_more_commands():
            self.current_index += 1
            self.command = self.lines[self.current_index]
        else:
            raise ValueError('NO ADVANCE ERROR')
    

    def command_type(self):
        if self.command[0] == '@':
            return 'A_COMMAND'
        elif self.command[0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'
    
    
    def symbol(self):
        if self.command_type() == 'A_COMMAND':
            return self.command[1:]
        elif self.command_type() == 'L_COMMAND':
            return self.command[1:-1]
        else:
            raise ValueError('NOT A OR L COMMAND')


    def dest(self):
        if self.command_type() != 'C_COMMAND':
            raise ValueError('NOT C COMMAND')
        else:
            equal_index = self.command.find('=')
            if equal_index != -1:
                dest = self.command[:equal_index]
                self._comp = self.command[equal_index+1:]
                return dest
            else:
                return None


    def jump(self):
        if self.command_type() != 'C_COMMAND':
            raise ValueError('NOT C COMMAND')
        else:
            jump_index = self.command.find(';')
            if jump_index != -1:
                jump = self.command[jump_index+1:]
                self._comp = self.command[:jump_index]
                return jump 
            else:
                return None
    

    def comp(self):
        if self.dest():
            return self._comp
        elif self.jump():
            return self._comp
