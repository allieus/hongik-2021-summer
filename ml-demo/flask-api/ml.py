import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("Predict_Model.h5")


def predict(image_path: str) -> int:
    """
    이미지 파일을 읽어 예측한 숫자를 반환
    """

    resized_data = resize_image(image_path)
    res = model.predict(resized_data)
    return int(res.argmax())


def resize_image(image_path: str) -> np.ndarray:
    """
    이미지 파일을 읽어 grayscale 처리하고 28x28 리사이징한 ndarray 데이터를 반환
    """

    with Image.open(image_path) as im:
        w, h = im.size
        min_size = min(w, h)
        if w > h:
            left, top = (w - min_size) // 2, 0
        else:
            left, top = 0, (h - min_size) // 2
        right = left + min_size
        bottom = top + min_size

        rect = (left, top, right, bottom)
        cropped_im = im.crop(rect).convert("L")  # Grayscale

        resized_im = cropped_im.resize((28, 28))
        resized_pixels = np.resize(resized_im, (1, 784))
        resized_data = ((np.array(resized_pixels) / 255) - 1) * -1

        return resized_data
