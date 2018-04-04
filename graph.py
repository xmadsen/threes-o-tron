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
        games_rate = []

        while True:
            score = agent.step()
            if type(score) == int:
                times.append(time() - start_time)
                highscores.append(agent.max_points)
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
        print(times)
        print(scores)
        plt.clf()
        plt.plot(times, scores, 'bo', label="score")
        plt.plot(times, highscores, 'r-',
                 alpha=0.5, label="high score")
        plt.legend(loc="upper left")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Game score")
        plt.show()


if __name__ == '__main__':
    run_agent(sampling_rate=1)
