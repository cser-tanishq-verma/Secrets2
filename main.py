import os

def main():
    # Retrieve the secret token from the environment variable
    secret_token = os.environ.get("MY_SECRET_TOKEN")
    
    if not secret_token:
        print("❌ Error: MY_SECRET_TOKEN environment variable is not set.")
        print("Please ensure you have configured the GitHub Secret and passed it in the workflow file.")
        exit(1)
    
    print("✅ Successfully accessed the secret token from environment variables!")
    print(f"🔒 Secret length: {len(secret_token)} characters")
    
    # We do NOT print the actual secret to avoid leaking it in logs.
    # Note: GitHub Actions automatically masks secrets that are printed,
    # but it is best practice not to print them in the first place.
    if len(secret_token) > 2:
        masked = secret_token[0] + "*" * (len(secret_token) - 2) + secret_token[-1]
    else:
        masked = "**"
    print(f"👀 Masked preview: {masked}")

if __name__ == "__main__":
    main()
