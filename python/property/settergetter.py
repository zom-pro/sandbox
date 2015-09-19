class SetterGetter():
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        print('x\'s value has been set to {0} and can\'t be changed'.format(self._x))

    @x.getter
    def x(self):
        print('prepare to catch x\'s value!')
        return self._x

if __name__ == '__main__':
    settergetter = SetterGetter(10)
    print(settergetter.x)

    settergetter.x = 5
    print(settergetter.x)