import hashlib
import secrets
import time

# === CONFIGURATION ===
OTP_LENGTH = 6
EXPIRY_SECONDS = 30
MAX_ATTEMPTS = 3

def generate_otp():
    return ''.join(secrets.choice("0123456789") for _ in range(OTP_LENGTH))

def hash_otp(otp, salt):
    return hashlib.sha3_256((otp + salt).encode()).hexdigest()

def save_otp_to_file(hashed_otp, salt, timestamp):
    with open("otp_hash.txt", "w") as file:
        file.write(f"{hashed_otp}\n{salt}\n{timestamp}")

def load_otp_from_file():
    with open("otp_hash.txt", "r") as file:
        hashed_otp = file.readline().strip()
        salt = file.readline().strip()
        timestamp = float(file.readline().strip())
    return hashed_otp, salt, timestamp

# === STEP 1: Register and Generate OTP ===
username = input("Enter username: ")
password = input("Enter password (min 12 characters): ")

if len(password) < 12:
    print("❌ Password too short.")
    exit()

otp = generate_otp()
salt = secrets.token_hex(4)
otp_hash = hash_otp(otp, salt)
timestamp = time.time()

save_otp_to_file(otp_hash, salt, timestamp)

print(f"\n🔐 OTP (for simulation): {otp}")
print(f"⌛ You have {EXPIRY_SECONDS} seconds to enter it.\n")

# === STEP 2: OTP Verification ===
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_otp = input("Enter OTP: ")
    hashed_otp, saved_salt, saved_timestamp = load_otp_from_file()
    
    # Check if OTP expired
    if time.time() - saved_timestamp > EXPIRY_SECONDS:
        print("⌛ OTP expired. Please request a new one.")
        break
    
    user_otp_hash = hash_otp(user_otp, saved_salt)
    
    if user_otp_hash == hashed_otp:
        print("✅ Access Granted!")
        break
    else:
        attempts += 1
        print(f"❌ Invalid OTP. Attempts left: {MAX_ATTEMPTS - attempts}")

if attempts == MAX_ATTEMPTS:
    print("🚫 Too many failed attempts. Try again later.")
