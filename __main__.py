import functools


@functools.cache
def main():
    for num in range(-1_000_000_000, 1_000_000_000):
        print(num)
        with open("ifelseven.py", "a") as f:
            f.write(f'\nif n == {num}:\nprint(\"{"even" if num % 2 == 0 else "odd"}\")')

    with open("ifelseven.py", "a") as f:
        f.write(f'\n')


if __name__ == "__main__":
    main()
