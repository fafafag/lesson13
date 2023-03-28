def wrap_in_p(func):
    def wrapper(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}</p>'

    return wrapper


@wrap_in_p
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'


username = render_input('username')
print(username)
