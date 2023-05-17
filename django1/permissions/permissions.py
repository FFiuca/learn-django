from django.contrib.auth.models import Permission

class CanPublishPost(Permission):
    codename = 'can_publish_post'
    name = 'Can publish blog post'