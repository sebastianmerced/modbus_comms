#!/usr/bin/env python
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer


from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
import threading
import random
import sys
import time

FORMAT = (
    "%(asctime)-15s %(threadName)-15s"
    " %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def ident():
    identity = ModbusDeviceIdentification()
    identity.VendorName = "Pymodbus"
    identity.ProductCode = "PM"
    identity.VendorUrl = "http://github.com/riptideio/pymodbus/"
    identity.ProductName = "Pymodbus Server"
    identity.ModelName = "Pymodbus Server"
    identity.MajorMinorRevision = version.short()

    return identity


def rand_list():
    return [random.randrange(1, 50, 1) for i in range(100)]


def run_server(port):

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, rand_list()),
        co=ModbusSequentialDataBlock(0, [0] * 100),
        hr=ModbusSequentialDataBlock(0, rand_list()),
        ir=ModbusSequentialDataBlock(0, rand_list()),
    )

    context = ModbusServerContext(slaves=store, single=True)

    StartTcpServer(context, identity=ident(), address=("0.0.0.0", port))


if __name__ == "__main__":

    if len(sys.argv) < 3:
        logging.error("Must indicate number of threads and starting port")
        sys.exit()

    try:
        thread_count = int(sys.argv[1])
        port = int(sys.argv[2])
    except:
        logging.error("Invalid argument types")
        sys.exit()

    threads = list()
    for i in range(thread_count):
        logging.info(f"Starting server thread with port {port}")
        thread = threading.Thread(target=run_server, args=(port,))
        threads.append(thread)
        thread.start()
        port += 1

    try:
        while True:
            time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Stopping...")
    except Exception as e:
        logging.error(f"Unexpected exception occured: {str(e)}")
    finally:
        for index, thread in enumerate(threads):
            logging.info(f"Stopping thread {index}...")
            thread.join()
        logging.info(f"All threads stopped")
        sys.exit(0)
