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

class Point:
    def __init__(self,x,y):
        self.x= x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"




def addition(point_a,point_b,a,mod):
    slope = 0
    if point_a==point_b:
        slope= (3*point_a.x*point_a.x) + a
        slope = slope * inverse_of(2*point_a.y,mod)
    else:
        slope = point_b.y - point_a.y
        slope = slope * inverse_of(point_b.x-point_a.x,mod)
    slope = slope %mod
    x3= (slope*slope -point_a.x - point_b.x) % mod
    y3 = (slope*(point_a.x-x3)-point_a.y)%mod
    return Point(x3,y3)



def mutliple_of_point(point,multiple,a,p):
    running_point = point
    list_of_points = []
    bitmask =  1
    #check with &bitmask
    while multiple:
        if(multiple&bitmask):
            list_of_points.append(running_point)
        running_point = addition(running_point,running_point,a,p)
        multiple = multiple >> 1
    running_point = list_of_points[-1]
    list_of_points.pop()
    for i in range(len(list_of_points)):
        running_point=addition(list_of_points[i],running_point,a,p)
    return running_point

a = 497
p = 9739
p1 = Point(2339, 2213)
mul =  7863
print(mutliple_of_point(p1,mul,a,p))


s0 = Point(1804,5368)
s1 = Point(4929,8240)
s2 = Point(7909,7508)
s3 = Point(5697,8702)

C = addition(s0,s1,a,p)
D = addition(s2,s2,a,p)
print(addition(C,D,a,p))



