import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf


def get_data():
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    return (train_images, train_labels, test_images, test_labels)


model = tf.keras.models.load_model("model.keras", compile=False)

train_images, train_labels, test_images, test_labels = get_data()

test_num = 100
predictions = np.array(model(test_images[:test_num]))
predicted_labels = np.argmax(model(test_images[:test_num]), axis=1)

label_names = [
    "Top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Boot",
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

correct_num = 0
for i in range(test_num):
    true_label = label_names[test_labels[i]]
    pred_label = label_names[predicted_labels[i]]

    if test_labels[i] == predicted_labels[i]:
        result = f"{GREEN}Correct{RESET}"
        correct_num += 1
    else:
        result = f"{RED}IncorrectL{RESET}"

    print(f"{i:2d}: true={true_label:8s} pred={pred_label:8s} {result}")
accuracy = correct_num / test_num

print()
print(f"Accuracy: {correct_num}/{test_num} = {accuracy:.2%}")
