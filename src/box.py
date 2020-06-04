class Box:

    def __init__(self, top_left, bottom_left, top_right, bottom_right):
        self.top_left = top_left
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.ship = False
        self.hit_status = False

    def get_ship(self):
        return self.ship

    def get_hit_status(self):
        return self.hit_status