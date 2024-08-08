'''
This moudle provides to say hello for some people
'''

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """
    say_hello function
        It say hello for some peoples
        parameters:
        some_peoples => list of peoples that use in function
        print: the hello + name of the some one
    """
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(myFriends)
