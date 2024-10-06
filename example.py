import sys

# Add module folder if not installed
# sys.path.append('src/mosquitto_pwd')
# import mosquitto_pwd as mp

# with package installed
from mosquitto_pwd import mosquitto_pwd as mp




def main(password):

    # Generate a digest
    digest = mp.generate_digest(password)
    print("Digest:", digest)

    # Verify the digest
    is_valid = mp.is_valid_digest(password, digest)
    print("Is valid:", is_valid)

    # Create password digests in JSON format
    json_hashes = mp.create_pwd(password)
    print("JSON Hashes:", json_hashes)


if __name__ == "__main__":
    # Default password
    password = "admin"
    # Check if a password is provided as an argument
    if len(sys.argv) > 1:
        password = sys.argv[1]
    # Run the main function
    main(password)
