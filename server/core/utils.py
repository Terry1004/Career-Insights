def non_empty_items(l):
    return [item.strip() for item in l if item]


def to_like_string(s):
    s = s.strip().lower().replace('_', r'\_').replace('%', r'\%')
    return '%{}%'.format(s)