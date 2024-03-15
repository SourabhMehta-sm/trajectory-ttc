import os
import numpy as np

def load_trajectory_data(base_folder_path):
    # Dictionary to hold trajectory data, keyed by scene and frame
    trajectory_data = {}

    # List all scene folders in the directory
    scene_folders = [f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))]
    
    for scene_folder in scene_folders:
        scene_path = os.path.join(base_folder_path, scene_folder)
        trajectory_data[scene_folder] = {}
        
        # List all frame files in the scene directory
        for file_name in os.listdir(scene_path):
            if file_name.startswith('frame_') and file_name.endswith('.txt'):
                # Extract the frame number from the file name
                frame_number = int(file_name.replace('frame_', '').replace('.txt', ''))
                
                # Read the file and parse the trajectory data
                file_path = os.path.join(scene_path, file_name)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    trajectories = []
                    for line in lines:
                        _, agent_id, x, y = line.split()
                        trajectories.append([int(float(agent_id)), float(x), float(y)])
                
                # Sort by agent_id and convert to numpy array
                trajectories.sort(key=lambda x: x[0])
                trajectory_data[scene_folder][frame_number] = np.array(trajectories)[:, 1:]

    return trajectory_data

def calculate_and_summarize_collisions(trajectory_data, max_x_distance=100, max_y_distance=4.0, vehicle_length=4.0, vehicle_width=1.8):
    collision_summaries = {}

    for scene, frames_data in trajectory_data.items():
        max_prob = 0
        summary = ""
        for frame, positions in frames_data.items():
            # Sort vehicles by x-coordinate to identify adjacent vehicles
            sorted_indices = np.argsort(positions[:, 0])
            sorted_positions = positions[sorted_indices]

            for i in range(len(sorted_positions) - 1):
                ego_id = sorted_indices[i]
                target_id = sorted_indices[i + 1]

                # Adjust distances by subtracting vehicle dimensions
                x_distance = sorted_positions[i + 1][0] - sorted_positions[i][0] - vehicle_length
                y_distance = abs(sorted_positions[i + 1][1] - sorted_positions[i][1]) - vehicle_width

                # Ensure distances do not go negative after adjustment
                x_distance = max(x_distance, 0)
                y_distance = max(y_distance, 0)

                # Calculate collision probabilities
                prob_x = max(0, 1 - x_distance / max_x_distance)
                prob_y = max(0, 1 - y_distance / (max_y_distance / 2))  # Adjust for left and right side
                combined_prob = prob_x * prob_y

                if combined_prob > max_prob:
                    max_prob = combined_prob
                    summary = f"vehicle {ego_id} has a {max_prob:.2f} probability of colliding with vehicle {target_id}"

        collision_summaries[scene] = summary
    
    return collision_summaries

def calculate_collision_probabilities_with_nonlinear(trajectory_data, vehicle_length=4.0, vehicle_width=1.8):
    collision_probabilities = {}

    # Define decay parameters for the exponential function
    lambda_x = 0.01  # Example value, adjust based on dataset
    lambda_y = 0.1  # Example value, adjust based on dataset

    for scene, frames_data in trajectory_data.items():
        max_prob = 0
        most_likely_collision_pair = ()
        for frame, positions in frames_data.items():
            sorted_indices = np.argsort(positions[:, 0])
            sorted_positions = positions[sorted_indices]

            for i in range(len(sorted_positions) - 1):
                ego_id = sorted_indices[i]
                target_id = sorted_indices[i + 1]

                # Adjust distances by subtracting vehicle dimensions and ensure non-negativity
                x_distance = max(sorted_positions[i + 1][0] - sorted_positions[i][0] - vehicle_length, 0)
                y_distance = max(abs(sorted_positions[i + 1][1] - sorted_positions[i][1]) - vehicle_width, 0)

                # Calculate probabilities using exponential decay
                prob_x = 1 - np.exp(-lambda_x * x_distance)
                prob_y = 1 - np.exp(-lambda_y * y_distance)
                combined_prob = prob_x * prob_y

                # Update max probability and most likely collision pair if needed
                if combined_prob > max_prob:
                    max_prob = combined_prob
                    most_likely_collision_pair = (ego_id, target_id)

        # Store the most likely collision pair and its probability for the current scene
        if most_likely_collision_pair:
            collision_probabilities[scene] = {
                "most_likely_collision_pair": most_likely_collision_pair,
                "probability": max_prob
            }

    return collision_probabilities

base_folder_path = '../results/nuscenes_5sample_agentformer/results/epoch_0035/test/recon'
trajectory_data = load_trajectory_data(base_folder_path)
collision_probabilities = calculate_collision_probabilities_with_nonlinear(trajectory_data)
print(collision_probabilities)
# collision_summaries = calculate_and_summarize_collisions(trajectory_data)
# for scene, summary in collision_summaries.items():
#     print(f"In {scene}, {summary}")