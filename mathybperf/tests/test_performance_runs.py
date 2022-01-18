import pytest
import subprocess
import glob


def setup_names():
    setup_list = glob.glob("./performance/setups/*.sh")
    setup_names = [s[s.rfind("/")+1:s.rfind(".")] for s in setup_list]
    return setup_names

base_path = './mathybperf/performance/results/mixed_poisson/pplus1pow3/'
setups = setup_names()

def run_profiler(name):
    proc = subprocess.run(["sh", "./performance/run_profiler.sh", name, "--verification"])
    if proc.returncode!=0:
        error_file = glob.glob(base_path+name+'**/verification.err', recursive=True)[0]
        error_message = open(error_file, "r").read()
    else:
        error_message="empty"
    assert proc.returncode==0, "Case "+name+" failed. Error message in file "+str(error_file)+": \n"+error_message


@pytest.mark.parametrize("name", setups)
def test_setups_mixed_poisson(name):
    run_profiler(name)
