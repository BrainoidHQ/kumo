from .cyclonedx import load_cyclonedx
from gqlalchemy import Memgraph


if __name__ == "__main__":
    db = Memgraph()
    with open('data/memgraph.cdx.json', mode='r') as f:
        data = f.read()
    load_cyclonedx(data, db)
