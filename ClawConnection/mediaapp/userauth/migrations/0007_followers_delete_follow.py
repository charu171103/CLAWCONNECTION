from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_follow_delete_followerscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
