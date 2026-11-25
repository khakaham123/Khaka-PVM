import sys


class SplitTable:
    def __init__(self):
        self.first = 1


def set_second(instance):
    instance.second = 3


def main():
    assert sys.get_max_dict_size() == -1
    try:
        sys.set_max_dict_size(3)
        assert sys.get_max_dict_size() == 3

        values = {}
        values["a"] = 1
        values["b"] = 2
        values["c"] = 3
        values["a"] = 99
        assert values == {"a": 99, "b": 2, "c": 3}

        try:
            values["d"] = 4
        except ValueError as exc:
            assert str(exc) == "DictCapPVM: dictionary size limit exceeded"
        else:
            raise AssertionError("inserting a fourth key was not blocked")
        assert "d" not in values
        print("Capped dict: 3 keys; update allowed; fourth key rejected")

        sys.set_max_dict_size(2)
        defaults = {}
        assert defaults.setdefault("a", 1) == 1
        assert defaults.setdefault("b", 2) == 2
        assert defaults.setdefault("a", 99) == 1
        try:
            defaults.setdefault("c", 3)
        except ValueError as exc:
            assert str(exc) == "DictCapPVM: dictionary size limit exceeded"
        else:
            raise AssertionError("setdefault inserted beyond the dictionary cap")
        print("setdefault: existing key allowed; new key rejected")

        instance = SplitTable()
        for _ in range(20):
            set_second(instance)
            del instance.second
        sys.set_max_dict_size(1)
        instance.first = 2
        try:
            set_second(instance)
        except ValueError as exc:
            assert str(exc) == "DictCapPVM: dictionary size limit exceeded"
        else:
            raise AssertionError("optimized split-table insertion was not blocked")
        assert instance.__dict__.setdefault("first", 99) == 2
        try:
            instance.__dict__.setdefault("third", 3)
        except ValueError as exc:
            assert str(exc) == "DictCapPVM: dictionary size limit exceeded"
        else:
            raise AssertionError("split-table setdefault exceeded the dictionary cap")
        print("Split-table dict: update allowed; new attribute rejected")

        sys.set_max_dict_size(0)
        values["d"] = 4
        assert len(values) == 4
        sys.set_max_dict_size(-1)
        values["e"] = 5
        assert len(values) == 5
        assert sys.get_max_dict_size() == -1
        print("Disabled cap: dictionary growth resumed")
        print("DictCapPVM demo passed")
    finally:
        sys.set_max_dict_size(-1)


if __name__ == "__main__":
    main()
