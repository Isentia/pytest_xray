import logging
import unittest
from random import randint

import pytest

logging.basicConfig(level=logging.INFO)


class PluginTests(unittest.TestCase):
    @pytest.mark.xray(test_key="PRDS-12277", test_exec_key="PRDS-12276")
    def test_pass_1(self):
        pass

    def test_pass_2(self):
        pass

    @pytest.mark.xray(test_key="PRDS-12279", test_exec_key="PRDS-12276")
    def test_fail(self):
        self.fail("Forced failure 1")

    def test_fail_2(self):
        self.fail("Forced failure 2")

    @pytest.mark.xray(test_key="PRDS-12280", test_exec_key="PRDS-12276")
    def test_intermittent_failure_1(self):
        if randint(0, 100) < 20:
            raise Exception("Something went wrong")

    def test_intermittent_failure_2(self):
        if randint(0, 100) < 20:
            raise Exception("Something went wrong")
