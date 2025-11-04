import torch
import numpy as np
from torch import optim, nn, tensor
import argparse
from global_funcs import Vector2

samples = 1000
parser = argparse.ArgumentParser()
parser.add_argument('--sample', type=int, help='The number of samples for the AI.')
args = parser.parse_args()
if args.sample:
  samples = args.sample
AI_POS = [0, 0]
TARGET_POS = [80, 66]
def create_data(num_samples=1000):
  # Input features: a tensor of 10 random numbers for each sample
  # The network will learn to ignore these and just predict the target
  X = torch.randn(num_samples, 2)
  # Target: The hidden number repeated for each sample
  targets = []
  for _ in range(num_samples):
    targets.append(TARGET_POS)
  y = tensor(targets, dtype=torch.float)
  print(y)
  return X, y
# Generate our training data
X_train, y_train = create_data(samples)
class NumberGuesser(nn.Module):
  def __init__(self):
    super(NumberGuesser, self).__init__()
    # 10 input features, a few hidden layers, and a single output neuron
    self.fc1 = nn.Linear(2, 32)
    self.fc2 = nn.Linear(32, 16)
    self.output_layer = nn.Linear(16, 2)
    
  def forward(self, x):
    x = torch.relu(self.fc1(x))
    x = torch.relu(self.fc2(x))
    x = self.output_layer(x)
    return x
# Instantiate the network, loss function, and optimizer
model = NumberGuesser().to('cuda')
loss_function = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
# Training loop
epochs = samples
for epoch in range(epochs):
  # Forward pass: get the model's guess
  y_pred = model(X_train)
  # Calculate the loss
  loss = loss_function(y_pred, y_train)
  # Backward pass and optimization
  optimizer.zero_grad() # Clear gradients
  loss.backward()      # Compute gradients
  optimizer.step()     # Update weights
  # Print loss every 5 epochs
  if (epoch+1) % 250 == 0:
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
print("Training finished!")
# Create new, random data for the model to guess on
X_test = 0
# Put the model in evaluation mode
model.eval() 
# Make the prediction
with torch.no_grad():
  guessed_pos = model(torch.randn(1, 2))
print(f"\nModel's guess: {guessed_pos[0][0]:.2f, guessed_pos[0][1]:.2f}")#.item():.2f}, {guessed_pos[1].item():.2f}")
print(f"Correct number: {TARGET_POS}")