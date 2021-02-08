import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import random


def load_dataset_batch(path):
    with open(path, "rb") as f:
        data = pickle.load(f, encoding="bytes")
    return data


def load_cifar_train(root_path):
    train_data = []
    for i in range(1, 6):
        filename = f"data_batch_{i}"
        train_data = load_dataset_batch(os.path.join(root_path, filename))
    train_data = decode_data(train_data)
    return train_data


def load_cifar_test(root_path):
    filename = "test_batch"
    test_data = load_dataset_batch(os.path.join(root_path, filename))
    test_data = decode_data(test_data)
    return test_data


def decode_data(raw_data):
    images = raw_data[b"data"]  # Load Data
    images = images.reshape(10000, 3, 32, 32)  # Reshape into RGB Images
    images = np.moveaxis(images, 1, -1)  # Convert Channels First to Channels Last

    labels = raw_data[b"labels"]

    return np.array(images), np.array(labels)


def get_cifar_label_names(root_path):
    label_names = load_dataset_batch(os.path.join(root_path, "batches.meta"))[
        b"label_names"
    ]
    label_names = [label.decode() for label in label_names]

    return label_names


def visualize_batch(images, labels, label_names, title="Sample Dataset"):
    num_examples = 36

    # Get Random Batch of Data
    dataset = list(zip(images, labels))
    dataset_batch = random.sample(dataset, num_examples)

    # Set Subplot Params
    axis_length = int(np.sqrt(num_examples))
    fig, axs = plt.subplots(axis_length, axis_length)
    fig.set_size_inches(10, 10)
    plt.suptitle(title, fontsize=25)
    index = 0

    # Plot images
    for i in range(axis_length):
        for j in range(axis_length):
            axs[i, j].imshow(dataset_batch[index][0])
            axs[i, j].set_title(label_names[dataset_batch[index][1]])
            axs[i, j].axis("off")
            index += 1

    plt.show()
