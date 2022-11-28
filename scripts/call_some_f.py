import argparse
import sub_pack_1
import sub_pack_2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="simply call a func from one of the two sub-packages"
    )
    parser.add_argument("caller", type=str, default="Unnamed Caller")
    parser.add_argument("sub_package", type=int, default=1, choices=[1, 2])
    args = parser.parse_args()

    if args.sub_package == 1:
        res = sub_pack_1.func(caller_name=args.caller)
    elif args.sub_package == 2:
        res = sub_pack_2.func(caller_name=args.caller)

    else:
        raise ValueError(f"unexpected sub_package: {args.sub_package}")

    print(res)
