# Collision Probability Calculation

This guide details the process for calculating the probability of collision between vehicles, taking into account both their spatial and temporal proximities. The method integrates the concept of Time to Collision (TTC) with the physical distance between vehicles to assess potential risks more comprehensively.

## Time to Collision (TTC)

TTC is a crucial metric in evaluating the risk of collision between two moving vehicles. It can be calculated using the formula:

TTC = D / V_rel


where:

- `TTC` is the Time to Collision.
- `D` represents the distance between the two vehicles.
- `V_rel` is the relative velocity between the vehicles, calculated as `V_lead - V_ego`. Here, `V_lead` is the velocity of the leading vehicle, and `V_ego` is the velocity of the trailing (or ego) vehicle.

## Collision Probability Calculation

To determine the collision probability for each pair of vehicles, we assess whether the TTC falls below a specific threshold, indicating a high risk of collision. The probability of collision across a scene or dataset is given by:

P_collision = C / T

where:

- `P_collision` is the probability of collision.
- `C` is the count of vehicle pairs with TTC below a certain threshold.
- `T` is the total number of unique vehicle pairs in the scene or dataset.

## Integrating Distance into the Probability

To incorporate spatial proximity into the collision risk assessment, the calculation can be adjusted to consider vehicle pairs that are both likely to collide based on TTC and are within a specified distance threshold:

C' = Count of pairs where TTC < TTC_threshold and D < D_threshold

The modified collision probability then becomes:

P_collision' = C' / T

This enhanced formula accounts for both temporal and spatial factors, offering a more comprehensive evaluation of collision risks.