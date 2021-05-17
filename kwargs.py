
def foo(name: int, /, **kwargs) -> str:
    """Prints keyword arguments.

    Delimit slash to enforce that name will always be positional.
    hsiad ajdFzdf ds dsyfl sfsjs
    fdshf lsdkhlskjs s s 
    s
    gssdj gpfsghoisfh gpf;sgjs's
    gs
    gs
    gsfgj sfdljusfdgsfd'
    """
    for key in kwargs:
        print(key)

    print("annotations", foo.__annotations__)
    print(foo.__annotations__["name"] == int)
    # print(name)
    # print(type(name))

foo("afdadasd", **{"name":"v2", "k3":"v3"})

print(foo.__doc__)