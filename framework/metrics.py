from deepeval.metrics import GEval
from framework.metric_config import METRIC_CONFIG
from framework.config import THRESHOLDS

# Create a generic Metric Builder

def get_metric(metric_name):

    config = METRIC_CONFIG[metric_name]

    return GEval(

        name = metric_name,
        criteria = config["criteria"],
        evaluation_params = config["evaluation_params"],
        evaluation_steps = config["evaluation_steps"],
        threshold = THRESHOLDS.get(metric_name, 0.8)  # Default threshold is 0.8 if not specified
    ) 