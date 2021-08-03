import pytest

from ml import predict

# def test_predict_3():
#     assert predict("sample-3.png") == 3


# def test_predict_7():
#     assert predict("sample-7.jpg") == 7

@pytest.mark.parametrize("image_path,expected_number", [
    ("sample-3.png", 3),
    ("sample-7.jpg", 7),
])
def test_predict(image_path, expected_number):
    assert predict(image_path) == expected_number
