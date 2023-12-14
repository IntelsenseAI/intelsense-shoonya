# Generated by Django 3.1.14 on 2022-05-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset", "0022_translationpair_context"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blocktext",
            name="domain",
            field=models.CharField(
                help_text="Domain of the block text",
                max_length=1024,
                verbose_name="domain",
            ),
        ),
        migrations.AlterField(
            model_name="blocktext",
            name="splitted_text",
            field=models.TextField(
                blank=True,
                help_text="Sentences Split from the Block Text",
                null=True,
                verbose_name="splitted_text",
            ),
        ),
        migrations.AlterField(
            model_name="blocktext",
            name="splitted_text_prediction",
            field=models.JSONField(
                blank=True,
                help_text="Prediction showing the block text split into sentences",
                null=True,
                verbose_name="splitted_text_prediction",
            ),
        ),
        migrations.AlterField(
            model_name="blocktext",
            name="text",
            field=models.TextField(
                help_text="A block of text having many sentences", verbose_name="text"
            ),
        ),
        migrations.AlterField(
            model_name="datasetbase",
            name="metadata_json",
            field=models.JSONField(
                blank=True,
                help_text="Metadata having details related to the annotation tasks or functions this data was involved in",
                null=True,
                verbose_name="metadata_json",
            ),
        ),
        migrations.AlterField(
            model_name="datasetinstance",
            name="dataset_type",
            field=models.CharField(
                choices=[
                    ("SentenceText", "SentenceText"),
                    ("TranslationPair", "TranslationPair"),
                    ("OCRDocument", "OCRDocument"),
                    ("BlockText", "BlockText"),
                ],
                help_text="Dataset Type which is specific for each annotation task",
                max_length=100,
                verbose_name="dataset_type",
            ),
        ),
        migrations.AlterField(
            model_name="datasetinstance",
            name="parent_instance_id",
            field=models.IntegerField(
                blank=True,
                help_text="The instance id of the source dataset",
                null=True,
                verbose_name="parent_instance_id",
            ),
        ),
        migrations.AlterField(
            model_name="sentencetext",
            name="domain",
            field=models.CharField(
                help_text="Domain of the Sentence",
                max_length=1024,
                verbose_name="domain",
            ),
        ),
        migrations.AlterField(
            model_name="sentencetext",
            name="is_profane",
            field=models.BooleanField(
                default=False,
                help_text="Indicates whether a sentence is profane or not.",
            ),
        ),
        migrations.AlterField(
            model_name="sentencetext",
            name="text",
            field=models.TextField(help_text="Sentence Text", verbose_name="text"),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="context",
            field=models.TextField(
                blank=True,
                help_text="Context of the sentence to be translated",
                null=True,
                verbose_name="context",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="input_text",
            field=models.TextField(
                help_text="The text to be translated", verbose_name="input_text"
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="labse_score",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Labse Score of the Translation",
                max_digits=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="machine_translation",
            field=models.TextField(
                blank=True,
                help_text="Machine translation of the sentence",
                null=True,
                verbose_name="machine_translation",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="output_text",
            field=models.TextField(
                blank=True,
                help_text="The translation of the sentence",
                null=True,
                verbose_name="output_text",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="rating",
            field=models.IntegerField(
                blank=True,
                help_text="Rating of the translation",
                null=True,
                verbose_name="translation_rating",
            ),
        ),
    ]