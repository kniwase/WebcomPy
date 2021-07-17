from typing import Any, Type
from javascript import RegExp, String


pattern = RegExp.new(r'[A-Z]+', 'g')


def replacer(match: str, *_: str) -> str:
    return '-' + match.lower()


def convert_camel_to_kebab(text: str):
    return String.new(text).replace(pattern, replacer).strip('-')


def get_component_class_name(component: Type[Any]) -> str:
    return component.__bases__[-1].__name__


def get_component_tag_name(component: Type[Any]) -> str:
    class_name = get_component_class_name(component)
    tag_name = convert_camel_to_kebab(class_name)
    return tag_name
