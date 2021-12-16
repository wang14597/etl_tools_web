import grpc
from google.protobuf import empty_pb2
from proto_py.ApplicationManagerService_pb2 import GetDependenciesRequest


class ApplicationManagerClient:

    def __init__(self, address, service):
        self._channel = grpc.insecure_channel(address)
        self._stub = service(self._channel)

    def get_jobs(self):
        jobs = self._stub.getJobs(empty_pb2.Empty())
        return jobs.jobId

    def get_dependencies(self, **kwargs):
        dependencies = self._stub.getDependencies(
            GetDependenciesRequest(jobId=kwargs.get("job_id", None), taskId=kwargs.get("task_id", None)))
        return dependencies.stages
