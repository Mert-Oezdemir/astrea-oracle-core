import json
from . import AstreaOracle, Profile

def main():
    first = Profile("sample-a", 26, True, ("art", "hiking"), ("kindness",), "aries")
    second = Profile("sample-b", 28, True, ("hiking",), ("kindness",), "libra")
    print(json.dumps(AstreaOracle().match(first, second).to_dict(), indent=2))

if __name__ == "__main__":
    main()
