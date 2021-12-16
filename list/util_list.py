class UtilsList(list):

    def foreach(self, function):
        for i in self:
            function(i)

    def map(self, function):
        return [function(i) for i in self]

