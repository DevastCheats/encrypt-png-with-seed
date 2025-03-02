from PIL import Image
import random

def encrypt_image(seed, choicefilencrypted, choicefildecrypted):
    random.seed(seed)
    img = Image.open(choicefilencrypted)
    width, height = img.size
    encrypted_img = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            original_pixel = img.getpixel((x, y))
            random_color = tuple(random.randint(0, 255) for _ in range(3))
            encrypted_pixel = tuple(a ^ b for a, b in zip(original_pixel, random_color))
            encrypted_img.putpixel((x, y), encrypted_pixel)
    encrypted_img.save(choicefildecrypted)
    print(f"Saved encrypted image to {choicefildecrypted}")

def decrypt_image(seed, choicefildecrypted, output_filename):
    random.seed(seed)
    encrypted_img = Image.open(choicefildecrypted)
    width, height = encrypted_img.size
    decrypted_img = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            random_color = tuple(random.randint(0, 255) for _ in range(3))
            decrypted_pixel = tuple(a ^ b for a, b in zip(encrypted_pixel, random_color))
            decrypted_img.putpixel((x, y), decrypted_pixel)
    decrypted_img.save(output_filename)
    print(f"Saved decrypted image to {output_filename}")

def main():
    while True:
        choice = input("1 - encrypt, 2 - decrypt image: ")
        if choice not in ['1', '2']:
            print("Choose 1, 2")
            continue

        encryption_seed = int(input("Seed of crypt: "))

        if choice == '1':
            choicefilencrypted = input("Name of file to encrypt: ")
            choicefildecrypted = input("Name of file to save encrypted image: ")
            encrypt_image(encryption_seed, choicefilencrypted, choicefildecrypted)
        elif choice == '2':
            choicefildecrypted = input("Name of file to decrypt: ")
            output_filename = input("Name of file to save decrypted image: ")
            decrypt_image(encryption_seed, choicefildecrypted, output_filename)
main()