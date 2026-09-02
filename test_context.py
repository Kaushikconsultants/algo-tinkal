import inspect
from dhanhq import DhanContext

try:
    print("DhanContext signature:")
    print(inspect.signature(DhanContext.__init__))
except Exception as e:
    print(e)
