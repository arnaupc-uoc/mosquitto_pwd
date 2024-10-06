import json
from passlib.hash import pbkdf2_sha512


def generate_digest(password):
    """
    Generate a digest for the given password using pbkdf2_sha512.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The generated digest.
    """
    digest = pbkdf2_sha512.using(salt_size=12, rounds=101).hash(password)
    if '.' in digest:
        digest = digest.replace('.', '+')
    return digest.replace('$pbkdf2-sha512$', '$7$') + '=='


def is_valid_digest(password, hashed):
    """
    Verify if the given password matches the hashed digest.
    
    Args:
        password (str): The password to verify.
        hashed (str): The hashed digest to compare against.
    
    Returns:
        bool: True if the password matches the hashed digest, False otherwise.
    """
    normalized_hash = hashed.replace('$7$', '$pbkdf2-sha512$').rstrip('==')
    return pbkdf2_sha512.verify(password, normalized_hash)


def create_pwd(password):
    """
    Create a password digest and return it in a JSON format.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: A JSON string containing the password digests.
    """
    valid_pass = False
    while not valid_pass:
        digest = generate_digest(password)
        valid_pass = is_valid_digest(password, digest)

    hashes = {
        'password': password,
        'mosquitto': digest
    }

    return json.dumps(hashes)
