# MosquittoPwd

## Description

`MosquittoPwd` is a Python module that provides methods to generate and verify mosquitto password digest using `pbkdf2_sha512`. It also provides a method to create a JSON string containing the password digest.

`pbkdf2-sha512` will generate something like:
`$pbkdf2-sha512$101$RsfyboeO.Wmd2Qig$8fTVPoDsy87q9N9k52MlR9RcIF3N4SCFfft/kctp/..frxpRgBtfYhTuOrBt/clsKw83vkLvuxDka1JZCEE3hA==`

We replace to the first part with `$7$` because that is how mosquitto understands which scheme the password hash is.

There is some inconsistency in mosquitto.
Whenever there is a `.` character in the the password part of the hash or in the salt part, mosquitto discards the credentials outright. Generating digests including `.` replaced by `+` accepts the credentials.

## Methods

### `generate_digest(password)`

Generate a digest for the given password using `pbkdf2_sha512`.

- **Args**:
  - `password` (str): The password to hash.
- **Returns**:
  - `str`: The generated digest.

### `is_valid_digest(password, hashed)`

Verify if the given password matches the hashed digest.

- **Args**:
  - `password` (str): The password to verify.
  - `hashed` (str): The hashed digest to compare against.
- **Returns**:
  - `bool`: True if the password matches the hashed digest, False otherwise.

### `create_pwd(password)`

Create a password digest and return it in a JSON format.

- **Args**:
  - `password` (str): The password to hash.
- **Returns**:
  - `str`: A JSON string containing the password digest.


## Useful Links

- [mosquitto_passwd man page](https://mosquitto.org/man/mosquitto_passwd-1.html)
- [Inconsistency with PBKDF2_SHA512 password hashing when using script as opposed to mosquitto_passwd](https://www.eclipse.org/lists/mosquitto-dev/msg02847.html)
- [Broker does not accept PBKDF2_SHA512 digests that contain . character in them](https://github.com/eclipse/mosquitto/issues/2847)
