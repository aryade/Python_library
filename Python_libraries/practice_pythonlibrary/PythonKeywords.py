class PythonKeywords:
    def __init__(self, *args, **kwargs):
        print(f"Sample Library initialized with args: {args} and kwargs: {kwargs}")
 
    def no_arguments(self):
        print("Keyword got no arguments.")

    def one_argument(self, arg):
        print("Keyword got one argument '%s'." % arg)

    def three_arguments(self, a1, a2, a3):
        print("Keyword got three arguments '%s', '%s' and '%s'." % (a1, a2, a3))

    def one_default(self, arg='default'):
        print("Argument has value %s" % arg)

    def multiple_defaults(self, arg1, arg2='default 1', arg3='default 2'):
        print("Got arguments %s, %s and %s" % (arg1, arg2, arg3))
     
    def my_keyword(self, *args, **kwargs):
        print(f"Keyword got args: {args} and kwargs: {kwargs}")
        return "Hello World"