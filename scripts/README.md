# Experiment launchers

These shell scripts are retained from the original research workflow. Many assume a specific cluster layout under `/mnt/ssd`, hard-code GPU IDs, or refer to historical staging folders. They are useful as records of the run recipes, but require local review before execution elsewhere.

For a new installation, use the direct commands in the [root README](../README.md) and the root `main_*.py` entry points. The maintained rotation evaluator is `main_eval_rotation.py`; its historical name still accepts the paper's `--max_angle 90` setting.

Do not assume `configs/pretrain.yaml` matches a checkpoint trained with `configs/pretrain_v9_repaired.yaml`; select the corresponding model config explicitly.
