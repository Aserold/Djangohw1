from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sensor} - {self.temperature}°C at {self.created_at}"
