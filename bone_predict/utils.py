from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from keras.metrics import mean_absolute_error


def mae_in_months(x_p, y_p):
    """function to return mae in months"""
    return mean_absolute_error(
        (41.182021399396326 * x_p + 127.3207517246848),
        (41.182021399396326 * y_p + 127.3207517246848),
    )


def predict(path):
    model = load_model(
        "best_model.h5",
        custom_objects={"mae_in_months": mae_in_months},
    )
    image = Image.open(path)

    if image.mode != "RGB":
        image = image.convert("RGB")

    target_size = (256, 256)
    image = image.resize(target_size)

    img_array = img_to_array(image)

    img_array = np.expand_dims(img_array, axis=0)

    img = (img_array - 127.3207517246848) / 41.182021399396326

    pred = (127.3207517246848 + 41.182021399396326 * model.predict(img)) / 12

    print(f"Predicted bone age: {pred}")

    return pred
