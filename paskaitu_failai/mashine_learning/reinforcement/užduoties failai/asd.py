import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

class GridWorld:
    def __init__(self, size=10, start=(0, 0), goal=(9, 9)):
        self.size = size
        self.start = start
        self.goal = goal
        self.obstacles = self.generate_obstacles(15)
        self.reset()

    def generate_obstacles(self, num_obstacles):
        obstacles = set()
        while len(obstacles) < num_obstacles:
            obstacle = (np.random.randint(0, self.size), np.random.randint(0, self.size))
            if obstacle != self.start and obstacle != self.goal:
                obstacles.add(obstacle)
        return list(obstacles)

    def reset(self):
        self.position = self.start
        return self.position

    def step(self, action):
        if action == 0:  # Up
            next_position = (self.position[0] - 1, self.position[1])
        elif action == 1:  # Right
            next_position = (self.position[0], self.position[1] + 1)
        elif action == 2:  # Down
            next_position = (self.position[0] + 1, self.position[1])
        elif action == 3:  # Left
            next_position = (self.position[0], self.position[1] - 1)

        reward = -1  # Standard reward for a step

        if (0 <= next_position[0] < self.size and
                0 <= next_position[1] < self.size):
            if next_position not in self.obstacles:
                self.position = next_position
            else:
                reward = -15  # Penalty for hitting an obstacle
        else:
            reward = -5  # Penalty for hitting a wall

        if self.position == self.goal:
            reward = 20  # Reward for reaching the goal

        return self.position, reward, self.position == self.goal

    def render(self, q_table=None, ax=None):
        grid = np.zeros((self.size, self.size))
        for obs in self.obstacles:
            grid[obs] = -1
        grid[self.start] = 0.5
        grid[self.goal] = 1
        grid[self.position] = 0.8

        ax.clear()
        ax.imshow(grid, cmap='cool')
        if q_table is not None:
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) not in self.obstacles and (i, j) != self.goal:
                        action = np.argmax(q_table[i, j])
                        if action == 0:
                            ax.arrow(j, i, 0, -0.3, head_width=0.2, head_length=0.2)
                        elif action == 1:
                            ax.arrow(j, i, 0.3, 0, head_width=0.2, head_length=0.2)
                        elif action == 2:
                            ax.arrow(j, i, 0, 0.3, head_width=0.2, head_length=0.2)
                        elif action == 3:
                            ax.arrow(j, i, -0.3, 0, head_width=0.2, head_length=0.2)

def q_learning(env, q_table=None, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, epsilon_decay=0.99, visualize_every=10):
    q_table = np.zeros((env.size, env.size, 4)) if q_table is None else q_table
    steps = []
    episode_rewards = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0

        while not done:
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(4)
            else:
                action = np.argmax(q_table[state[0], state[1]])

            next_state, reward, done = env.step(action)
            old_value = q_table[state[0], state[1], action]
            next_max = np.max(q_table[next_state[0], next_state[1]])

            q_table[state[0], state[1], action] = old_value + alpha * (reward + gamma * next_max - old_value)

            state = next_state
            episode_reward += reward

            if episode % visualize_every == 0:
                steps.append((q_table.copy(), env.position))

        episode_rewards.append(episode_reward)
        epsilon *= epsilon_decay

    return q_table, steps, episode_rewards

def save_q_table(q_table, filename='asd.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(q_table, f)

def load_q_table(filename='asd.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def update(frame, env, ax):
    q_table, position = frame
    env.position = position
    env.render(q_table, ax)

try:
    q_table = load_q_table()
except FileNotFoundError:
    q_table = None

env = GridWorld()
q_table, steps, episode_rewards = q_learning(env, q_table=q_table, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, epsilon_decay=0.99, visualize_every=10)

save_q_table(q_table)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=steps, fargs=(env, ax), interval=10)
plt.show()
