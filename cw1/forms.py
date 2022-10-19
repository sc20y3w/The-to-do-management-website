import wtforms
from wtforms.validators import length, data_required, regexp


# Form validation to see if the input is formatted, otherwise the add page will be cleared
class AddForm(wtforms.Form):
    title = wtforms.SearchField(validators=[length(min=1, max=30)])
    description = wtforms.SearchField(validators=[length(min=1, max=30)])
    ddl = wtforms.SearchField(validators=[data_required()])
    finish = wtforms.SearchField(validators=[data_required(), regexp('True|true|TRUE|False|false|FALSE', 0,
                                                                     'Invalid status')])
    # You must write the right module name, otherwise it will clear the add page, and you need to rewrite it.
    module_id = wtforms.SearchField(validators=[data_required(), regexp('XJCO2011|XJCO2211|XJCO2321|XJCO2421|XJCO2711',
                                                                        0, 'Invalid status')])

    # At first, I decided that the title could not be duplicated, so I added validation
    # But later I thought that the title could be repeated, for example, each unit has a cwk1, so I commented it out

    # def validate_title(self, field):
    #     title = field.data
    #     title_model = Total.query.filter_by(title=title).first()
    #     if title_model:
    #         raise wtforms.ValidationError("The title already exists.")
