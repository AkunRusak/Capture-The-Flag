def menu():
    print("CTF Helper Menu")
    print("1. Run SQLi Fuzzer")
    print("2. Run XSS Scanner")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        import sqli_fuzzer
    elif choice == "2":
        import xss_scanner
    else:
        print("Exiting...")

menu()