from time import time


class User():

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if rank < -8 or rank == 0 or rank > 8 or not isinstance(rank, int):
            raise ValueError

        d = rank - self.rank
        if rank > 0 and self.rank < 0:
            d -= 1
        elif rank < 0 and self.rank > 0:
            d += 1
        if self.rank == 8:
            return 0
        if d == 0:
            self.progress += 3
        elif d == -1:
            self.progress += 1
        elif d > 0:
            self.progress += 10 * d * d
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
            if self.rank == 8:
                self.progress = 0
                return 0
        return 0


t1 = time()
user = User()
user.inc_progress(-1)
user.inc_progress(-7)
user.inc_progress(1)
t2 = time()
