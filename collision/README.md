# Probability of Collision Calculation

## Overview

This document provides the formulas used for calculating the probability of a collision within a simulation. It covers calculations for a single frame as well as for an entire scene.

## Single Frame Collision Probability

The probability of a collision occurring in a single frame is calculated as follows:

- **Formula**: `P(collision) = C(n, 2)`
- **Where**:
  - `P(collision)` is the probability of a collision occurring in a frame.
  - `C` is the number of unique agent pairs where the distance between agents is less than the collision threshold.
  - `n` is the total number of agents in the frame.
  - `C(n, 2)` is the binomial coefficient, representing the total number of unique agent pairs possible in the frame. This is calculated as `n(n - 1) / 2`, which gives the total combinations of pairs.

## Scene Collision Probability

To calculate the probability of collision across an entire scene, we use the average probability across all frames:

- **Formula**: `P_scene(collision) = 1/T * Σ(from t=1 to T) P_t(collision)`
- **Where**:
  - `P_scene(collision)` is the average probability of a collision occurring in the entire scene.
  - `T` is the total number of frames in the scene.
  - `P_t(collision)` is the probability of a collision occurring in frame `t`.

This methodology allows for a comprehensive understanding of collision dynamics within the simulated environment, providing crucial insights for optimization and safety assessments.