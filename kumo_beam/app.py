from typing import Callable

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class Options(PipelineOptions):

  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_argument(
        "--input-text",
        default="Default input text",
        help="Input text to print.",
    )


def run(
    options: Options,
    test: Callable[[beam.PCollection], None] = lambda _: None,
) -> None:
    with beam.Pipeline(options=options) as pipeline:
        elements = (
            pipeline
            | "Create elements" >> beam.Create(["Hello", "World!", options.input_text])
            | "Print elements" >> beam.Map(print)
        )

        # Used for testing only.
        test(elements)
