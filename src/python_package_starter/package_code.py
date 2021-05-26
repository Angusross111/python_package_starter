from .sub_package import bar_fn, foo_fn
def main():
	print("Executing main() in package_code.py")
	bar_fn()
	foo_fn()

if __name__ == '__main__':
    main()
