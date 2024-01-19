from typing import Dict, Iterable, Optional, cast
import json
from .purl import load_purl
from .node import Bom, BomComponent
from .relation import DependsOn, HasComponent, HasPurl
from cyclonedx.model.bom import Bom as CdxBom, BomMetaData
from cyclonedx.model.component import Component
from cyclonedx.model.dependency import Dependency
from cyclonedx.schema import SchemaVersion
from cyclonedx.validation.json import JsonStrictValidator


def load_cyclonedx(data: str, db):
    # validate
    validator = JsonStrictValidator(SchemaVersion.V1_5)
    err = validator.validate_str(data)
    if err is not None:
        raise Exception(err)

    bom = cast(CdxBom, CdxBom.from_json(json.loads(data)))  # type: ignore[attr-defined]
    components: Dict[str, BomComponent] = {}

    # metadata
    cdx_metadata = cast(BomMetaData, bom.metadata)
    if cdx_metadata.component is not None:
        component = load_component(cdx_metadata.component, db)
        if component is not None:
            components[component.ref] = component

    # components
    for cdx_component in cast(Iterable[Component], bom.components):
        component = load_component(cdx_component, db)
        if component is not None:
            components[component.ref] = component

    # dependencies
    for cdx_dependency in cast(Iterable[Dependency], bom.dependencies):
        load_dependency(cdx_dependency, components, db)


def load_metadata(cdx: BomMetaData, db) -> Optional[BomComponent]:
    bom = Bom(timestamp=cdx.timestamp.isoformat)
    bom.save(db)
    if cdx.component is not None:
        component = load_component(cdx.component, db)
        if component is not None:
            HasComponent(
                _start_node_id=bom._id,
                _end_node_id=component._id
            ).save(db)
        return component
    return None


def load_component(cdx: Component, db) -> Optional[BomComponent]:
    ref = cdx.bom_ref.value
    if ref is not None:
        component = BomComponent(ref=ref)
        component.save(db)
        if cdx.purl is not None:
            purl = load_purl(cdx.purl.to_string(), db)
            HasPurl(
                _start_node_id=component._id,
                _end_node_id=purl._id
            ).save(db)
        return component
    return None


def load_dependency(cdx: Dependency, components: Dict[str, BomComponent], db):
    start = cdx.ref.value
    for dependency in cast(Iterable[Dependency], cdx.dependencies):
        end = dependency.ref.value
        if start is not None and end is not None:
            DependsOn(
                _start_node_id=components[start]._id,
                _end_node_id=components[end]._id
            ).save(db)
