from PIL import Image

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Get the pixel data
    pixels = img.load()
    
    # Encrypting the image by swapping pixel values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example of pixel manipulation: swapping red and blue components
            pixels[x, y] = (b, g, r)
    
    # Save the encrypted image
    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print("Image encrypted and saved as", encrypted_path)

def decrypt_image(image_path):
    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size
    
    # Get the pixel data
    pixels = img.load()
    
    # Decrypting the image by swapping pixel values back
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example of pixel manipulation: swapping red and blue components back
            pixels[x, y] = (b, g, r)
    
    # Save the decrypted image
    decrypted_path = image_path.split('_encrypted.')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print("Image decrypted and saved as", decrypted_path)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt the image? (e/d): ").strip().lower()
        if choice not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        image_path = input("Enter the path to the image file: ").strip()

        if choice == 'e':
            encrypt_image(image_path)
        else:
            decrypt_image(image_path)

        another = input("Do you want to continue? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
