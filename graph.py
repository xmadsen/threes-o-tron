import matplotlib.pyplot as plt
from time import sleep, time
from agent import BasicAgent


def run_agent(sampling_rate=5):
    try:
        agent = BasicAgent()
        game_count = 0
        start_time, last_time = time(), time()
        times = []
        highscores = []
        scores = []
        state_count = []
        games_rate = []

        while True:
            score = agent.step()
            if type(score) == int:
                times.append(time() - start_time)
                highscores.append(agent.max_points)
                state_count.append(agent.states_seen)
                scores.append(score)

            game_count = agent.game_count

            if time() - last_time > sampling_rate:

                # Update games_per_second rate and print high score
                games_per_second = game_count / (time() - start_time)
                print("------------------------------------")
                print(f"Overall rate: {games_per_second:.2f} games / second")
                print(f"High score: {agent.max_points}")
                print(f"Total game count: {game_count}")
                print("------------------------------------")
                last_time = time()

    except KeyboardInterrupt:
        # Graph the high scores and individual game scores over time
        plt.clf()
        plt.subplot(211)
        plt.legend(loc="upper left")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Game score")
        plt.plot(times, scores, 'bo', label="score")
        plt.plot(times, highscores, 'r-',
                 alpha=0.75, label="high score")
        plt.subplot(212)
        plt.plot(times, state_count, 'g-',
                 alpha=0.75, label="state count")
        plt.legend(loc="upper left")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Number of states")
        plt.show()


if __name__ == '__main__':
    run_agent(sampling_rate=1)
