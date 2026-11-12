"""Model training will be implemented after the dataset is inspected.

We must first identify:
- the validated HRQoL instrument and outcome column;
- whether the task is regression, classification, or another analysis;
- predictor availability, data leakage risks, and sample size;
- the study design and appropriate validation strategy.
"""

def training_readiness_check(target_column: str | None) -> str:
    if not target_column:
        return "Not ready: the target outcome has not been identified."
    return (
        f"Target candidate recorded: {target_column}. "
        "Confirm its meaning and measurement before training."
    )
