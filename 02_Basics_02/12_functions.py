## parameters used when define function

def say_hello(name, emoji):
    print(f'hello {name} {emoji}')

## arguments used when call (or invoke) function
# positional arguments
say_hello('Heath', '😜')
say_hello('😎', 'Bob')

# keyword arguments
say_hello(name='Joe', emoji = '😰')

# default parameters make sure function runs even if called without arguemnts
def say_bye(name = "I'm cold", emoji = '🥶'):
    print(f'bye {name} {emoji}')

say_bye('Susan')