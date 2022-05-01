import unittest
from Inheritance implementation import *

class Assignment4tst(unittest.TestCase):
    def test_NotGate_gate_notset(self):
        n1 = NotGate("N1")
        self.assertIsNone(n1.output.value, None)
    def test_NotGate_gate_set_False(self):
        n1 = NotGate("N1")
        n1.input.value = True
        self.assertFalse(n1.output.value, False)
    def test_NotGate_gate_set_True(self):
        n1 = NotGate("N1")
        n1.input.value = False
        self.assertTrue(n1.output, True)

    def test_NotGate_output_connection(self):
        not_gate1 = NotGate("not1")
        not_gate1.input.value = False
        not_gate2 = NotGate("not2")
        not_gate1.output.connect(not_gate2.input)
        self.assertTrue(not_gate2.output, True)

    def test_NotGate_output_connection_after_input_change(self):
        not_gate1 = NotGate("not1")
        not_gate1.input.value = False
        not_gate2 = NotGate("not2")
        not_gate1.output.connect(not_gate2.input)
        not_gate1.input = True
        self.assertTrue(not_gate2.output, True)

    def test_AndGate_gate_notset(self):
        andgate = AndGate("and1")
        self.assertIsNone(andgate.output.value, None)
    def test_AndGate_set_False(self):
        andgate = AndGate("and1")
        andgate.input0.value = False
        andgate.input1.value = True
        self.assertFalse(andgate.output.value)
    def test_AndGate_set_True(self):
        andgate = AndGate("and1")
        andgate.input0.value = True
        andgate.input1.value = True
        self.assertTrue(andgate.output)
    def test_NandGate_not_gate_notset(self):
        Nandgate = NandGate("Nand1")
        self.assertIsNone(Nandgate.output.value, None)
    def test_NandGate_set_True(self):
        Nand = NandGate("Nand1")
        Nand.input0.value = False
        Nand.input1.value = False
        self.assertFalse(Nand.output.value)
    def test_NandGate_set_False(self):
        Nand = NandGate("Nand1")
        Nand.input0.value = True
        Nand.input1.value = True
        self.assertFalse(Nand.output.value)
    def test_Or_gate_notset(self):
        or1 = OrGate("or1")
        self.assertIsNone(or1.output.value, None)

    def test_Or_gate_set_true(self):
        or1 = OrGate("or1")
        or1.input1.value = True
        or1.input0.value = True
        self.assertTrue(or1.output, True)

    def test_Or_gate_set_False(self):
        or1 = OrGate("or1")
        or1.input1.value = False
        or1.input0.value = False
        self.assertFalse(or1.output.value, False)

    def test_Nor_gate_set_true(self):
        Nor1 = NorGate("Nor1")
        Nor1.input1.value = True
        Nor1.input0.value = True
        self.assertFalse(Nor1.output.value, False)

    def test_Nor_gate_set_False(self):
        Nor1 = NorGate("Nor1")
        Nor1.input1.value = False
        Nor1.input0.value = False
        self.assertTrue(Nor1.getOutPut, True)
