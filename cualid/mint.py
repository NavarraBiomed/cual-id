import uuid


def hamming(s1, s2):
    count_diff = 0
    for i1, i2 in zip(s1, s2):
        if i1 != i2:
            count_diff += 1
    return count_diff


def greater_than_distance(query, existing, d=2):
    for e in existing:
        if hamming(query, e) <= d:
            return False
    return True


def create_ids(n, id_length, distance=2):
    uuids = []
    hrids = []
    while len(hrids) < n:
        uuid_ = uuid.uuid4()
        hrid = uuid_.hex[-id_length:]
        if greater_than_distance(hrid, hrids):
            uuids.append(uuid_)
            hrids.append(hrid)
            yield (uuid_, hrid)