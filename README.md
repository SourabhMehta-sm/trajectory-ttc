# Installation 

### Environment
* **Tested OS:** MacOS, Linux
* Python >= 3.7
* PyTorch == 1.8.0
### Dependencies:
1. Install [PyTorch 1.8.0](https://pytorch.org/get-started/previous-versions/) with the correct CUDA version.
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
### Datasets 

To pre-process the data use the code.

```
python data/process_nuscenes.py --data_root <PATH_TO_NUSCENES>
```

### Result
Run the following command to test pretrained models for the nuScenes dataset:

```
python test.py --cfg nuscenes_5sample_agentformer --gpu 0
```
|       | ADE_5 | FDE_5 | 
|-------|-------|-------|
| model | 1.856 | 3.889 | 

### Model Architecture

- **Input Representation**: The model first encodes the input trajectories of all agents in the scene using embeddings. These embeddings capture the temporal aspect of each agent's past trajectory.
- **Agent-Aware Self-Attention Mechanism**: At the core of the architecture is an agent-aware self-attention mechanism. This allows the model to differentiate between the same agent at different times and different agents at the same time. It enables the model to capture both temporal dynamics of individual agents and the spatial interactions among multiple agents effectively.
- **Encoder-Decoder Structure**: The architecture follows the Transformer's encoder-decoder structure. The encoder processes the input trajectories, while the decoder generates future trajectories. Both the encoder and decoder utilize the agent-aware self-attention mechanism to model the complex dependencies in the data.
- **Output Trajectory Prediction**: The decoder outputs predicted future trajectories based on the learned representations of past trajectories and inter-agent relations. The model can generate multiple plausible future trajectories for each agent, considering the inherent uncertainty in their movements.
- **Conditional Variational Autoencoder (CVAE)**: To handle the multimodal nature of future trajectories (i.e., there can be multiple plausible futures), the arhitecture incorporates a CVAE. This allows the model to sample different possible future states, providing a distribution of future trajectories rather than a single deterministic output.


# Citation
> Ye Yuan, 2021, "AgentFormer: Agent-Aware Transformers for
Socio-Temporal Multi-Agent Forecasting" [AgentFormer](https://www.ye-yuan.com/agentformer/):
```bibtex
@inproceedings{yuan2021agent,
    title={AgentFormer: Agent-Aware Transformers for Socio-Temporal Multi-Agent Forecasting},
    author={Yuan, Ye and Weng, Xinshuo and Ou, Yanglan and Kitani, Kris},
    booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    year={2021}
}
```

# License
Please see the [license](LICENSE) for further details.
