import sys
#yourpath
sys.path.append('/Users/zhaoziyu/IGinX/core/target/iginx-core-0.8.0-SNAPSHOT/udf_funcs/python_scripts/Unsupervised_Deep_Learning_of_Incompressible_Fluid_Dynamics')

from demo_interactive import sim

class MyTransformer:
    def __init__(self):
        pass

    def transform(self, rows):
        ret = [['t', 'v', 'p', 'a']]
        
        for row in rows[1:]:
            ret += sim(row[1], row[2], row[3])

        return ret
