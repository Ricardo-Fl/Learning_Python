"""Functions class."""

def hello(name='persona', lastname='exposito'):
    """Function that print 'Hello World'
    name: string,
    lastname: string,
    
    return: string,
    """
    if name != 'persona':
        return f'¿Cómo estas {name}?'
    return f'Hola {name} {lastname}'

print(hello())
