from tfx.components.example_gen.csv_example_gen.component import CsvExampleGen
from tfx.utils.dsl_utils import csv_input
from tfx.components import StatisticsGen
from tfx.components import SchemaGen
from tfx.components import ExampleValidator


class devc:
    def __init__(self, base_dir, csvname):
        self.base_dir = base_dir
        self.csvname = csvname
        self.components = []
        examples = csv_input(os.path.join(self.base_dir, self.csvname))
        self.example_gen = tfx.components.example_gen.csv_example_gen.component.CsvExampleGen(input=examples)
        self.statistics_gen = StatisticsGen(self.example_gen.outputs['examples'],instance_name=self.csvname + "_statistics_gen")
        self.scheme_gen = SchemaGen(
            statistics=self.statistics_gen.outputs['statistics']
        )
        self.valid_stats = ExampleValidator(
            statistics=self.statistics_gen.outputs["statistics"], schema=self.scheme_gen.outputs["schema"]
        )

    @classmethod
    def re_pipe(self, csvname):
        self.csvname = csvname
        examples = csv_inputs(
            os.path.join(self.base_dir, self.csvname))
        self.example_gen = tfx.components.example_gen.csv_example_gen.component.CsvExampleGen(
            input=examples)
        self.statistics_gen = StatisticsGen(
            self.example_gen.outputs['examples'],
            instance_name=self.csvname + "_statistics_gen"
        )
        self.scheme_gen = SchemaGen(
            statistics=self.statistics_gen.outputs['statistics']
        )
        self.valid_stats = ExampleValidator(
            statistics=self.statistics_gen.outputs["statistics"], schema=self.scheme_gen.outputs["schema"]
        )
        return "done"

    @classmethod
    def gen_examples(self, csvname):
        self.csvname = csvname
        examples = csv_inputs(
            os.path.join(self.base_dir, self.csvname))
        self.example_gen = tfx.components.example_gen.csv_example.component.CsvExampleGen(
            input=examples)
        return self.examples_gen
    @classmethod
    def appendAll(self):
        self.components.append(self.examples_gen)
        self.components.append(self.statistics_gen)
        self.components.append(self.schema_gen)
        self.components.append(self.valid_stats)
    @classmethod
    def stats_gen(self):
        return self.statistics_gen

    @classmethod
    def scheme_gen(self):
        return self.statistics_gen
