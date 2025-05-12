def create_test_data():
    print("Test data creation started...")
    # Simulate writing to a file or DB or API
    with open("dummy_data.txt", "w") as f:
        f.write("username: tomsmith\npassword: SuperSecretPassword!\n")
    print("Test data creation finished.")

if __name__ == "__main__":
    create_test_data()
