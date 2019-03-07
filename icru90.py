import os
import sys
import logging

import numpy as np
import matplotlib.pyplot as plt


res_dir = "./res"

file_list = (
    # filename, z, a, target_id
    ("icru90_h1_air.csv", 1, 1, 104),
    ("icru90_h1_graphite.csv", 1, 1, 906),
    ("icru90_h1_water.csv", 1, 1, 276),
    ("icru90_he4_air.csv", 2, 4, 104),
    ("icru90_he4_graphite.csv", 2, 4, 906),
    ("icru90_he4_water.csv", 2, 4, 276),
    ("icru90_c12_air.csv", 6, 12, 104),
    ("icru90_c12_graphite.csv", 6, 12, 906),
    ("icru90_c12_water.csv", 6, 12, 276)
    )


def read_icru90():
    """
    """

    data = []
    for i, f in enumerate(file_list):
        fn = os.path.join(res_dir, f[0])
        print(fn)
        data.append(np.genfromtxt (fn, delimiter=",", skip_header=3))

    return data


def main(args=sys.argv[1:]):
    # something
    data = read_icru90()

    d = data[0]

    plt.loglog(d[:,0],d[:,1],'s')
    plt.show()


if __name__ == '__main__':
    logging.basicConfig()
    sys.exit(main(sys.argv[1:]))
