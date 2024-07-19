import sys
#yourpath
sys.path.append('/Users/IGinX/core/target/iginx-core-0.8.0-SNAPSHOT/udf_funcs/python_scripts/Unsupervised_Deep_Learning_of_Incompressible_Fluid_Dynamics')

from train import train

class MyTransformer:
    def __init__(self):
        pass

    def transform(self, rows):
        ret = [['parm', 'model_state']]
        
        for row in rows[1:]:
            line = []
            line.append(bytes("parm:" + str([row[1], row[2], row[3]]), 'utf-8'))
            line.append(bytes(str(train(row[1], row[2], row[3])), 'utf-8'))
            ret.append(line)

        return ret