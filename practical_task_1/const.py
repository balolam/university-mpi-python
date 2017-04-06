def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)


# noinspection PyPep8Naming
class _Const(object):
    # noinspection PyMethodParameters
    @constant
    def FOO():
        return 0xBAADFACE

    # noinspection PyMethodParameters
    @constant
    def BAR():
        return 0xDEADBEEF

CONST = _Const()
