from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Create a new image to store the encrypted pixels
    encrypted_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel and apply encryption
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Apply encryption algorithm (for example, XOR with a key)
            r ^= key
            g ^= key
            b ^= key
            encrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    
    # Create a new image to store the decrypted pixels
    decrypted_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel and apply decryption
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_img.getpixel((x, y))
            # Apply decryption algorithm (in this case, XOR with the same key)
            r ^= key
            g ^= key
            b ^= key
            decrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

# Example usage
image_path = "example_image.png"
key = 123  # Choose a key for encryption/decryption
encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
