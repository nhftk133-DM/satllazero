'''
    @file get_image.py
    @brief Capture Image for SATLLA0 OBC.

    Copyright (C) 2023 @author Shai Aharon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os
import sys
import LIT

# import matplotlib.pyplot as plt
def main(fld_path):
    if not os.path.isdir(fld_path):
        print("{} is not a directory".format(fld_path))
        exit()

    img = LIT.LoadImage(fld_path)

    # plt.imshow(img)
    # plt.show()


if __name__ == '__main__':
    main(sys.argv[1])
