from circleshape import *

class Asteroid(CircleShape):

    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    