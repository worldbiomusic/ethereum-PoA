import sys
from web3 import Web3
from eth_account import Account

def extract_private_key(keystore_path, password):
    try:
        # Keystore 파일 읽기
        with open(keystore_path, "r") as file:
            keystore = file.read()

        # 프라이빗 키 복구
        private_key = Account.decrypt(keystore, password)
        return private_key.hex()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 명령줄 인자 확인
    if len(sys.argv) != 3:
        print("Usage: python script.py <keystore-file-path> <password>")
        sys.exit(1)

    # 첫 번째 인자: Keystore 파일 경로
    keystore_path = sys.argv[1]

    # 두 번째 인자: Keystore 암호
    password = sys.argv[2]

    # 프라이빗 키 추출
    private_key = extract_private_key(keystore_path, password)
    print("Private Key:", private_key)
