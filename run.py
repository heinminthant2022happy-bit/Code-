import aa

if name == "main":
    try:
        # Execute the main function from compiled aa.so
        aa.main()
    except AttributeError:
        print("Error: Function 'main' not found in aa.so")
    except Exception as e:
        print(f"Runtime Error: {e}")
