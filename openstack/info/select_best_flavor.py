import json
import os
import sys
import tempfile

import numpy as np
from numpy.linalg import norm


def get_shorter_dist(available_instances, requested_instance):
    flavors = available_instances['openstack_flavors']

    requested_vector = np.array([int(requested_instance['mem_size'].split(' ')[0]),
                                 int(requested_instance['num_cores']),
                                 int(requested_instance['disk_size'].split(' ')[0])])

    min_dist = sys.maxsize
    selected_flavor = None
    for flavor in flavors:
        available_vector = np.array([flavor['ram'], flavor['vcpus'], flavor['disk']])
        dist = norm(requested_vector - available_vector)
        if dist < min_dist:
            min_dist = dist
            selected_flavor = flavor

    return selected_flavor


if __name__ == "__main__":
    available_instances_file_path = sys.argv[1]
    requested_instance_file_path = sys.argv[2]

    f = open(available_instances_file_path, )
    available_instances = json.load(f)

    f = open(requested_instance_file_path, )
    requested_instance = json.load(f)

    selected_flavor = get_shorter_dist(available_instances, requested_instance)
    fd, filename = tempfile.mkstemp()

    with os.fdopen(fd, 'w') as tmp:
        # do stuff with temp file
        json.dump(selected_flavor, tmp)
    print(filename)
