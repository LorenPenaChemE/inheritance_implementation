"""
Inheritance implementation
Loren Pena
Purpose of this assignment is to create logic gates using a inheritance architecture
"""
class Input:
    """
    One object of this class represents a Input for a logic gate.
    """
    def __init__(self, owner):
        if isinstance(owner, LogicGate) is not True:
            raise TypeError
        else:
            self._owner = owner
        self._value = None

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_input_value):
        self._value = new_input_value
        self._owner.evaluate()

    def __str__(self):
        if self._value == None:
            return "(not set)"
        else:
            return self._value


class OutPut:
    """
    One object of this class represents an output of a logic gate.
    """
    def __init__(self):
        self._value = None
        self._connections = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_ouput_value):
        self._value = new_ouput_value

        for input in self._connections:
            input.value = self._value

    @property
    def get_connections(self):
        return self._connections

    def connect(self, input):
        if isinstance(input, Input) is not True:
            raise TypeError("Not an instance of Input")
        if input in self._connections:
            raise TypeError("Pin is full")
        else:
            self._connections.append(input)



    def __str__(self):
        if self._value is None:
            return "(not set)"
        else:
            return self._value


class LogicGate:
    """
    One object of this class represents a Logic Gate
    """
    def __init__(self, name):
        self._name = name
        self.output = OutPut()

    @property
    def getLabel(self):
        return self._name

    @property
    def getOutPut(self):
        self.output._value = self.evaluate()
        return self.output._value

    def __str__(self):
        if self.getOutPut == None:
            return f" output = (not set)"
        else:
            return f" output = {self.getOutPut}"

class BinaryGate(LogicGate):
    """
    One object of this class represents a logic gate that has two inputs.
    """
    def __init__(self, name):
        super().__init__(name)
        self.input0 = Input(self)
        self.input1 = Input(self)

    @property
    def get_input0(self):
        if self.input0.value == None:
            return "(not set)"
        else:
            return self.input0.value
    @property
    def get_input1(self):
        if self.input1.value == None:
            return "(not set)"
        else:
            return self.input1.value

    def __str__(self):
        return f"Gate {self.getLabel}: input0 = {self.get_input0} input1 = {self.get_input1}" + super().__str__()

class UranaryGate(LogicGate):
    """
    One object of this class represents a logic gate that has one input
    """
    def __init__(self, name):
        super().__init__(name)

        self.input = Input(self)
    @property
    def get_input(self):
        if self.input.value == None:
            return "(not set)"
        else:
            return self.input._value

    def __str__(self):
        return f"Gate {self.getLabel}: input = {self.get_input}" + super().__str__()

class NotGate(UranaryGate):
    """
        One object of this class represents a Not Gate
    """
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self):
        logic = self.get_input
        if logic == True:
            return False
        elif logic == False:
            return True


class AndGate(BinaryGate):
    """
        One object of this class represents a And Gate.
    """
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self):
        input0 = self.get_input0
        input1 = self.get_input1

        if input0 == "(not set)" or input1 == "(not set)":
            return None
        elif input0 == True and input1 == True:
            return True
        else:
            return False


class NandGate(AndGate):
    """
        One object of this class represents a Nand Gate
    """
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self):
        andResult = super().evaluate()
        if andResult==True:
            return False
        elif andResult == False:
            return True
        else:
            return None

class OrGate(BinaryGate):
    """
        One object of this class represents a Or Gate.
    """

    def __init__(self, name):
        super().__init__(name)

    def evaluate(self):

        input0 = self.get_input0
        input1 = self.get_input1

        if input0 == "(not set)" or input1 == "(not set)":
            return None
        elif input0 == True or input1 == True:
            return True
        else:
            return False

class NorGate(OrGate):
    """
        One object of this class represents a Nor Gate.
    """
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self):
        orResult = super().evaluate()
        if orResult == True:
            return False
        elif orResult == False:
            return True
        else:
            return None

if __name__ == '__main__':
    not_gate1 = NotGate("not1")
    not_gate1.input.value = False
    print(not_gate1)

    not_gate2 = NotGate("not2")
    not_gate1.output.connect(not_gate2.input)
    print("After connect:")
    print(not_gate1)
    print(not_gate2)

    not_gate1.input.value = True
    print("After setting input to True:")
    print(not_gate1)
    print(not_gate2)