class IObserver:
    def update(self):
        raise NotImplementedError


class ISubject:
    def __init__(self):
        self.observers: list = []

    def attach(self, observer: IObserver):
        self.observers.append(observer)

    def detach(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()
