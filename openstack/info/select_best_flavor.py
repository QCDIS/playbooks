import json
import os
import sys
import tempfile

import numpy as np
from numpy.linalg import norm


def get_shorter_dist(available_instances, requested_instances):
    flavors = available_instances['openstack_flavors']
    selected_flavors = {}
    for requested_instance_name in requested_instances:
        min_dist = sys.maxsize
        requested_instance = requested_instances[requested_instance_name]
        requested_vector = np.array([int(requested_instance['mem_size'].split(' ')[0]),
                                     int(requested_instance['num_cores']),
                                     int(requested_instance['disk_size'].split(' ')[0])])
        for flavor in flavors:
            available_vector = np.array([flavor['ram'], flavor['vcpus'], flavor['disk']])
            dist = norm(requested_vector - available_vector)
            if dist < min_dist:
                min_dist = dist
                selected_flavor = {'flavor_id': flavor['id']}
                selected_flavors[requested_instance_name] = selected_flavor

    return selected_flavors


if __name__ == "__main__":
    available_instances_file_path = sys.argv[1]
    requested_instances_file_path = sys.argv[2]

    f = open(available_instances_file_path, )
    available_instances = json.load(f)

    f = open(requested_instances_file_path, )
    requested_instances = json.load(f)

    selected_flavors = get_shorter_dist(available_instances, requested_instances)
    instances = {'instances':selected_flavors}

    fd, filename = tempfile.mkstemp()

    with os.fdopen(fd, 'w') as tmp:
        # do stuff with temp file
        json.dump(instances, tmp)
    print(filename)
