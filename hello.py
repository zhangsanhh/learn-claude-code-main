def greet(name: str) -> str:
    """生成一条问候消息。

    Args:
        name: 被问候对象的名字。

    Returns:
        格式化后的问候字符串。
    """
    return f"Hello, {name}!"


def main() -> None:
    """程序主入口：打印问候语。"""
    message: str = greet("World")
    print(message)


if __name__ == "__main__":
    main()
