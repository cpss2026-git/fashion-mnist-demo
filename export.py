import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf

model = tf.keras.models.load_model("model.keras", compile=False)
model.export("export")
print("Model was exported.")
