# import pyhash as hash

bit_vector = [0] * 20

# Non cryptographic hash function (Murmur and FNV)

fnv = hash.fnv1_32()

murmur = hash.murmur3_32()


# Calculate the ouptut of FNV and Mumur hash functions for Pickachu and Charmander

fnv_pika = fnv("Pikcahu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20