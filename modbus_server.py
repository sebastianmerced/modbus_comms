#!/usr/bin/env python
"""
Pymodbus Synchronous Server Example
--------------------------------------------------------------------------

The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted is just not feasible. What follows is an example of its use:
"""
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer


from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
import threading
import random
# FORMAT = ('%(asctime)-15s %(threadName)-15s'
#           ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

def ident():
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = version.short()

    return identity


def rand_list():
    return [random.randrange(1, 50, 1) for i in range(100)]

def run_server(port):
   

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, rand_list()),
        co=ModbusSequentialDataBlock(0, [0]*100),
        hr=ModbusSequentialDataBlock(0, rand_list()),
        ir=ModbusSequentialDataBlock(0, rand_list())
    )

    context = ModbusServerContext(slaves=store, single=True)

    StartTcpServer(context, identity=ident(), address=("0.0.0.0", port))



if __name__ == "__main__":
    t1 = threading.Thread(target=run_server, args=(502,))
    t2 = threading.Thread(target=run_server, args=(503,))
    t3 = threading.Thread(target=run_server, args=(504,))
    t4 = threading.Thread(target=run_server, args=(505,))
    t5 = threading.Thread(target=run_server, args=(506,))
    t6 = threading.Thread(target=run_server, args=(507,))
    t7 = threading.Thread(target=run_server, args=(508,))
    t8 = threading.Thread(target=run_server, args=(509,))
    t9 = threading.Thread(target=run_server, args=(510,))
    t10 = threading.Thread(target=run_server, args=(511,))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
        

