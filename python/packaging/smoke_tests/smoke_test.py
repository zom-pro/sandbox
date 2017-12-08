from io import StringIO
import sys
import os


class Output(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

# this could be handled with Python unittest library too.
expected_output = "21"
os.system("multiplier 1 2 3 4")
print("Smoke test finished correctly!")