from threesgame import Board
from qlearning import QLearningTable
from collections import deque

ACTION_SPACE = [
    'up',
    'down',
    'left',
    'right',
]

class BasicAgent():
    def __init__(self):
        self.board = Board()
        self.qlearn = QLearningTable(actions=list(range(len(ACTION_SPACE))))
        self.previous_action = None
        self.previous_state = None
        self.max_points = 0
        self.memory = Memory()
        
    def step(self):
        obs = self.board.read_board()

        if obs["first"]:
            # first step stuff
            self.previous_action = None

        if obs["last"]:
            reward = 0
            if obs["points"] > self.max_points:
                # add reward
                # ...
                # and then
                self.max_points = obs["points"]

            # q learning at the end of the game
            # reset game

        if self.previous_action is not None:
            self.memory.push(self.previous_state, self.previous_action)

        state = obs["tiles"]

        action = self.qlearn.choose_action(str(state))

        # for now it just picks a random action 0-3
        print(action)

        self.previous_state = state
        self.previous_action = action
            

class Memory:
    def __init__(self, max_size=300000):
        self.max_size = max_size
        self.reset()

    def reset(self):
        self.buffer = deque(maxlen=self.max_size)

    def push(self, state, action):
        self.buffer.append((str(state), action))

    def pop(self):
        if self.buffer:
            return self.buffer.pop()


agent = BasicAgent()
agent.step()
