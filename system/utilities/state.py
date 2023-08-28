direction = 'up' or 'down' or 'left' or 'right'
action = 'stop' or 'walk'
class State():
    def __init__(self, dir:str = direction, act:str = action):
        self.direction:direction = dir
        self.action:action = act
    
    def __str__(self) -> str:
        return f"{self.direction}_{self.action}"