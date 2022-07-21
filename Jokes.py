from jokeapi import Jokes # Import the Jokes class

"""fix yelling at me error"""
from functools import wraps

from asyncio.proactor_events import _ProactorBasePipeTransport


def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise

    return wrapper


_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
"""fix yelling at me error end"""


async def print_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        return joke["joke"]
    else:
        return joke["setup"] + "\n" + joke["delivery"]

