import matplotlib.pyplot as plt
import numpy as np

def imprimirimg(train_dataset,labels, nr, nc):
    fig, ax = plt.subplots(nrows=nr, ncols=nc, figsize=(15, 12))
    idx = 0
    for i in range(4):
        for j in range(4):
            label = labels[np.argmax(train_dataset[0][1][idx])]
            ax[i, j].set_title(f"{label}")
            ax[i, j].imshow(train_dataset[0][0][idx][:, :, :])
            ax[i, j].axis("off")
            idx += 1

    # plt.tight_layout()
    plt.suptitle("Sample Training Images", fontsize=21)
    plt.show()