# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import unittest

# import paddle
# import torchvision

# from padiff import autodiff


# class TestCaseName(unittest.TestCase):
#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

#     def test_success(self):
#         layer = paddle.vision.resnet50()
#         module = torchvision.models.resnet50()
#         inp = paddle.rand((10, 3, 224, 224)).numpy().astype("float32")
#         assert (
#             autodiff(layer, module, inp, auto_weights=True, options={"atol": 5e-2}) is True
#         ), "Failed. expected success."


# if __name__ == "__main__":
#     unittest.main()
