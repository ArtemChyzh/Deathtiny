class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if type(cls) not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]
