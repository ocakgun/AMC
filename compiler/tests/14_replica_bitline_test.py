"""Run a regresion test on replica bitline. """

import unittest
from testutils import header,AMC_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

class replica_bitline_test(AMC_test):

    def runTest(self):
        globals.init_AMC("config_20_{0}".format(OPTS.tech_name))
        
        global calibre
        import calibre
        OPTS.check_lvsdrc = False

        import replica_bitline

        stages=2
        fanout=3
        rows=7
        debug.info(2, "Testing RBL with {0} FO4 stages, {1} rows".format(stages,rows))
        a = replica_bitline.replica_bitline(stages,fanout,rows)
        self.local_check(a)

        
        # return it back to it's normal state
        OPTS.check_lvsdrc = True
        globals.end_AMC()
        
# instantiate a copy of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()
