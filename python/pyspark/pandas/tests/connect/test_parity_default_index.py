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

from pyspark.pandas.tests.test_default_index import DefaultIndexTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase
from pyspark.testing.pandasutils import PandasOnSparkTestUtils


class DefaultIndexParityTests(
    DefaultIndexTestsMixin, PandasOnSparkTestUtils, ReusedConnectTestCase
):
    @unittest.skip(
        "TODO(SPARK-43610): Enable `InternalFrame.attach_distributed_column` in Spark Connect."
    )
    def test_default_index_distributed(self):
        super().test_default_index_distributed()

    @unittest.skip(
        "TODO(SPARK-43611): Fix unexpected `AnalysisException` from Spark Connect client."
    )
    def test_default_index_sequence(self):
        super().test_default_index_sequence()

    @unittest.skip(
        "TODO(SPARK-43623): Enable DefaultIndexParityTests.test_index_distributed_sequence_cleanup."
    )
    def test_index_distributed_sequence_cleanup(self):
        super().test_index_distributed_sequence_cleanup()


if __name__ == "__main__":
    from pyspark.pandas.tests.connect.test_parity_default_index import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
