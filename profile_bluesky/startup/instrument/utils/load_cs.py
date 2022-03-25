""" Loads a new eiger device """

from ..devices.cryostream import OXFORD_CS800
from ..devices.ad_lightfield import LocalLightfieldDetector
from ..framework import sd
from ..session_logs import logger
logger.info(__file__)

__all__ = """
    load_cs800
""".split()


def load_cs800(pv="17bmCryo:BM:"):

    print("-- Loading CryoStream 800 --")
    cs800 = LocalVarexDetector(pv, name="cs800")
    sd.baseline.append(cs800)
     
    # Is this necessary? Was used previously as .get would fail!!!
     cs800.wait_for_connection(timeout=10)

    print("Done!")
    print("All done!")

	cs800 = oxford_cs800("17bmCryo:BM:", name="cs800")
	cs800.report_dmov_changes.put(True)  # a diagnostic
	cs800.tolerance.put(1.0)  # done when |readback-setpoint|<=tolerance

    return cs800
