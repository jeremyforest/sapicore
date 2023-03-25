import pytest
import os

from sapicore.data.external.drift import DriftDataset
from sapicore.tests import ROOT

TEST_ROOT = os.path.join(ROOT, "tests", "data", "test_data")  # test root directory.


class TestDrift:
    @pytest.mark.unit
    def test_drift_processing(self):
        # calling a dataset invokes its load() method and returns a self reference.
        DriftDataset(identifier="drift", root=os.path.join(TEST_ROOT, "drift"))()


if __name__ == "__main__":
    pytest.main(args=["-s", "-v"])
