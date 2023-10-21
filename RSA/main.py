def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p
    
def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

# Create an empty dictionary to store the key-value pairs
config = {}

with open('variables.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(' = ')
        config[key] = value

p1 = int(config['p1'])
p2 = int(config['p2'])
pub = int(config['public_key'])
encrypt = int(config['encrypt'])
msg = config['message']

modulos = p1*p2
phi_n = (p1-1)*(p2-1)
_,priv,_ = extended_euclidean_algorithm(pub,phi_n)
priv = priv%phi_n
pack_length = len(str(modulos))

if encrypt:
    msg_list = [ord(char) for char in list(msg)]
    base_msg = msg_list
    for i in range(pub-1):
        msg_list = [(char*base_char)%modulos for char,base_char in zip(msg_list,base_msg)]
    msg_list = [("0"*(pack_length-len(str(msg))))+str(msg) for msg in msg_list]
    print(''.join(msg_list))

else: #decrypt. Msg is encrypted
    msg_list = [msg[i:i+pack_length] for i in range(0,len(msg),pack_length)]
    msg_list = [int(msg) for msg in msg_list]
    priv_base_msg =msg_list
    for i in range(priv-1):
        msg_list = [(char*base_char)%modulos for char,base_char in zip(msg_list,priv_base_msg)]
    msg_list = [chr(c) for c in msg_list]
    print(''.join(msg_list))




