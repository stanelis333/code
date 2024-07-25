import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle
from collections import deque
import random
import seaborn as sns

class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def add(self, experience):
        self.buffer.append(experience)

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)

class GridWorld:
    def __init__(self, size=10, start=(0, 0), goal=(9, 9)):
        self.size = size
        self.start = start
        self.goal = goal
        self.obstacles = self.generate_obstacles(15)  # Increased obstacles to 20
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

    def render(self, q_table=None, ax=None, trajectory=None, heatmap=None):
        grid = np.zeros((self.size, self.size))
        for obs in self.obstacles:
            grid[obs] = -1
        grid[self.start] = 0.5
        grid[self.goal] = 1
        grid[self.position] = 0.8

        if heatmap is not None:
            ax.clear()
            sns.heatmap(heatmap, cmap='YlGnBu', annot=False, cbar=True, ax=ax, square=True)
            return

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
        if trajectory is not None:
            for pos in trajectory:
                ax.plot(pos[1], pos[0], 'ro-')

def q_learning(env, q_table=None, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, epsilon_decay=0.99, visualize_every=10, buffer_size=1000, batch_size=32):
    q_table = np.zeros((env.size, env.size, 4)) if q_table is None else q_table
    replay_buffer = ReplayBuffer(buffer_size)
    reward_history = []
    step_history = []
    all_trajectories = []
    heatmap = np.zeros((env.size, env.size))

    for episode in range(episodes):
        state = env.reset()
        done = False
        trajectory = [state]

        while not done:
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(4)
            else:
                action = np.argmax(q_table[state[0], state[1]])

            next_state, reward, done = env.step(action)
            trajectory.append(next_state)
            replay_buffer.add((state, action, reward, next_state, done))

            # Update heatmap
            heatmap[state[0], state[1]] += 1

            # Sample from replay buffer
            if len(replay_buffer) >= batch_size:
                batch = replay_buffer.sample(batch_size)
                for state_b, action_b, reward_b, next_state_b, done_b in batch:
                    old_value = q_table[state_b[0], state_b[1], action_b]
                    next_max = np.max(q_table[next_state_b[0], next_state_b[1]])
                    q_table[state_b[0], state_b[1], action_b] = old_value + alpha * (reward_b + gamma * next_max * (1 - done_b) - old_value)

            state = next_state

        epsilon *= epsilon_decay
        reward_history.append(reward)
        step_history.append(len(trajectory))
        all_trajectories.append(trajectory)

        if episode % visualize_every == 0:
            print(f"Episode {episode}/{episodes}: Reward: {reward}, Steps: {len(trajectory)}")

    return q_table, reward_history, step_history, all_trajectories, heatmap

def double_q_learning(env, q_table1=None, q_table2=None, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, buffer_size = 1000, epsilon_decay=0.99, visualize_every=10):
    q_table1 = np.zeros((env.size, env.size, 4)) if q_table1 is None else q_table1
    q_table2 = np.zeros((env.size, env.size, 4)) if q_table2 is None else q_table2
    reward_history = []
    step_history = []
    all_trajectories = []
    replay_buffer = ReplayBuffer(buffer_size)
    heatmap = np.zeros((env.size, env.size))

    for episode in range(episodes):
        state = env.reset()
        done = False
        trajectory = [state]

        while not done:
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(4)
            else:
                action = np.argmax(q_table1[state[0], state[1]] + q_table2[state[0], state[1]])

            next_state, reward, done = env.step(action)
            trajectory.append(next_state)
            replay_buffer.add((state, action, reward, next_state, done))

            # Update heatmap
            heatmap[state[0], state[1]] += 1

            if np.random.uniform(0, 1) < 0.5:
                next_action = np.argmax(q_table1[next_state[0], next_state[1]])
                old_value = q_table1[state[0], state[1], action]
                next_max = q_table2[next_state[0], next_state[1], next_action]
                q_table1[state[0], state[1], action] = old_value + alpha * (reward + gamma * next_max - old_value)
            else:
                next_action = np.argmax(q_table2[next_state[0], next_state[1]])
                old_value = q_table2[state[0], state[1], action]
                next_max = q_table1[next_state[0], next_state[1], next_action]
                q_table2[state[0], state[1], action] = old_value + alpha * (reward + gamma * next_max - old_value)

            state = next_state

        epsilon *= epsilon_decay
        reward_history.append(reward)
        step_history.append(len(trajectory))
        all_trajectories.append(trajectory)

        if episode % visualize_every == 0:
            print(f"Episode {episode}/{episodes}: Reward: {reward}, Steps: {len(trajectory)}")

    return q_table1, q_table2, reward_history, step_history, all_trajectories, heatmap

def save_q_table(q_table, filename='q_table.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(q_table, f)

def load_q_table(filename='q_table.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def update(frame, env, ax, q_table=None, trajectory=None, heatmap=None):
    if heatmap is not None:
        env.render(heatmap=heatmap, ax=ax)
    else:
        if q_table is not None:
            env.render(q_table=q_table, ax=ax, trajectory=trajectory)

try:
    q_table = load_q_table()
    q_learning_mode = True
except FileNotFoundError:
    q_table = None
    q_table1 = None
    q_table2 = None
    q_learning_mode = True  # Set to False if you want to run Double Q-Learning

env = GridWorld()

if q_learning_mode:
    q_table, reward_history, step_history, trajectories, heatmap = q_learning(
        env, q_table=q_table, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, epsilon_decay=0.99, visualize_every=10, buffer_size=1000, batch_size=32
    )
    save_q_table(q_table)
else:
    q_table1, q_table2, reward_history, step_history, trajectories, heatmap = double_q_learning(
        env, q_table1=q_table1, q_table2=q_table2, episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1, epsilon_decay=0.99, visualize_every=10
    )
    save_q_table(q_table1, filename='q_table1.pkl')
    save_q_table(q_table2, filename='q_table2.pkl')

# Animation
fig, ax = plt.subplots()
num_frames = len(trajectories[0])  # Assuming all trajectories have the same length
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(env, ax, q_table, trajectories[0], None), interval=200)
plt.show()

# Plot heatmap
plt.figure()
sns.heatmap(heatmap, cmap='YlGnBu', annot=False, cbar=True)
plt.title('Heatmap of Agent\'s Time Spent')
plt.show()

plt.figure()
plt.plot(step_history)
plt.title('Steps per Episode')
plt.xlabel('Episode')
plt.ylabel('Steps')
plt.show()

# Plot trajectories
fig, ax = plt.subplots()
for trajectory in trajectories:
    traj_x, traj_y = zip(*trajectory)
    ax.plot(traj_y, traj_x, marker='o')
ax.set_title('Agent\'s Trajectories')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

# Plot learning curves
plt.figure()
plt.plot(reward_history)
plt.title('Reward per Episode')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.show()


