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



# Citation
If you find our work useful in your research, please cite our paper [AgentFormer](https://www.ye-yuan.com/agentformer/):
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
