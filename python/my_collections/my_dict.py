class MyDict():
    def __init__(self, default_value):
        # default value to be used when key isn't found.
        self.default_value = default_value
        self._d = dict()
    def __setitem__(self, key, value):
        return self._d.__setitem__(key, value)
    def __getitem__(self, key):
        try:
            return self._d.__getitem__(key)
        except KeyError:
            return self.default_value
            
    def __delitem__(self, key):
        return self._d.__delitem__(key)