def valid_threads(arguments):
    default_threads = 6
    try:
        threads = int(arguments.threads)
        if 0 < threads <= 60:
            return threads
        else:
            print(f"[!] Invalid threads parameter: {arguments.threads}, default value will be used")
            return default_threads
    except ValueError:
        print(f"[!] Invalid threads parameter: {arguments.threads}, default value will be used")
        return default_threads
