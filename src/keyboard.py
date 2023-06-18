class Mixin:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'
        return self


class Keyboard(Mixin):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        self._language = language

    def __str__(self):
        return self.name

    @property
    def language(self):
        return self._language


