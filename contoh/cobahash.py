#
# Contoh fungsi hash

import hashlib
h = hashlib.sha256("beli 10000\n")
print h.hexdigest()
