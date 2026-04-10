#La pelota que rebota.
class BouncingBall:
    def __init__(self, initial_height, bounces):
        self.height = initial_height
        self.bounces = bounces
        self.current_bounce = 0

    def simulate_bounces(self):
        while self.current_bounce < self.bounces:
            self.current_bounce += 1
            self.height *= (3/5)
            print(f"Bounce {self.current_bounce}: Height {round(self.height, 2)}")

# Example of using the BouncingBall class
initial_height = 100
bounces = 12

bouncing_ball = BouncingBall(initial_height, bounces)
bouncing_ball.simulate_bounces()


