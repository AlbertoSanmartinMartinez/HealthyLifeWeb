from django.apps import AppConfig

class PostConfig(AppConfig):
    name = 'healthylife'

    def ready(self):
        pre_save.connect(createSlug, dender=self)


class CommentConfig(AppConfig):
    name = 'comment'
    verbose_name = 'Comment'

    def ready(self):
        import comment.signals
