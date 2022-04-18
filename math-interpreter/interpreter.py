from parser import *
import readline

operators_handlers = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

class MathInterpreter:
    def __init__(self, parser):
        self.parser = parser

    def _visit_number_node(self, node):
        return node.value

    def _visit_binary_operator_node(self, node):
        operation_handler = operators_handlers[node.op]
        return operation_handler(self._visit(node.left), self._visit(node.right))

    def _visit(self, node):
        if node is None:
            return 0

        if isinstance(node, NumberNode):
            return self._visit_number_node(node)
        
        return self._visit_binary_operator_node(node)

    def evaluate(self):
        return self._visit(self.parser.parse())
