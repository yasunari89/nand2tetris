class SymbolTable:
    def __init__(self):
        self.symbol_table = []
    

    def add_entry(self, symbol, address):
        self.symbol_table.append((symbol, address))
    

    def contains(self, symbol):
        for entry in self.symbol_table:
            if symbol == entry[0]:
                return True 
        return False 
    

    def get_address(self, symbol):
        for entry in self.symbol_table:
            if symbol == entry[0]:
                return entry[1]
        return None