class Parent():
    def implicit(self):
        print('Parent implicit()')

    def override(self):
        print('Parent override()')

    def something(self):
        print('Parent something()')


class Child(Parent):
    def override(self):
        print('Child override')

    def something(self):
        super().something()
        print('Child adds something')


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.something()
son.something()