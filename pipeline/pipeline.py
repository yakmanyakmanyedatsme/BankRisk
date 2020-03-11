from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import Optional, Text, List, Dict, Any

from ml_metadata.proto import metadata_store_pb2from tfx.components.base import executor_spec
from tfx.extensions.google_cloud_ai_platform.pusher import executor as ai_platform_pusher_executor
from tfx.extensions.google_cloud_ai_platform.trainer import executor as ai_platform_trainer_executor
from tfx.orchestration import pipeline
from tfx.proto import evaluator_pb2
from tfx.proto import pusher_pb2
from tfx.proto import trainer_pb2
from tfx.utils.dsl_utils import external_input
import TFXhelper.Devc as Devc

def create_pipeline(
    pipeline_name: Text,
    pipeline_root: Text,
    bucket: Text,
    csv_file: Text,
    preprocessing_fn: Text,
    trainer_fn: Text,
    train_args: trainer_pb2.TrainArgs,
    eval_args: trainer_pb2.EvalArgs,
    serving_model_dir: Text,
    metadata_connection_config: Optional[
    metadata_store_pb2.ConnectionConfig]=None,
    beam_pipeline_args: Optional[List[Text]]=None,
    ai_platform_training_args: Optional[Dict[Text, Text]]=None,
    ai_platform_serving_args: Optional[Dict[Text, Any]]=None,
    ) -> pipeline.Pipeline:
        tfdv=Devc(bucket,csv_file)
        components=Devc.appendAll()
    return pipeline.Pipeline(
        pipeline_name=pipeline_name,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        meta_data_connection_config=

        )
