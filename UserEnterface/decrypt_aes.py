from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

# Encrypted data (base64)
encrypted_b64 = "3MVRZ6AWWO/kmwIwkwUNpMh5XoUWySiWUtwYIeelX2znmVm2jpfuVlsogHIQEvif2GPp8xBP83Fs5vgTYtD1ZQ=="

# Secret key string
secret_key_str = "Certificate IV in Cyber Security"

# Derive 32-byte key using SHA-256 hash of the secret key string
key = hashlib.sha256(secret_key_str.encode()).digest()

# Decode base64 ciphertext
encrypted_bytes = b64decode(encrypted_b64)

# Assume the first 16 bytes are IV
iv = encrypted_bytes[:16]

# The actual ciphertext is after the IV
ciphertext = encrypted_bytes[16:]

# Create AES cipher object for decryption (AES-256-CBC)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad the plaintext
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted Text:", plaintext.decode())
