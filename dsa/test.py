class Cookie:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print("The color is", self.color)

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
cookie_one = Cookie("White")
cookie_one.print_color()

cookie_one.set_color("Yellow")
print("The cookie color is", cookie_one.get_color())