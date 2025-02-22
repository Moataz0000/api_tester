import argparse
from .client import MakeAPICall


def main():
    parser = argparse.ArgumentParser(description="API Tester CLI Tool")
    parser.add_argument("method", type=str, help="HTTP Method (GET, POST, PUT, PATCH, DELETE)")
    parser.add_argument("url", type=str, help="API Base URL")
    parser.add_argument("endpoint", type=str, help="API Endpoint")
    parser.add_argument("--data", type=str, help="Request Data (JSON format)", default="{}")

    args = parser.parse_args()


    client = MakeAPICall(args.url)
    response = client.request(args.method, args.endpoint, json=eval(args.data))

    print("Response Status: ", response.status_code)
    print("Response Body: ", response.json())


if __name__ == "__main__":
    main()