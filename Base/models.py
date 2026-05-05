from django.db import models


class Contact(models.Model):
    """Stores contact form submissions from portfolio visitors."""
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
