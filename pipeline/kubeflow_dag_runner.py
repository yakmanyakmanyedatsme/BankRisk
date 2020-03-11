from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import absl
import configs
import pipeline
from tfx.orchestration.kubeflow import kubeflow_dag_runner

# TFX pipeline produces many output files and metadata. All output data will be
# stored under this OUTPUT_DIR.
OUTPUT_DIR = os.path.join('gs://', configs.GCS_BUCKET_NAME)
PIPELINE_ROOT = os.path.join(OUTPUT_DIR, 'tfx_pipeline_output',
                             configs.PIPELINE_NAME)
# The last component of the pipeline, "Pusher" will produce serving model under
# SERVING_MODEL_DIR.
SERVING_MODEL_DIR = os.path.join(PIPELINE_ROOT, 'serving_model')
# Specifies data file directory. DATA_PATH should be a directory containing CSV
BUCKET=config.GCS_BUCKET_NAME
CSV_FILE='Global_banks_ready.csv'
def run():
  tfx_image = os.environ.get('KUBEFLOW_TFX_IMAGE', None)

  runner_config = kubeflow_dag_runner.KubeflowDagRunnerConfig(
      kubeflow_metadata_config=metadata_config,
      tfx_image=tfx_image
  )
  kubeflow_dag_runner.KubeflowDagRunner(config=runner_config).run(
      pipeline.create_pipeline(
          pipeline_name=configs.PIPELINE_NAME,
          pipeline_root=PIPELINE_ROOT,
          bucket=BUCKET,
          csv_file=CSV_FILE,
          preprocessing_fn=configs.PREPROCESSING_FN,
          trainer_fn=configs.TRAINER_FN,
          train_args=configs.TRAIN_ARGS,
          eval_args=configs.EVAL_ARGS,
          serving_model_dir=SERVING_MODEL_DIR,
      ))
