from typing import Any
from .node import PackageType, PackageNamespace, PackageName, PackageVersion, PackageUrl
from .relation import HasNamespace, HasName, HasVersion, HasPurl
from packageurl import PackageURL


def load_purl(data: str, db: Any) -> PackageUrl:
    url = PackageURL.from_string(data)

    ptype = PackageType(type=url.type)
    ptype.save(db)

    pname = PackageName(name=url.name)
    pname.save(db)

    purl = PackageUrl(purl=data)
    purl.save(db)

    if url.namespace is None:
        HasName(
            _start_node_id=ptype._id,
            _end_node_id=pname._id
        ).save(db)
    else:
        pnamespace = PackageNamespace(namespace=url.namespace)
        pnamespace.save(db)

        HasNamespace(
            _start_node_id=ptype._id,
            _end_node_id=pnamespace._id
        ).save(db)
        HasName(
            _start_node_id=pnamespace._id,
            _end_node_id=pname._id
        ).save(db)

    if url.version is None:
        HasPurl(
            _start_node_id=pname._id,
            _end_node_id=purl._id
        ).save(db)
    else:
        pversion = PackageVersion(version=url.version)
        pversion.save(db)

        HasVersion(
            _start_node_id=pname._id,
            _end_node_id=pversion._id
        ).save(db)
        HasPurl(
            _start_node_id=pversion._id,
            _end_node_id=purl._id
        ).save(db)

    return purl
