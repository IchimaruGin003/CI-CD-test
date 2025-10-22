def dedupe(items):
    """去除列表中的重复元素"""
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

def add_numbers(a, b):
    """加法功能 - 新添加的功能"""
    return a + b

if __name__ == "__main__":
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    result = list(dedupe(sample_data))
    print(f"Original: {sample_data}")
    print(f"After dedupe: {result}")

    # 新功能演示 - 加法
    sum_result = add_numbers(10, 5)
    print(f"加法演示: 10 + 5 = {sum_result}")