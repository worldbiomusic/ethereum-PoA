import sys
import sha3  # pysha3 라이브러리

def to_checksum_address(address):
    # Remove '0x' prefix and convert to lowercase
    address = address.lower().replace("0x", "")
    # Compute Keccak-256 hash of the address
    keccak = sha3.keccak_256()
    keccak.update(address.encode('utf-8'))
    address_hash = keccak.hexdigest()
    # Apply checksum formatting
    checksum_address = "0x"
    for i, char in enumerate(address):
        if int(address_hash[i], 16) >= 8:
            checksum_address += char.upper()
        else:
            checksum_address += char
    return checksum_address

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python eip55.py <address>")
        sys.exit(1)
    input_address = sys.argv[1]
    try:
        checksum_address = to_checksum_address(input_address)
        print("Checksum Address:", checksum_address)
    except Exception as e:
        print(f"Error: {e}")
