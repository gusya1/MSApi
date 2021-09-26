
class Search:

    def __init__(self, *args):
        self.search_list = []
        for arg in args:
            self.search_list.append(str(arg))

    def __str__(self):
        return f"search={' '.join(self.search_list)}"
