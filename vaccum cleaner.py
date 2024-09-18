class VacuumCleaner:
    def __init__(self):
        # Initial state: (current_room, room_a_status, room_b_status)
        self.state = ('A', 'D', 'D')  # Starting in Room A with both rooms dirty

    def clean(self):
        current_room = self.state[0]
        if current_room == 'A':
            self.state = (current_room, 'C', self.state[2])  # Clean Room A
            print("Cleaning Room A")
        else:
            self.state = (current_room, self.state[1], 'C')  # Clean Room B
            print("Cleaning Room B")

    def move(self):
        current_room = self.state[0]
        if current_room == 'A':
            self.state = ('B', self.state[1], self.state[2])  # Move to Room B
            print("Moving to Room B")
        else:
            self.state = ('A', self.state[1], self.state[2])  # Move to Room A
            print("Moving to Room A")

    def run(self):
        while True:
            # Check if both rooms are clean
            if self.state[1] == 'C' and self.state[2] == 'C':
                print("Both rooms are clean!")
                break
            
            # Clean the current room if it's dirty
            if self.state[1] == 'D' and self.state[0] == 'A':
                self.clean()
            elif self.state[2] == 'D' and self.state[0] == 'B':
                self.clean()
            else:
                # Move to the other room
                self.move()

# Example usage
vacuum = VacuumCleaner()
vacuum.run()