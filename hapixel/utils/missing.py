__all__ = (
    'MISSING',
    'Missing'
)


class Missing:
    def __init__(self):
        pass

    def __repr__(self):
        return "<MISSING>"

    def __str__(self):
        return "MISSING"

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, Missing)

    def __ne__(self, other):
        return not isinstance(other, Missing)

    def __call__(self, *args, **kwargs):
        return self


MISSING = Missing()
