import numpy as np
import cv2
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Logistic Map
def logistic_map(x0, n, r=3.9999):
    sequence = []
    x = x0
    for _ in range(n):
        x = r * x * (1 - x)
        sequence.append(x)
    return np.array(sequence)

# Henon Map
def henon_map(x0, y0, n, a=1.4, b=0.3):
    x, y = x0, y0
    sequence = []
    for _ in range(n):
        x_new = 1 - a * x**2 + y
        y = b * x
        x = x_new
        sequence.append(x)
    return np.array(sequence)

# Chebyshev Map
def chebyshev_map(x0, n, l=4):
    sequence = []
    x = x0
    for _ in range(n):
        x = np.cos(l * np.arccos(x))
        sequence.append(x)
    return np.array(sequence)

# Generate combined chaotic sequence
def generate_chaotic_sequence(length, x0_log, x0_henon, y0_henon, x0_cheby):
    logistic_seq = logistic_map(x0_log, length)
    henon_seq = henon_map(x0_henon, y0_henon, length)
    chebyshev_seq = chebyshev_map(x0_cheby, length)

    logistic_seq = np.abs((logistic_seq * 255).astype(np.uint8))
    henon_seq = np.abs((henon_seq * 255).astype(np.uint8))
    chebyshev_seq = np.abs((chebyshev_seq * 255).astype(np.uint8))

    chaotic_seq = np.bitwise_xor.reduce([logistic_seq, henon_seq, chebyshev_seq])
    return chaotic_seq

# Genetic crossover function
def crossover(data, key_stream):
    scrambled = data.copy()
    for idx in range(0, len(key_stream), 2):
        if idx + 1 < len(key_stream):
            scrambled[idx], scrambled[idx + 1] = scrambled[idx + 1], scrambled[idx]
    return scrambled

# RGB histogram plot
def display_rgb_histogram(image, title):
    colors = ('r', 'g', 'b')
    plt.figure()
    plt.title(f"Histogram of {title}")
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()

# Encryption process
def encrypt_color_image(image, chaotic_seq):
    encrypted_channels = []
    for i in range(3):  # R, G, B channels
        channel = image[:, :, i]
        scrambled = np.apply_along_axis(crossover, 1, channel, chaotic_seq[:channel.shape[1]])
        scrambled = np.apply_along_axis(crossover, 0, scrambled, chaotic_seq[:channel.shape[0]])
        chaotic_seq_reshaped = chaotic_seq[:channel.shape[0]].reshape(-1, 1)
        encrypted_channel = np.bitwise_xor(scrambled, chaotic_seq_reshaped)
        encrypted_channels.append(encrypted_channel)
    return cv2.merge(encrypted_channels)

# Decryption process
def decrypt_color_image(encrypted_image, chaotic_seq):
    decrypted_channels = []
    for i in range(3):
        channel = encrypted_image[:, :, i]
        chaotic_seq_reshaped = chaotic_seq[:channel.shape[0]].reshape(-1, 1)
        scrambled = np.bitwise_xor(channel, chaotic_seq_reshaped)
        scrambled = np.apply_along_axis(crossover, 0, scrambled, chaotic_seq[:channel.shape[0]])
        scrambled = np.apply_along_axis(crossover, 1, scrambled, chaotic_seq[:channel.shape[1]])
        decrypted_channels.append(scrambled)
    return cv2.merge(decrypted_channels)

# Correlation analysis
def calculate_correlation(image):
    height, width, _ = image.shape
    def compute_corr(pairs):
        x, y = zip(*pairs)
        x = np.array(x)
        y = np.array(y)
        covariance = np.mean(x * y) - (np.mean(x) * np.mean(y))
        std_x = np.std(x)
        std_y = np.std(y)
        return covariance / (std_x * std_y)
    results = []
    for i in range(3):
        channel = image[:, :, i]
        horizontal = [(channel[x, y], channel[x, y + 1]) for x in range(height) for y in range(width - 1)]
        vertical = [(channel[x, y], channel[x + 1, y]) for x in range(height - 1) for y in range(width)]
        results.append((compute_corr(horizontal), compute_corr(vertical)))
    return np.mean([r[0] for r in results]), np.mean([r[1] for r in results])

# Run
if __name__ == "__main__":
    img_path = "sampleimage.jpg"  # Change if needed
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

    if img is None:
        print("Error: Could not load image.")
    else:
        plt.imshow(img)
        plt.title("Original Image")
        plt.axis('off')
        plt.show()
        display_rgb_histogram(img, "Original Image")

        height, width, _ = img.shape
        x0_log, x0_henon, y0_henon, x0_cheby = 0.4999, 0.21, 0.21, 0.4999
        chaotic_seq = generate_chaotic_sequence(max(height, width), x0_log, x0_henon, y0_henon, x0_cheby)

        encrypted_img = encrypt_color_image(img, chaotic_seq)
        plt.imshow(encrypted_img)
        plt.title("Encrypted Image")
        plt.axis('off')
        plt.show()
        display_rgb_histogram(encrypted_img, "Encrypted Image")

        decrypted_img = decrypt_color_image(encrypted_img, chaotic_seq)
        plt.imshow(decrypted_img)
        plt.title("Decrypted Image")
        plt.axis('off')
        plt.show()
        display_rgb_histogram(decrypted_img, "Decrypted Image")

        plain_corr = calculate_correlation(img)
        cipher_corr = calculate_correlation(encrypted_img)
        decrypted_corr = calculate_correlation(decrypted_img)

        table = PrettyTable()
        table.field_names = ["Direction", "Plain Image", "Cipher Image", "Decrypted Image"]
        table.add_row(["Horizontal", f"{plain_corr[0]:.5f}", f"{cipher_corr[0]:.5f}", f"{decrypted_corr[0]:.5f}"])
        table.add_row(["Vertical", f"{plain_corr[1]:.5f}", f"{cipher_corr[1]:.5f}", f"{decrypted_corr[1]:.5f}"])
        print(table)
