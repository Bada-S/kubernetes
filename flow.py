from prefect import Flow, task
from prefect.executors import DaskExecutor
from dask_kubernetes import KubeCluster, make_pod_spec
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun


@task
def task():
    return 1 + 1


with Flow() as flow:
    task()

flow.run(storage=storage)
