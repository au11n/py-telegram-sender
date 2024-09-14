# py-telegram-sender

py-telegram-sender is a simple and convenient Python library for sending messages and files via a Telegram bot.

## Installation
You can install py-telegram-sender using pip:

```
pip install py-telegram-sender
```

## Usage

### Basic Usage

```python
from py_telegram_sender import TelegramSender

# Create a TelegramSender instance
sender = TelegramSender('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')

# Send a text message
sender.send_msg('Hello, world!')

# Send a file
sender.send_file('Here is a document', '/path/to/your/file.txt')
```

### Using Backward Compatibility Functions

```python
from py_telegram_sender import set_credentials, send_msg, send_file

# Set credentials
set_credentials('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')

# Send a text message
send_msg('Hello, world!')

# Send a file
send_file('Here is a document', '/path/to/your/file.txt')
```

## Requirements

- Python 3.6+
- requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to the project! Please feel free to create an issue or pull request.   

## Contact

If you have any questions or suggestions, please create an issue in this repository.