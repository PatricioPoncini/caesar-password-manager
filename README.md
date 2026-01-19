# `🌿 Caesar Password Manager`
A lightweight, terminal-based password manager written in Python. This tool allows you to store and retrieve your credentials securely using a custom Caesar Cipher implementation.

## `Features`
- **Custom Encryption**: Protects your data using a Caesar Cipher (shifting letters, numbers, and symbols).
- **Persistent Storage**: Saves your credentials in a local .txt file.
- **Clean UI**: Displays your saved passwords in a well-formatted table using the tabulate library.
- **User-Friendly Menu**: Simple command-line interface for easy navigation.

## `How it works`
The application applies a mathematical shift to every character you input.
- **Encryption**: Moves characters forward by a specific SHIFT value.
- **Decryption**: Moves characters backward by the same SHIFT value when reading the file.
- **Formatting**: Data is stored using a custom separator (;|) and cleaned using .strip() to ensure a perfect display.

> [!WARNING]
> This project uses the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher), which is intended for educational purposes only. For production environments or sensitive personal data, consider using more advanced encryption standards.

## `Installation`
1. Clone the repository:
```shell
git clone https://github.com/PatricioPoncini/caesar-password-manager.git
cd caesar-password-manager
```

2. Install dependencies: This project uses tabulate for table formatting.
```shell
pip install tabulate
```

## `Usage`

Run the main script using Python:
```shell
python main.py
```

### `Menu Options`
- New password: Enter the software name, username, and password to encrypt and save.
- View passwords: Decrypts and displays all stored credentials in an aligned table.
- Exit: Closes the application.

### `Menu Options`
- New password: Enter the software name, username, and password to encrypt and save.
- View passwords: Decrypts and displays all stored credentials in an aligned table.
- Exit: Closes the application.