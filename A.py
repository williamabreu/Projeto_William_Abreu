class A:
    def __init__(self, A1: int, A2: float):
        self.A1 = A1
        self.A2 = A2
    
    def get_A1(self):
        return self.A1
    
    def get_A2(self):
        return self.A2
    
    def set_A1(self, A1: int):
        self.A1 = A1
    
    def set_A2(self, A2: float):
        self.A2 = A2
    
    def MA1(self):
        print('MA1')
    
    def MA2(self):
        print('MA2')
