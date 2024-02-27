class UUID(str):
    def __repr__(self):
        return f"UUID({super().__repr__()})"
