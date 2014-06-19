#!/usr/bin/env python

#    Copyright 2014 Rustici Software
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Discovers and runs all tests in the test module.

All tests must end in '_test.py' to be included in the test. It is
highly recommended that tests be named in the format
'<module_name>_test.py'.
"""
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('test', pattern='*_test.py')
    unittest.TextTestRunner(verbosity=2).run(suite)

