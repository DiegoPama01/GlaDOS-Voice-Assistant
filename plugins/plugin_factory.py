from plugins.plugin import Plugin
from typing import Callable, Any

plugin_creation_funcs: dict[str, Callable[..., Plugin]] = {}

def register(plugin_name: str, creation_func: Callable[..., Plugin]):
    """ Register a plugin creation function """
    plugin_creation_funcs[plugin_name] = creation_func
    print(f'Registered {plugin_name}')

def unregister(plugin_name: str):
    """ Unregister a plugin creation function """
    plugin_creation_funcs.pop(plugin_name, None) 

def create(arguments:dict[str, Any])->Plugin:
    """ Create a plugin from a dictionary of arguments """
    args_copy = arguments.copy()
    print(f"args: {args_copy}")
    plugin_name = args_copy.pop('name')
    try:
        creation_func = plugin_creation_funcs[plugin_name]
        print(f"Creation funcs {creation_func}")
        print(f"Creating plugin {plugin_name}")
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown plugin type: {plugin_name}") from None