def get_initials(name):
    if " " not in name:
        return name[0] + "."
    else:
        chars = list(name)
        uppers = [c for c in chars if c.isupper()]
        return '.'.join(uppers) + '.'
