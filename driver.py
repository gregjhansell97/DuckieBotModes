#external modules
from collections import namedtuple
from duckie_bot import Mode

class Driver(Mode):
    '''
    base driver for the other driver modes in this package

    Attributes:
        speed_forces(namedtuple): forces affecting speed
        speed(int): speed of the driver
        omega_forces(namedtuple): forces affecting rotational velocity
        omega(int): rotational velocity
    '''
    def __init__(self):
        #forces applied to speeds
        Forces = namedtuple("Forces", ["applied", "drag"])
        self.speed_forces = Forces(applied=0.7, drag=0.5)
        self.omega_forces = Forces(applied=1, drag=0.8)

        #speeds themselves
        self.speed = 0
        self.omega = 0

    def drag(self, speed, drag):
        '''
        given drag and current speed what is the next speed

        Args:
            speed(int): current speed
            drag(fload): drag that will change the speed
        '''
        if speed < -drag:
            speed += drag
        elif speed < 0:
            speed = 0
        if speed > drag:
            speed -= drag
        elif speed > 0:
            speed = 0
        #puts a cap limit on max speed
        if abs(speed - 0) < 0.0001:
            speed = 0
        if speed < 0:
            return max(speed, -1)
        else:
            return min(speed, 1)

    def tick(self):
        '''
        implementation of abstract method in parent
        '''
        start_speed = self.speed
        start_omega = self.omega

        if "W" in self.keys_pressed:#up
            self.speed += self.speed_forces.applied
        if "S" in self.keys_pressed:#down
            self.speed -= self.speed_forces.applied
        if "A" in self.keys_pressed:#left
            self.omega += self.omega_forces.applied
        if "D" in self.keys_pressed:#right
            self.omega -= self.omega_forces.applied
        self.speed = self.drag(self.speed, self.speed_forces.drag)
        self.omega = self.drag(self.omega, self.omega_forces.drag)
        #deaccelerates items

        #reflect changes in car
        if start_speed != self.speed:
            self.car.set_speed(self.speed)
        if start_omega != self.omega:
            self.car.set_omega(self.omega)

    def frame(self, frame):
        '''
        implementation of abstract method in parent
        '''
        return frame
