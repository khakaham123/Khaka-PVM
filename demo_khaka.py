import sys

print("Khaka DictCap PVM")
print("Python:", sys.version)
print("Initial limit:", sys.get_max_dict_size())
sys.set_max_dict_size(3)
d = {"a": 1, "b": 2, "c": 3}
d["a"] = 99
print("Existing-key update:", d)
try:
    d["d"] = 4
except ValueError as exc:
    print("Expected limit error:", exc)
else:
    raise SystemExit("FAIL: fourth key was accepted")
assert len(d) == 3 and d["a"] == 99
sys.set_max_dict_size(-1)
d["d"] = 4
assert len(d) == 4
print("Khaka PVM demo passed.")
