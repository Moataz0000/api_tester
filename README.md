# restquest

## Overview
`restquest` is a command-line tool for testing REST API endpoints with various HTTP methods (GET, POST, PUT, PATCH, DELETE). It simplifies API testing by allowing developers to quickly send requests and view responses directly from the terminal.

## Features
- Supports `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests.
- User-friendly command-line interface.
- Displays JSON responses in a readable format.
- Custom headers and request body support.
- Error handling and response status display.

## Installation

You can install `restquest` from PyPI:
```bash
pip install restquest
```

Or install it locally in editable mode for development:
```bash
git clone https://github.com/Moataz0000/api-tester.git
cd api-tester
pip install -e .
```

## Usage

### Sending a GET request
```bash
api-tester GET https://jsonplaceholder.typicode.com/posts/1
```

### Sending a POST request with JSON data
```bash
api-tester POST https://jsonplaceholder.typicode.com/posts -d '{"title": "Test Post", "body": "This is a test", "userId": 1}'
```

### Sending a PUT request
```bash
api-tester PUT https://jsonplaceholder.typicode.com/posts/1 -d '{"title": "Updated Title"}'
```

### Sending a DELETE request
```bash
api-tester DELETE https://jsonplaceholder.typicode.com/posts/1
```

### Using custom headers
```bash
api-tester GET https://api.example.com/data -H 'Authorization: Bearer YOUR_TOKEN'
```

## Contributing
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Developed by [Moataz Fawzy](https://github.com/Moataz0000).

