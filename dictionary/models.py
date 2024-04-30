from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(verbose_name="avatar", upload_to='avatars/', blank=True, null=True)

    @property
    def text(self):
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Dictionary(models.Model):
    dictionary_name = models.CharField(max_length=255, verbose_name="Dictionary name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    date_created = models.DateTimeField(verbose_name="Date time created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date time updated", auto_now=True)
    logo = models.ImageField(verbose_name="Logo", blank=True, null=True, upload_to="dictionary_logo")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Owner", blank=True, null=True)

    def __str__(self):
        return self.dictionary_name

    @property
    def get_words_count(self):
        return self.words.count()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'


class Word(models.Model):
    word_rus = models.CharField(max_length=255, verbose_name="Word rus")
    word_eng = models.CharField(max_length=255, verbose_name="Word eng")
    date_created = models.DateTimeField(verbose_name="Date time created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date time updated", auto_now=True)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="Dictionary", related_name="words")

    def __str__(self):
        return self.word_rus + ' ' + self.word_eng

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

