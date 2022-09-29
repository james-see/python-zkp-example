import merkletools  # type: ignore
import hashlib

mt = merkletools.MerkleTools()

hex_data = '05ae04314577b2783b4be98211d1b72476c59e9c413cfb2afa2f0c68e0d93911'
print(f"Example hex data added to merkle tree as leaf directly: {hex_data}")
list_data = ['Some text data', 'perhaps']
print(f"Example list of values auto-added and auto-hashed strings added to tree as leaves for these values: {list_data}")
mt.add_leaf(hex_data)
mt.add_leaf(list_data, True)
mt.add_leaf("aaaaaa")
mt.make_tree()
root = mt.get_merkle_root()
print(root)
# hash testing
hash = hashlib.sha256(b'Some text data')
print(hash.digest())
# end hash testing
leaf_count = mt.get_leaf_count()
print(leaf_count)

print(mt.leaves)
print(mt.get_proof(1))
print(mt.validate_proof(mt.get_proof(1), hash.hexdigest(), mt.get_merkle_root()))

