from .dump import dump  # noqa: F401


def show_messages(messages, title=None, functions=None):
    if title:
        print(title.upper(), "*" * 50)

    for msg in messages:
        role = msg["role"].upper()
        if content := msg.get("content"):
            for line in content.splitlines():
                print(role, line)
        if content := msg.get("function_call"):
            print(role, content)

    if functions:
        dump(functions)
