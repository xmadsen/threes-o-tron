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
        self.qlearn = QLearningTable(actions=ACTION_SPACE)
        self.previous_action = None
        self.previous_state = None
        self.previous_score = 0
        self.game_count = 0
        self.max_points = 0
        
    def step(self):
        obs = self.board.read_board()

        state = obs["tiles"]
        score = obs["points"]
        # Give reward based on increased score for that single step
        # I wonder if lower reward values (closer to ~1 range) are better?
        score_difference = score - self.previous_score

        # last step of game
        if obs["last"]:

            print("Game", self.game_count, "ended with a score of", obs["points"])
            print("High score is", self.max_points)
            if obs["points"] > self.max_points:
                self.max_points = obs["points"]
                print("New high score!")

            # Give final reward
            self.qlearn.learn(
                str(self.previous_state), state, score_difference, 'terminal')
            # print(str(self.qlearn.q_table))

            # take no action
            return

        # if first step of game
        if obs["first"]:
            self.previous_state = None
            self.previous_action = None
            self.previous_score = 0
            self.game_count += 1

        if self.previous_state:
            self.qlearn.learn(
                str(self.previous_state), state, score_difference, str(state))

        action = self.qlearn.choose_action(str(state))

        # for now it just picks a random action 0-3
        print(action)
        # take action and loop step

        self.previous_state = state
        self.previous_action = action
        self.previous_score = score

agent = BasicAgent()
agent.step()
agent.step()
agent.step()
agent.step()
print(str(agent.qlearn.q_table))
