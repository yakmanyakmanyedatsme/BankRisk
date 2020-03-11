import tfx
import Devc


class TTE:

    def __init__(self, Devc, preprocess, trainer_fn):
        self.Transform = tfx.components.Transform(
            examples=Devc.example_gen.outputs["training_examples"],
            schema=Devc.schema_gen.outputs["schema"],
            preprocessing_fn=preprocess,
            name='transform training'

        self.trainer=tfx.components.Trainer(
            module_file=module_file,
            transformed_examples=transform.outputs['transformed_examples'],
            schema=Devc.schema_gen.outputs['schema'],
            base_models=latest_model_resolver.outputs['latest_model'],
            transform_graph=transform.outputs['transform_graph'],
            train_args=trainer_pb2.TrainArgs(num_steps=10000),
            eval_args=trainer_pb2.EvalArgs(num_steps=5000))
    # transorm
    # Trainer
    # Evaluator
