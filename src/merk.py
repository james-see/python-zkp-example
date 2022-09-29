import merkletools  # type: ignore
import hashlib

# Generate merkletree object
mt = merkletools.MerkleTools()

# Generate some leaves
hex_data = '05ae04314577b2783b4be98211d1b72476c59e9c413cfb2afa2f0c68e0d93911'
print(f"Example hex data added to merkle tree as leaf directly: {hex_data}")
list_data = ['Some text data', 'perhaps']
print(f"Example list of values auto-added and auto-hashed strings added to tree as leaves for these values: {list_data}")

# Add data to the merkle tree
mt.add_leaf(hex_data)
mt.add_leaf(list_data, True)
mt.add_leaf("aaaaaa")

# Make the tree now that you have all the values you need. Note you can generate a lot of blanks first
mt.make_tree()
root = mt.get_merkle_root()
print(f"Root from the tree: {root}")

# hash testing
# this is the repeat of what is going on 
hash = hashlib.sha256(b'Some text data')
print(hash.digest())
# end hash testing
leaf_count = mt.get_leaf_count()
print(leaf_count)

print(f"All the leaves as byte strings: {mt.leaves}")
print(f"Here is the proof: {mt.get_proof(1)}")
print(f"Now the validation: {mt.validate_proof(mt.get_proof(1), hash.hexdigest(), mt.get_merkle_root())}")