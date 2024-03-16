class Tortoise:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        moves = max(dx, dy)
        if self.s >= moves:
            return moves
        else:
            return moves - self.s + 1

# Example usage:
tortoise = Tortoise(0, 0, 1)
tortoise.go_up()
tortoise.go_right()
print(tortoise.count_moves(2, 3))  