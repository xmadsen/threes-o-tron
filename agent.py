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
        self.board.board_init()
        self.memory = Memory()
        self.qlearn = QLearningTable(actions=ACTION_SPACE)
        self.previous_action = None
        self.previous_state = None
        self.previous_score = 0
        self.states_seen = 0
        self.game_count = 0
        self.max_points = 0

    def step(self):
        obs = self.board.read_board()

        # flatten our state into one list
        state = [item for sublist in obs["tiles"] for item in sublist]
        score = obs["points"]
        # Give reward based on increased score for that single step
        # I wonder if lower reward values (closer to ~1 range) are better?
        score_difference = score - self.previous_score

        # last step of game
        if obs["last"]:

            final_point_total = obs["points"]

            # print("Game", self.game_count,
            #      "ended with a score of", final_point_total)
            if final_point_total > self.max_points:
                print("New high score! Previous max was", self.max_points)
                self.max_points = final_point_total

            # loop through all saved states one by one and train on them
            # memory entries are of form [state, action, reward]
            current_memory = self.memory.pop()
            next_memory = self.memory.pop()
            while next_memory is not None:
                self.qlearn.learn(str(current_memory[0]), current_memory[1],
                                  final_point_total + current_memory[2], str(next_memory[0]))
                current_memory = next_memory
                # print(str(final_point_total + current_memory[2]))
                next_memory = self.memory.pop()
            # last memory gets a terminal code
            self.qlearn.learn(str(current_memory[0]), current_memory[1],
                              final_point_total + current_memory[2], 'terminal')
            # print(str(self.qlearn.q_table))

            # reset board
            self.board.board_init()
            self.memory.reset()
            self.previous_state = None
            self.previous_action = None
            self.previous_score = 0
            self.states_seen = len(self.qlearn.q_table.index)
            # take no action
            return final_point_total

        if obs["first"]:
            self.game_count += 1
            # return self.previous_score

        else:
            self.memory.push(self.previous_state,
                             self.previous_action, score_difference)
            # self.qlearn.learn(str(self.previous_state), self.previous_action,
            #                   score_difference, str(state))

        action = self.qlearn.choose_action(str(state))

        # take action
        valid_move = self.board.swipe(action)
        # if not valid_move:
        #     print("invalid move", action)
        # print(self.board)
        # print(score, 'points')
        # print(' ')

        # prepare for next step
        self.previous_state = state
        self.previous_action = action
        self.previous_score = score


class Memory:
    def __init__(self, max_size=300000):
        self.max_size = max_size
        self.reset()

    def reset(self):
        self.buffer = deque(maxlen=self.max_size)

    def push(self, state, action, reward):
        self.buffer.append((str(state), action, reward))

    def pop(self):
        if self.buffer:
            return self.buffer.pop()


# agent = BasicAgent()

# while True:
#    agent.step()
