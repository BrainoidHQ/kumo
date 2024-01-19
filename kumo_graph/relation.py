from gqlalchemy import Relationship


# PackageType --> PackageNamespace
class HasNamespace(Relationship):
    pass


# PackageType --> PackageName
# PackageNamespace --> PackageName
class HasName(Relationship):
    pass


# PackageName --> PackageVersion
class HasVersion(Relationship):
    pass


# PackageName --> PackageUrl
# PackageVersion --> PackageUrl
# BomComponent --> PackageUrl
class HasPurl(Relationship):
    pass


# Bom --> BomComponent:
class HasComponent(Relationship):
    pass


# BomComponent --> BomComponent
class DependsOn(Relationship):
    pass
