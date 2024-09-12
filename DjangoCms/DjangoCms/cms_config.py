from djangocms_versioning.datastructures import VersionableItem
from cms.models import PageContent
from djangocms_versioning.models import Version
from djangocms_versioning.cms_config import VersioningCMSConfig

class MyAppCMSConfig(VersioningCMSConfig):
    versioning = [
        VersionableItem(
            content_model=PageContent,
            grouper_field_name='page',
            copy_function=None,
            concrete=True,
        ),
    ]