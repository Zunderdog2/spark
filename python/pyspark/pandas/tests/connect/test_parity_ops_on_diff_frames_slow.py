#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from pyspark.pandas.tests.test_ops_on_diff_frames_slow import OpsOnDiffFramesEnabledSlowTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase
from pyspark.testing.pandasutils import PandasOnSparkTestUtils


class OpsOnDiffFramesEnabledSlowParityTests(
    OpsOnDiffFramesEnabledSlowTestsMixin, PandasOnSparkTestUtils, ReusedConnectTestCase
):
    @unittest.skip(
        "TODO(SPARK-43613): Enable pyspark.pandas.spark.functions.covar in Spark Connect."
    )
    def test_cov(self):
        super().test_cov()

    @unittest.skip(
        "TODO(SPARK-43611): Fix unexpected `AnalysisException` from Spark Connect client."
    )
    def test_diff(self):
        super().test_diff()

    @unittest.skip(
        "TODO(SPARK-43658): Fix unexpected `SparkConnectGrpcException` from Spark Connect client."
    )
    def test_frame_iloc_setitem(self):
        super().test_frame_iloc_setitem()

    @unittest.skip("TODO(SPARK-43652): Enable GroupBy.rank with Spark Connect.")
    def test_rank(self):
        super().test_rank()

    @unittest.skip(
        "TODO(SPARK-43659): Enable OpsOnDiffFramesEnabledSlowParityTests.test_series_eq."
    )
    def test_series_eq(self):
        super().test_series_eq()

    @unittest.skip(
        "TODO(SPARK-43658): Fix unexpected `SparkConnectGrpcException` from Spark Connect client."
    )
    def test_series_iloc_setitem(self):
        super().test_series_iloc_setitem()

    @unittest.skip(
        "TODO(SPARK-43611): Fix unexpected `AnalysisException` from Spark Connect client."
    )
    def test_shift(self):
        super().test_shift()


if __name__ == "__main__":
    from pyspark.pandas.tests.connect.test_parity_ops_on_diff_frames_slow import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
