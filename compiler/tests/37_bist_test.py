# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA. (See LICENSE for licensing information)


""" Run a regresion test on bist. """

import unittest
from testutils import header, AMC_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

class bist_test(AMC_test):

    def runTest(self):
        globals.init_AMC("config_20_{0}".format(OPTS.tech_name))
        
        global calibre
        import calibre
        OPTS.check_lvsdrc = False

        import bist

        #with async_bist=False ring-oscillator won't be added to design
        
        #minimum size is 3 bit 
        debug.info(1, "Testing 12bit bist")
        a = bist.bist(addr_size=5, data_size=16, delay = 5, async_bist=True, name="bist")
        self.local_check(a)

        debug.info(1, "Testing 12bit bist")
        a = bist.bist(addr_size=10, data_size=8, delay = 10, async_bist=False, name="bist2")
        self.local_check(a)
        
        # return it back to it's normal state
        OPTS.check_lvsdrc = True
        globals.end_AMC()
        
# instantiate a copdsay of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()