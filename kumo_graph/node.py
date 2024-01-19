from gqlalchemy import Node


class PackageType(Node):
    type: str


class PackageNamespace(Node):
    namespace: str


class PackageName(Node):
    name: str


class PackageVersion(Node):
    version: str


class PackageUrl(Node):
    purl: str


class Bom(Node):
    timestamp: str


class BomComponent(Node):
    ref: str
