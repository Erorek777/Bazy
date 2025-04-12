from typing import Annotated

Capital = Annotated[str,'First latter is capital letter']

name: Capital = 'imię'
print(type(name))
print(name)

def test(name: Capital):
    return name.capitalize()

print(test.__annotations__['name'].__meteadata__)



