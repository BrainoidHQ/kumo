import unittest
from unittest.mock import patch

from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

import kumo_beam


@patch("apache_beam.Pipeline", TestPipeline)
@patch("builtins.print", lambda x: x)
class TestApp(unittest.TestCase):
    def test_run_direct_runner(self):
        expected = ["Test", "Hello", "World!"]
        kumo_beam.run(
            options=kumo_beam.Options(input_text="Test"),
            test=lambda elements: assert_that(elements, equal_to(expected)),
        )


if __name__ == "__main__":
    unittest.main()
