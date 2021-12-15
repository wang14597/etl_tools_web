from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import FastAPI
from model import *
from proto_py.etl_tool_client import ApplicationManagerClient
from proto_py.ApplicationManagerService_pb2_grpc import ApplicationManagerServiceStub


app = FastAPI()
router = InferringRouter()


@cbv(router)
class WebServer:
    application_manager_client = ApplicationManagerClient("127.0.0.1:9999", ApplicationManagerServiceStub)

    @router.get("/")
    def read_root(self):
        h = HelloWorld(content="hello")
        return h.json()

    @router.get("/jobs")
    def get_jobs(self):
        with self.application_manager_client as client:
            jobs = client.get_jobs()
        return Jobs(jobs=jobs).json()

    @router.get("/jobs/{job_id}")
    def get_dependency(self, job_id):
        with self.application_manager_client as client:
            dependencies = client.get_dependencies(job_id=job_id)
        return dependencies


app.include_router(router)
