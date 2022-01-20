from prefect import Flow, task
from prefect.executors import DaskExecutor

# from dask_kubernetes import KubeCluster, make_pod_spec
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun

import time


@task
def task():
    time.sleep(5)
    return 1 + 1


with Flow(name="kube") as flow:
    task()


flow.run_config = KubernetesRun()
flow.storage = GitHub(repo="Bada-S/kubernetes", path="flow.py")
flow.run()
