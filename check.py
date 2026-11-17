# rules.py 가 맞게 동작하는지 검사합니다.  실행: python check.py
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from config import GRACE_SEC
from rules import judge

cases = [
    ("2명",                  (2, None, False),          "NORMAL"),
    ("수신호 없이 1명",       (1, None, False),          "WARNING"),
    ("수신호 후 10초, 1명",   (1, 10, False),            "GRACE"),
    ("유예 시간 지남, 1명",   (1, GRACE_SEC + 1, False), "WARNING"),
    ("2명인데 쓰러짐",        (2, None, True),           "EMERGENCY"),
    ("유예 중 쓰러짐",        (1, 10, True),             "EMERGENCY"),
]

ok = 0
for name, args, want in cases:
    got = judge(*args)
    ok += got == want
    print(("✅" if got == want else "❌"), f"{name:<14} 기대 {want:<10} 결과 {got}")

print(f"\n{ok}/{len(cases)} 통과  (유예 시간 {GRACE_SEC}초)")
