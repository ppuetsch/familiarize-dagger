"""Execute a command."""

import sys

import anyio

import dagger


async def test():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")
        base_python_container = (
            client.container()
            .from_("python:3.11-slim-buster")
            .with_directory("/src", src)
            .with_workdir("/src")
            .with_exec(["pip", "install", "pytest", "black"])
        )
        unittest = base_python_container.with_env_variable("PYTHONPATH", ".").with_exec(
            ["pytest"]
        )

        await unittest

        lint = base_python_container.with_exec(["black", "--check", "."])

        await lint

        nginx_container = client.container().build(src)

        nginx_container_as_service = nginx_container.as_service()

        check_service = (
            client.container()
            .from_("alpine:latest")
            .with_service_binding("hallo_nginx", nginx_container_as_service)
            .with_exec(["wget", "-O", "-", "hallo_nginx"])
        )

        service_output = await check_service.stdout()

        print(f"sucessfully finished all tests. Service Output = {service_output}")


anyio.run(test)
