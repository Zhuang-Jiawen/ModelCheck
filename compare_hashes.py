import argparse


def parse_hash_file(file_path):
    hash_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # 跳过空行和nohup警告
            if not line or line.startswith("nohup:"):
                continue
            # 分割哈希和路径
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue  # 跳过格式错误的行
            file_hash, file_path = parts
            hash_dict[file_path] = file_hash
    return hash_dict


def compare_hash_dicts(dict_a, dict_b):
    all_files = set(dict_a.keys()) | set(dict_b.keys())
    results = {
        'added': [],
        'removed': [],
        'modified': [],
        'same': []
    }

    for file in all_files:
        hash_a = dict_a.get(file)
        hash_b = dict_b.get(file)

        if hash_a is None:
            results['added'].append(file)
        elif hash_b is None:
            results['removed'].append(file)
        elif hash_a != hash_b:
            results['modified'].append(file)
        else:
            results['same'].append(file)

    return results


def main():
    parser = argparse.ArgumentParser(description="Compare two hash lists")
    parser.add_argument("file_a", default="hash_list_A.txt",help="Path to first hash list (e.g. hash_list_A.txt)")
    parser.add_argument("file_b", default="hash_list_B.txt",help="Path to second hash list (e.g. hash_list_B.txt)")
    args = parser.parse_args()

    dict_a = parse_hash_file(args.file_a)
    dict_b = parse_hash_file(args.file_b)

    comparison = compare_hash_dicts(dict_a, dict_b)

    print(f"Files only in {args.file_a}: {len(comparison['removed'])}")
    for f in comparison['removed']:
        print(f"  - {f}")

    print(f"\nFiles only in {args.file_b}: {len(comparison['added'])}")
    for f in comparison['added']:
        print(f"  - {f}")

    print(f"\nModified files: {len(comparison['modified'])}")
    for f in comparison['modified']:
        print(f"  - {f} (A: {dict_a[f]}, B: {dict_b[f]})")

    print(f"\nSame files: {len(comparison['same'])}")


if __name__ == "__main__":
    main()