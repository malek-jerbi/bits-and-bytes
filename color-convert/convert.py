import sys
import re

sys.stdout.write(re.sub(r'\#[0-9a-fA-F]+', 'FOO', sys.stdin.read()))