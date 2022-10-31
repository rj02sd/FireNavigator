import pandas as pd
import datetime

from AgentOne import AgentOne
from Maze import Maze
from time import time
from AgentThree import AgentThree
from AgentTwo import AgentTwo
from AgentFour import AgentFour

"""
All code designed and written by
Troy Chibbaro – tbc41
Rishi Jammalamadaka - rj433

Each of us contributed an equal amount work via virtual collaboration.
Main was used strictly for testing our agents over extended periods of time
"""


def test(m, s, a, runs=100):
    """
    Runs tests with given parameters
    :param m: fire modifier
    :param s: size of maze
    :param a: agent number
    :param runs: number of runs to make
    :return: None
    """
    if a == 1:
        df = pd.read_csv("results/agent_one.csv", index_col=False)
    if a == 2:
        df = pd.read_csv("results/agent_two.csv", index_col=False)
    if a == 3:
        df = pd.read_csv("results/agent_three.csv", index_col=False)
    if a == 4:
        df = pd.read_csv("../backup/ProjectOne/results/agent_four_sim5.csv", index_col=False)
    for _ in range(runs):
        maze = Maze(fire_modifier=m, mazeSize=s)
        agent = None
        if a == 1:
            agent = AgentOne(maze)
        elif a == 2:
            agent = AgentTwo(maze)
        elif a == 3:
            agent = AgentThree(maze)
        elif a == 4:
            agent = AgentFour(maze)
        start = time()
        if agent.move():
            end = time()
            df.loc[len(df.index)] = [m, True, s, "{:3.5f}".format(end - start)]
        else:
            end = time()
            df.loc[len(df.index)] = [m, False, s, "{:3.5f}".format(end - start)]

    if a == 1:
        df.to_csv("results/agent_one.csv", index=False)
    if a == 2:
        df.to_csv("results/agent_two.csv", index=False)
    if a == 3:
        df.to_csv("results/agent_three.csv", index=False)
    if a == 4:
        df.to_csv("results/agent_four_sim5.csv", index=False)


def run_a_one():
    start = time()
    test(0.025, 51, 1, 1000)
    test(0.025, 75, 1, 1000)
    test(0.05, 51, 1, 1000)
    test(0.05, 75, 1, 1000)
    test(0.075, 51, 1, 1000)
    test(0.075, 75, 1, 1000)
    end = time()
    delta = str(datetime.timedelta(seconds=end - start))
    print(f"Agent one finished with runtime: {delta}")


def run_a_two():
    start = time()
    test(0.025, 51, 2, 1000)
    test(0.025, 75, 2, 1000)
    test(0.05, 51, 2, 1000)
    test(0.05, 75, 2, 1000)
    test(0.075, 51, 2, 1000)
    test(0.075, 75, 2, 1000)
    end = time()
    delta = str(datetime.timedelta(seconds=end - start))
    print(f"Agent two finished with runtime: {delta}")


def run_a_three():
    start = time()
    test(0.025, 51, 3, 250)
    test(0.025, 75, 3, 250)
    test(0.05, 51, 3, 250)
    test(0.05, 75, 3, 250)
    test(0.075, 51, 3, 250)
    test(0.075, 75, 3, 250)
    end = time()
    delta = str(datetime.timedelta(seconds=end - start))
    print(f"Agent three finished with runtime: {delta}")


def run_a_four():
    start = time()
    test(0.025, 51, 4, 250)
    test(0.025, 75, 4, 250)
    test(0.05, 51, 4, 250)
    test(0.05, 75, 4, 250)
    test(0.075, 51, 4, 250)
    test(0.075, 75, 4, 250)
    end = time()
    delta = str(datetime.timedelta(seconds=end - start))
    print(f"Agent three finished with runtime: {delta}")


def main():
    """start = time()
    t1 = threading.Thread(target=run_a_three())
    t2 = threading.Thread(target=run_a_four())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()
    delta = str(datetime.timedelta(seconds=end - start))
    print(f"Testing complete. Full runtime: {delta}. Beginning analysis")"""




    """start = time()
    t1 = threading.Thread(target=run_a_one())
    t2 = threading.Thread(target=run_a_two())
    t3 = threading.Thread(target=run_a_three())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time()
    delta = str(datetime.timedelta(seconds=end-start))
    """
    df_agent_one = pd.read_csv("new_results/agent_one.csv")
    df_agent_two = pd.read_csv("new_results/agent_two.csv")
    df_agent_three = pd.read_csv("new_results/agent_three.csv")
    df_agent_four = pd.read_csv("new_results/agent_four.csv")

    #Agent one
    small = df_agent_one[df_agent_one['maze_size'] == 51]
    group = small.groupby('q')
    print("Agent 1 results at maze size 51x51")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    #size 75
    medium = df_agent_one[df_agent_one['maze_size'] == 63]
    group = medium.groupby('q')
    print("Agent 1 results at maze size 75x75")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    #Agent two results
    small = df_agent_two[df_agent_two['maze_size'] == 51]
    group = small.groupby('q')
    print("Agent 2 results at maze size 51x51")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    # size 75
    medium = df_agent_two[df_agent_two['maze_size'] == 63]
    group = medium.groupby('q')
    print("Agent 2 results at maze size 75x75")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    # Agent three results
    small = df_agent_three[df_agent_three['maze_size'] == 51]
    group = small.groupby('q')
    print("Agent 3 results at maze size 51x51")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    # size 75
    medium = df_agent_three[df_agent_three['maze_size'] == 63]
    group = medium.groupby('q')
    print("Agent 3 results at maze size 75x75")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    # Agent four results
    small = df_agent_four[df_agent_four['maze_size'] == 51]
    group = small.groupby('q')
    print("Agent 4 results at maze size 51x51")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")

    # size 75
    medium = df_agent_four[df_agent_four['maze_size'] == 63]
    group = medium.groupby('q')
    print("Agent 4 results at maze size 75x75")
    print(f"Success rates\n{group['successful'].mean().to_string()}")
    print(f"Average runtime\n{group['runtime'].mean().to_string()}")


main()
