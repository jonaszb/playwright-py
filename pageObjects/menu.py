from pageObjects.base import Base


class Menu(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
