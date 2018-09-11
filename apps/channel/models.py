from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    rules = models.TextField(blank=True)
    moderators = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='moderators')

    def __str__(self):
        return self.name

    def get_channel_rule(self, index):
        rule_list = rules.split('\n')
        return rule_list[index]
