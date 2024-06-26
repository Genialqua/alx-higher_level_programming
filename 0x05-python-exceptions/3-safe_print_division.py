#!/usr/bin/python3
#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {:.1f}".format(result))
        return (result)
