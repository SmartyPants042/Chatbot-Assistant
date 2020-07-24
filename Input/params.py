class name():
    def __init__(self, called_by='name'):
        self.called_by = called_by
        self.value = None
        self.POS = 'NN'


class date_time():
    def __init__(self, called_by='date/time'):
        self.called_by = called_by
        self.value = None
        self.POS = 'NNP'

class number():
    def __init__(self, called_by='number'):
        self.called_by = called_by
        self.value = None
        self.POS = 'QC'