class ExpenseMetadata(object):
    def __init__(self, name=None, notes=None, imgurl=None):
        self.name = name
        self.notes = notes
        self.imgurl = imgurl

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_notes(self, name):
        self.notes = notes

    def get_notes(self):
        return self.notes

    def set_img_url(self, imgurl):
        self.name = name

    def get_img_url(self):
        return self.imgurl