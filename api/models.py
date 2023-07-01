from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.validators import Validator, MinLengthValidator
from tortoise.exceptions import ValidationError

from openoligo.seq import Seq, Category


class ValidSeq(Validator):
    """
    Validate that the value is a valid NA sequence
    """

    def __call__(self, value: str):
        try:
            Seq(value)
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc


class SequenceJob(Model):
    id = fields.IntField(pk=True)
    sequence = fields.TextField(validators=[ValidSeq(), MinLengthValidator(3)])
    category = fields.CharEnumField(enum_type=Category, default="DNA", required=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class InstrumentStatus(Model):
    id = fields.IntField(pk=True)
    reagents_loaded = fields.JSONField()
    queue_status = fields.CharField(max_length=200)
    max_queue_size = fields.IntField()


JobModelIn = pydantic_model_creator(SequenceJob, name="SequenceJob", exclude=("id", "created_at"))
JobModelOut = pydantic_model_creator(SequenceJob, name="SequenceJob")

InstrumentStatusModelIn = pydantic_model_creator(
    InstrumentStatus, name="InstrumentStatus", exclude=("id",)
)
InstrumentStatusModelOut = pydantic_model_creator(InstrumentStatus, name="InstrumentStatus")