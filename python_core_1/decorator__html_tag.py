def html_tag(tag: str):
    def inner(func):
        def wrapper (name: str) -> str:
            new_str = f"<{tag}>{func(name)}</{tag}>"
            return new_str
        return wrapper
    return inner

            
@html_tag("div")
def greeter(name: str) -> str:
    return f"Hello, {name}!"
